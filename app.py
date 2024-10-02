from flask import Flask, request, render_template, redirect, url_for
import subprocess
import os

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
        # Ruta absoluta del script de PowerShell
        script_path = os.path.abspath("scripts/powershell_script.ps1")
        
        # Ejecutar el script de PowerShell cuando la contraseña es incorrecta
        subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", script_path])
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
    app.run(debug=True)
