from flask_redis import FlaskRedis
from quart import *
import redis
# from tortoise.contrib.quart import register_tortoise

from app.db import engine, Base
from quart_schema import QuartSchema

schema = QuartSchema()

redis = redis.from_url("redis://:123456@localhost:6379")


def create_app():
    app = Quart(__name__)
    schema.init_app(app)


    app.config.from_pyfile('config.py')


    @app.route("/", methods=['GET'])
    def home():
        return jsonify({"msg": "Hello World"})

    from .routes import quart_app

    app.register_blueprint(quart_app)

    @app.after_request
    def after_request(response):
        header = response.headers
        header.add('Access-Control-Allow-Origin', '*')
        header.add('Access-Control-Allow-Headers', '*')
        header.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    @app.before_first_request
    async def init_tables():
        async with engine.begin() as conn:
            # await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    # register_tortoise(
    #     app,
    #     db_url="postgres://postgres:123456@localhost:5432/quart",
    #     modules={"models": ['app.models']},
    #     generate_schemas=True,
    # )

    return app
