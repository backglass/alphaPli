from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ["SECRET_KEY"] = "mysecretkey"

## Base Database Config

app.config ["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:plisados123@localhost:5432/plisafor"
app.config ["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Clientes(db.Model):

    __tablename__ = "clientes"

    nif = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100))
    telefono = db.Column(db.String(100))
    teledono_movil = db.Column(db.String(100))
    email = db.Column(db.String(100))
    direccion = db.Column(db.String(100), nullable=False)
    notas = db.Column(db.String(10000))

    def __init__(self, nif, nombre, apellidos, telefono, teledono_movil, email, direccion, notas):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.teledono_movil = teledono_movil
        self.email = email
        self.direccion = direccion
        self.notas = notas
    
    def __repr__(self):
        return f"Cliente('{self.nif}', '{self.nombre}', '{self.apellidos}', '{self.telefono}', '{self.teledono_movil}', '{self.email}', '{self.direccion}', '{self.notas}')"

db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html', clientes=Clientes.query.all())

@app.route('/<int:nif>/ver_cliente')
def ver(nif):
    return render_template('ver_cliente.html', cliente=Clientes.query.filter_by(nif=nif).first())


if __name__ == '__main__':
    app.run(debug=True)
    
