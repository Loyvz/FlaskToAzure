from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Contraseña correcta
PASSWORD_CORRECTA = "idodjnoijaojcoic"

# Ruta para el formulario de contraseña
@app.route('/')
def index():
    return render_template('password.html')

# Ruta para procesar la contraseña
@app.route('/verificar', methods=['POST'])
def verificar():
    contrasena = request.form['contrasena']
    
    if contrasena == PASSWORD_CORRECTA:
        return redirect(url_for('felicidades'))
    else:
        return redirect(url_for('error'))

# Página de éxito si la contraseña es correcta
@app.route('/felicidades')
def felicidades():
    return render_template('felicidades.html')

# Página de error si la contraseña es incorrecta
@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run()
