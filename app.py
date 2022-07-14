from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask_wtf import FlaskForm
app = Flask(__name__)
app.config ["SECRET_KEY"] = "mysecretkey"


## Base Database Config

app.config ["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:plisados123@localhost:5432/plisafor"
app.config ["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Clase para el formulario de crear clientes
class Insertar_cliente(FlaskForm):
    nif = StringField("NIF", validators=[validators.DataRequired()])
    nombre = StringField("Nombre", validators=[validators.DataRequired()])
    telefono = StringField("Telefono", validators=[validators.DataRequired()])
    telefono_movil = StringField("Telefono Movil")
    email = StringField("Email")
    direccion = StringField("Direccion")
    notas = TextAreaField("Notas")


# Clase cliente hereda de db.Model, servira para crear la tabla en la base de datos y usar sus datos
class Clientes(db.Model):

    __tablename__ = "clientes"

    nif = db.Column(db.String(15), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(100))
    teledono_movil = db.Column(db.String(100))
    email = db.Column(db.String(100))
    direccion = db.Column(db.String(100), nullable=False)
    notas = db.Column(db.String(10000))

    def __init__(self, nif, nombre, telefono, teledono_movil, email, direccion, notas):
        self.nif = nif
        self.nombre = nombre
        self.telefono = telefono
        self.teledono_movil = teledono_movil
        self.email = email
        self.direccion = direccion
        self.notas = notas
    
    def __repr__(self):
        return f"Cliente('{self.nif}', '{self.nombre}', '{self.telefono}', '{self.teledono_movil}', '{self.email}', '{self.direccion}', '{self.notas}')"
 
db.create_all()  # Crea la tabla en la base de datos


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/clientes')  # Ruta para la pagina de list de clientes 
def clientes():
    return render_template('clientes.html', clientes=Clientes.query.all()) # Muestra todos los clientes en la base de datos



@app.route('/clientes/<ver_cliente>') # Ruta para la pagina de ver cliente es dinamica porque se le pasa el nif del cliente 
def ver(ver_cliente):
    return render_template('ver_cliente.html', cliente=Clientes.query.filter_by(nif=ver_cliente).first()) # Muestra el cliente en la base de datos con el nif que se le pasa



@app.route("/clientes/crear", methods=["GET", "POST"]) # Ruta para la pagina de crear cliente 
def crear_cliente():
    
    form = Insertar_cliente() # Crea el formulario de crear cliente objeto form 
    if form.validate_on_submit(): # Si el formulario es validado
        
        # Crea un nuevo cliente con los datos del formulario 
        cliente = Clientes(form.nif.data, form.nombre.data, form.telefono.data, form.telefono_movil.data, form.email.data, form.direccion.data, form.notas.data)
        db.session.add(cliente)
        
        try: # Intenta guardar los datos en la base de datos
            db.session.commit() # Guarda los datos en la base de datos
            flash("Cliente creado correctamente") # Muestra un mensaje de que el cliente se ha creado correctamente
            return redirect(url_for('clientes'))  # Redirige a la pagina de lista de clientes
        
        except: # Si no se puede guardar en la base de datos 
            flash("Error al crear el cliente")
            return redirect(url_for('clientes'))
        
    return render_template('crear_cliente.html',form=form)

@app.route("/clientes/editar/<nif>", methods=["GET", "POST"]) # Ruta para la pagina de editar cliente
def editar_cliente(nif):
    cliente = Clientes.query.filter_by(nif=nif).first()
    form = Insertar_cliente()
    if form.validate_on_submit():
        cliente.nombre = form.nombre.data
        cliente.telefono = form.telefono.data
        cliente.teledono_movil = form.telefono_movil.data
        cliente.email = form.email.data
        cliente.direccion = form.direccion.data
        cliente.notas = form.notas.data
        db.session.commit()
        flash("Cliente editado correctamente")
        return redirect(url_for('clientes'))
    return render_template('editar_cliente.html', form=form, cliente=cliente)

@app.route("/clientes/eliminar/<nif>", methods=["GET", "POST"]) # Ruta para la pagina de eliminar cliente
def eliminar_cliente(nif):
    cliente = Clientes.query.filter_by(nif=nif).first()
    db.session.delete(cliente)
    db.session.commit()
    flash("Cliente eliminado correctamente")
    return redirect(url_for('clientes'))
if __name__ == '__main__':
    app.run(debug=True)
    
