from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("layout.html")

@app.route('/servicios')
def servicios():
    return render_template("servicios.html")

#La última pieza sirve para que el servidor actualice los cambios sin volver a desplegar el server de nuevo
if __name__ == '__main__':
    app.run(debug=True)