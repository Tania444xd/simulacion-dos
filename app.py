from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h2>Simulación de Login</h2>
        <form method="POST" action="/login">
            Usuario: <input name="user"><br>
            Contraseña: <input type="password" name="pass"><br>
            <button type="submit">Ingresar</button>
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    password = request.form['pass']
    return f"<h3>Hola, {user}. Tus datos fueron enviados. (sin validar)</h3>"
