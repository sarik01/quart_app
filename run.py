from app import create_app, engine, Base

app = create_app()

if __name__ == '__main__':
    app.run(debug=True,  port=9000)
