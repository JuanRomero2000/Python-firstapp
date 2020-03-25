# crear un programa escrito en Python que valide mediante expresiones regulares contraseñas así: A485btf%$(
# Es decir que valide contraseña de la siguiente manera:
#   - El primer carácter debe ser  una letra mayúscula.
#   - Los siguientes 3 caracteres son números.
#   - Después los siguientes caracteres deben ser letras minúsculas.
#   - Y los últimos 3 caracteres deben ser caracteres especiales. 

from flask import Flask, render_template,request
import re

#objeto
app=Flask(__name__)

@app.route('/')#pagina principal

def home():

    return render_template('home.html')


#expresion que operamos en la ventana
patron = patron=re.compile(r"^[A-Z]{1}\d{3}[a-z]+\W{3}$")

@app.route('/validar',methods=['POST'])

def validar():
    if request.method=='POST':
        expresion=request.form['expresion']

        if(patron.match(expresion)):

                return correcto()
        else:
                return incorrecto()


@app.route('/home/correcto')
def correcto():
    return render_template('correcto.html')

@app.route('/home/incorrecto')
def incorrecto():
    return render_template('incorrecto.html')

#escuchar siempre
if __name__=='__main__':
    app.run(debug=True)