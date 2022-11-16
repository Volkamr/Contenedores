from flask import Flask

app = Flask(__name__)

@app.route('/')
def usuario():
    return 'este es la pagina de un usuario'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
