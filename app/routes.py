import json
from functools import reduce

from quart import Blueprint, request, jsonify
from sqlalchemy import select

from app import redis
from app.db import User, session, User_test
from quart_schema import validate_request, validate_response, DataSource

# from app.models import User

quart_app = Blueprint('quart_app', __name__)


def list_of_cols_from(cls):
    return [column.key for column in cls.__table__.c]


# @quart_app.post('/create_user')
# async def create_user():
#     username = (await request.form)['username']
#     email = (await request.form)['email']
#
#     await User.create(username=username, email=email)
#
#     return jsonify({'msg': 'ok'})


@quart_app.get('/get_user')
async def get_user() -> list:
    cashed = redis.get('users')
    if cashed:
        print('cashed')
        return json.loads(cashed)
    # id = request.args.get('id')
    # user = await User.get(id=id)
    # posts = User.all()
    user = await session.execute(select(User).order_by(User.id.desc()))
    result = [x.format() for x in user.scalars()]
    redis.set(f'users', json.dumps(result), ex=200)
    return jsonify(result)

@quart_app.post('/create_user')
# @validate_request(User_test, source=DataSource.FORM)
# @validate_response(User, 201)
async def createUser():
    # username = (await request.form)['username']
    # email = (await request.form)['email']
    # print(username, email)
    ik_cols = list_of_cols_from(User)
    print(ik_cols)
    ik = User()
    for col in ik_cols:
        if col == 'id':
            pass
        else:
            val = (await request.form)[col]
            print(val)
            if val:
                setattr(ik, col, val)
    session.add(ik)
    await session.commit()
    # user = User(username=username, email=email)
    # session.add(user)
    # await session.commit()

    return jsonify(ik.format())


@quart_app.get('/get_one_user')
async def getOneUser():
    id = request.args.get('id')
    user = await session.execute(select(User).filter_by(id=int(id)))
    result = user.scalar()

    return jsonify(result.format())


@quart_app.post('/update_user')
async def UpdateUser():
    data = (await request.form)

    id = (await request.form)['id']
    # username = (await request.form)['username']
    # email = (await request.form)['email']
    user_query = await session.execute(select(User).filter_by(id=int(id)))
    user = user_query.scalar()

    cols = list_of_cols_from(User)

    for col in cols:
        if col == 'id':
            pass
        else:
            val = data[col]
            if val:
                setattr(user, col, val)


    #
    # user.username = username
    # user.email = email

    await session.commit()

    return jsonify(user.format())


@quart_app.get('/delete_user')
async def deleteUser():
    id = request.args.get('id')
    user_query = await session.execute(select(User).filter_by(id=int(id)))
    user = user_query.scalar()
    await session.delete(user)
    await session.commit()

    return jsonify(user.format())


import docx

def concat(x, y):
    return x + y


@quart_app.get('/get_docx')
async def GetDocx():
    doc = docx.Document('1-файл_иш_тури.docx')

    for paragraph in doc.paragraphs:
        if paragraph.text == '':
            pass
            # print(paragraph.text, 'ssss')
        else:
            # print(paragraph.text)
            digit = []
            text = []
            russ = []
            for i in paragraph.text[0:5]:
                if i == '.':
                    digit.append(i)
                if i.isnumeric():
                    digit.append(i)
            for i in paragraph.text:
                s = paragraph.text

                if i == '(' or i == ')':
                    index = s.find(i)
                    if index != -1:
                        russ.append(paragraph.text[int(index)::])
                        text.append(paragraph.text[::int(index)])
                if i == ' ':
                    text.append('_')
                if i.isnumeric():
                    pass
                else:
                    text.append(i)


            digit_str = ' '.join(digit).replace(' ', '')
            text_str = ' '.join(text).replace('.', '').replace(' ', '').replace('_', ' ')
            rus_str = ' '.join(russ).replace('.', '').replace(' ', '').replace('_', ' ')
            # print(text)
            print(digit_str)
            print(str(text_str))
            print(str(rus_str))



    return 'ok'