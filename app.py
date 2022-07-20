from datetime import datetime
import time
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Date, DateTime, Integer, String, Column, ForeignKey
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
    precio_metro = StringField("Precio Metro", validators=[validators.DataRequired()])
    notas = TextAreaField("Notas")

# Clase para crear formulario facturas 
class Nueva_factura(FlaskForm):
    numero = StringField("Numero")
    nif = StringField("NIF")
    fecha = StringField("Fecha")

    precio1 = StringField("Precio1")
    precio2 = StringField("Precio2")
    precio3 = StringField("Precio3")
    precio4 = StringField("Precio4")
    precio5 = StringField("Precio5")
    precio6 = StringField("Precio6")
    precio7 = StringField("Precio7")
    precio8 = StringField("Precio8")

    descripcion1 = StringField("Descripcion1")
    descripcion2 = StringField("Descripción2")
    descripcion3 = StringField("Descripción3")
    descripcion4 = StringField("Descripción4")
    descripcion5 = StringField("Descripción5")
    descripcion6 = StringField("Descripción6")
    descripcion7 = StringField("Descripción7")
    descripcion8 = StringField("Descripción8")
    
    metros1 = StringField("Metros1")
    metros2 = StringField("Metros2")
    metros3 = StringField("Metros3")
    metros4 = StringField("Metros4")
    metros5 = StringField("Metros5")
    metros6 = StringField("Metros6")
    metros7 = StringField("Metros7")
    metros8 = StringField("Metros8")

    faldas1 = StringField("Faldas1")
    faldas2 = StringField("Faldas2")
    faldas3 = StringField("Faldas3")
    faldas4 = StringField("Faldas4")
    faldas5 = StringField("Faldas5")
    faldas6 = StringField("Faldas6")
    faldas7 = StringField("Faldas7")
    faldas8 = StringField("Faldas8")

    importe1 = StringField("Importe1")
    importe2 = StringField("Importe2")
    importe3 = StringField("Importe3")
    importe4 = StringField("Importe4")
    importe5 = StringField("Importe5")
    importe6 = StringField("Importe6")
    importe7 = StringField("Importe7")
    importe8 = StringField("Importe8")

    precio_metro = StringField("Precio Metro")
    sub_total_sin_iva  = StringField("Subtotal")
    total_con_iva = StringField("Total")
    notas = TextAreaField("Notas")


# Clase cliente hereda de db.Model, servira para crear la tabla en la base de datos y usar sus datos
class Clientes(db.Model):

    __tablename__ = "cliente"

    nif = db.Column(db.String(15), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(100))
    teledono_movil = db.Column(db.String(100))
    email = db.Column(db.String(100))
    direccion = db.Column(db.String(100), nullable=False)
    precio_metro = db.Column(db.String(10))
    notas = db.Column(db.String(10000))

    def __init__(self, nif, nombre, telefono, teledono_movil, email, direccion,precio_metro, notas):
        self.nif = nif
        self.nombre = nombre
        self.telefono = telefono
        self.teledono_movil = teledono_movil
        self.email = email
        self.direccion = direccion
        self.precio_metro = precio_metro
        self.notas = notas
            
    def __repr__(self):
        return f"Cliente('{self.nif}', '{self.nombre}', '{self.telefono}', '{self.teledono_movil}', '{self.email}', '{self.direccion}','{self.precio_metro} '{self.notas}')"
 


    
class Facturas(db.Model): # Clase Facturas hereda de db.Model, servira para crear la tabla en la base de datos y usar sus datos

    __tablename__ = "factura"

    num = db.Column(db.Integer, primary_key=True)
    nif = db.Column(db.String(30), db.ForeignKey("cliente.nif"))
    fecha = db.Column(db.DateTime(timezone = True))
    
    precio1 = db.Column(db.String(10))
    precio2 = db.Column(db.String(10))
    precio3 = db.Column(db.String(10))
    precio4 = db.Column(db.String(10))
    precio5 = db.Column(db.String(10))
    precio6 = db.Column(db.String(10))
    precio7 = db.Column(db.String(10))
    precio8 = db.Column(db.String(10))
    
    descripcion1 = db.Column(db.String(100))
    descripcion2 = db.Column(db.String(100))
    descripcion3 = db.Column(db.String(100))
    descripcion4 = db.Column(db.String(100))
    descripcion5 = db.Column(db.String(100))
    descripcion6 = db.Column(db.String(100))
    descripcion7 = db.Column(db.String(100))
    descripcion8 = db.Column(db.String(100))

    metros1 = db.Column(db.String(10))
    metros2 = db.Column(db.String(10))
    metros3 = db.Column(db.String(10))
    metros4 = db.Column(db.String(10))
    metros5 = db.Column(db.String(10))
    metros6 = db.Column(db.String(10))
    metros7 = db.Column(db.String(10))
    metros8 = db.Column(db.String(10))

    faldas1 = db.Column(db.String(10))
    faldas2 = db.Column(db.String(10))
    faldas3 = db.Column(db.String(10))
    faldas4 = db.Column(db.String(10))
    faldas5 = db.Column(db.String(10))
    faldas6 = db.Column(db.String(10))
    faldas7 = db.Column(db.String(10))
    faldas8 = db.Column(db.String(10))

    importe1 = db.Column(db.String(10))
    importe2 = db.Column(db.String(10))
    importe3 = db.Column(db.String(10))
    importe4 = db.Column(db.String(10))
    importe5 = db.Column(db.String(10))
    importe6 = db.Column(db.String(10))
    importe7 = db.Column(db.String(10))
    importe8 = db.Column(db.String())

    pagada = db.Column(db.Boolean())
    subtotal  = db.Column(db.String(10))
    total = db.Column(db.String(10))
    precio_metro = db.Column(db.Float())
    notas = db.Column(db.String(1000))

    def __init__(self, nif, fecha,
                 precio1,precio2,precio3,precio4,precio5,precio6,precio7,precio8,
                 descripcion1,descripcion2,descripcion3,descripcion4,descripcion5,descripcion6,descripcion7,descripcion8,
                 metros1,metros2,metros3,metros4,metros5,metros6,metros7,metros8,
                 faldas1,faldas2,faldas3,faldas4,faldas5,faldas6,faldas7,faldas8,
                 importe1,importe2,importe3,importe4,importe5,importe6,importe7,importe8,
                 pagada,subtotal,total,precio_metro,notas):

        self.nif = nif
        self.fecha = fecha
        self.precio1 = precio1
        self.precio2 = precio2
        self.precio3 = precio3
        self.precio4 = precio4
        self.precio5 = precio5
        self.precio6 = precio6
        self.precio7 = precio7
        self.precio8 = precio8

        self.descripcion1 = descripcion1
        self.descripcion2 = descripcion2
        self.descripcion3 = descripcion3
        self.descripcion4 = descripcion4
        self.descripcion5 = descripcion5
        self.descripcion6 = descripcion6
        self.descripcion7 = descripcion7
        self.descripcion8 = descripcion8
        
        self.metros1 = metros1
        self.metros2 = metros2
        self.metros3 = metros3
        self.metros4 = metros4
        self.metros5 = metros5
        self.metros6 = metros6
        self.metros7 = metros7
        self.metros8 = metros8

        self.faldas1 = faldas1
        self.faldas2 = faldas2
        self.faldas3 = faldas3
        self.faldas4 = faldas4
        self.faldas5 = faldas5
        self.faldas6 = faldas6
        self.faldas7 = faldas7
        self.faldas8 = faldas8
        
        self.importe1 = importe1
        self.importe2 = importe2
        self.importe3 = importe3
        self.importe4 = importe4
        self.importe5 = importe5
        self.importe6 = importe6
        self.importe7 = importe7
        self.importe8 = importe8
        
        self.pagada = pagada
        self.subtotal = subtotal
        self.total = total
        self.precio_metro = precio_metro
        self.notas = notas
        

    def __repr__(self):
        return '<Factura %r>' % self.id 

class Borrar(db.Model):

    __tablename__ = "borrar"

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone = True) )
    nombre = db.Column(db.String(100))


    def __init__(self,numero,date,nombre):
        
        self.numero = numero
        self.date = date
        self.nombre = nombre
    
    
    def __repr__(self):
        return f"Cliente('{self.nif}', '{self.nombre}')"


db.create_all()  # Crea la tabla en la base de datos

@app.route('/borrar', methods=['GET', 'POST'])
def borrar():
    p1 = Borrar(2,time.strftime("%d/%m/%y"), "Juan")
    db.session.add(p1)
    db.session.commit()
    p2 = Borrar.query.filter_by(id=1).first()
    fec = datetime.date(p2.date)    ## Recupera la fecha de la base de datos esta en formato estados unidos
    print(fec.strftime("%d/%m/%y")) ## La formatea en formato europeo
    return redirect(url_for('index'))

@app.route('/')  # Ruta raiz
def index():
    return render_template('index.html')



@app.route('/clientes')  # Ruta para la pagina de lista de clientes 
def clientes():
    return render_template('clientes.html', clientes=Clientes.query.all()) # Muestra todos los clientes en la base de datos



@app.route('/clientes/<ver_cliente>') # Ruta para la pagina de ver un cliente es dinamica porque se le pasa el nif del cliente 
def ver_cliente(ver_cliente):
    cliente = Clientes.query.filter_by(nif=ver_cliente).first() # Busca el cliente en la base de datos
    factura = Facturas.query.filter_by(nif=ver_cliente).all() # Busca las facturas del cliente en la base de datos
    return render_template('ver_cliente.html',cliente=cliente, facturas=factura) # Devuelve la variable cliente con los datos del nif pasado por parametro



@app.route("/clientes/crear", methods=["GET", "POST"]) # Ruta para la pagina de crear cliente 
def crear_cliente():
    
    form = Insertar_cliente()     # Crea el formulario de crear cliente objeto form 
    if form.validate_on_submit(): # Si el formulario es validado
        
        # Crea un nuevo cliente con los datos del formulario 
        cliente = Clientes(form.nif.data, form.nombre.data, form.telefono.data, form.telefono_movil.data, form.email.data, form.direccion.data,form.precio_metro.data, form.notas.data)
        db.session.add(cliente)
        
        try:                                      # Intenta guardar los datos en la base de datos
            db.session.commit()                   # Guarda los datos en la base de datos
            flash("Cliente creado correctamente") # Muestra un mensaje de que el cliente se ha creado correctamente
            return redirect(url_for('clientes'))  # Redirige a la pagina de lista de clientes
        
        except:                                   # Si no se puede guardar en la base de datos 
            flash("Error al crear el cliente")
            return redirect(url_for('clientes'))
        
    return render_template('crear_cliente.html',form=form)


@app.route("/clientes/editar/<nif>", methods=["GET", "POST"]) # Ruta para la pagina de editar cliente
def editar_cliente(nif):

   
    cliente = Clientes.query.filter_by(nif=nif).first() # Busca el cliente en la base de datos con el nif que se le pasa en la ruta
    form = Insertar_cliente()                           # Crea una instancia del formulario de cr
    
    if form.validate_on_submit():
        
        cliente.nombre = form.nombre.data
        cliente.telefono = form.telefono.data
        cliente.teledono_movil = form.telefono_movil.data
        cliente.email = form.email.data
        cliente.direccion = form.direccion.data
        cliente.precio_metro = form.precio_metro.data
        cliente.notas = form.notas.data
        
        db.session.commit()
        flash("Cliente editado correctamente")
        return redirect(url_for('clientes'))
        
    return render_template('editar_cliente.html', form=form, cliente=cliente) # manda form y cliente a la pagina de editar cliente


@app.route("/clientes/eliminar/<nif>", methods=["GET", "POST"]) # Ruta para la pagina de eliminar cliente
def eliminar_cliente(nif):
    
    cliente = Clientes.query.filter_by(nif=nif).first()   # Busca el cliente en la base de datos con el nif que se le pasa por la ruta
    db.session.delete(cliente)
    db.session.commit()
    flash("Cliente eliminado correctamente")
    return redirect(url_for('clientes'))


@app.route("/facturas") # Ruta para ver la lista de todas las facturas
def facturas():
    return render_template('facturas.html', facturas=Facturas.query.all())


# @app.route("/facturas/nueva/<nif>", methods = ["GET","POST"]) # Ruta para la pagina de crear factura


# def nueva_factura(nif): # Funcion para crear una nueva factura
    
#     cliente = Clientes.query.filter_by(nif=nif).first()      # Usaos el nif que se le pasa por la ruta para buscar el cliente en la base de datos
#     form = Nueva_factura()                                   # Crea una instancia del formulario de crear factura

#     if form.validate_on_submit():
        
#         factura = Facturas(nif, form.fecha.data, form.precio.data, form.concepto.data, form.metros.data, form.faldas.data, form.importe.data, form.notas.data)
#         db.session.add(factura)
        
#         try:
#             db.session.commit()
#             flash("Factura creada correctamente")
#             return redirect(url_for('clientes'))
#         except Exception as e:
#             print("Error al crear la factura ", e)
#             return redirect(url_for('clientes'))

#     return render_template('nueva_factura.html', form=form, cliente=cliente) #cliente se usa para enviar algunos datos del cliente al formulario de crear factura(nif,nombre, etc)
    

@app.route("/ver_factura/<nif>", methods = ["GET","POST"]) # Ruta para la pagina de ver factura
def ver_factura(nif):
    factura = Facturas.query.filter_by(nif=nif).first()
    cliente = Clientes.query.filter_by(nif=nif).first()
    return render_template('ver_factura.html', factura=factura, cliente=cliente)



@app.route("/facturas/crear/<nif>", methods = ["GET","POST"]) # Ruta para la pagina de crear factura
def crear_factura(nif):
    print(nif)

    fecha = time.strftime("%d/%m/%y")     # Obtiene la fecha actual y la guarda en la variable fecha que se le pasa al template para que se muestre en el formulario
    form = Nueva_factura()                # Crea una instancia del formulario de crear factura
    cliente = Clientes.query.filter_by(nif=nif).first()

    num = Facturas.query.count()          # Cuenta el numero de facturas que hay en la base de datos para poner el numero de factura correcto en el formulario
    num = num + 1  
    
    if form.validate_on_submit():
                           # Aumenta el numero de factura en 1    
        factura = Facturas( cliente.nif, time.strftime("%d/%m/%y"),
                            form.precio1.data,
                            form.precio2.data,
                            form.precio3.data,
                            form.precio4.data,
                            form.precio5.data,
                            form.precio6.data,
                            form.precio7.data,
                            form.precio8.data,

                            form.descripcion1.data,
                            form.descripcion2.data,
                            form.descripcion3.data,
                            form.descripcion4.data,
                            form.descripcion5.data,
                            form.descripcion6.data,
                            form.descripcion7.data,
                            form.descripcion8.data,

                            form.metros1.data,
                            form.metros2.data,
                            form.metros3.data,
                            form.metros4.data,
                            form.metros5.data,
                            form.metros6.data,
                            form.metros7.data,
                            form.metros8.data,

                            form.faldas1.data,
                            form.faldas2.data,
                            form.faldas3.data,
                            form.faldas4.data,
                            form.faldas5.data,
                            form.faldas6.data,
                            form.faldas7.data,
                            form.faldas8.data,

                            form.importe1.data,
                            form.importe2.data,
                            form.importe3.data,
                            form.importe4.data,
                            form.importe5.data,
                            form.importe6.data,
                            form.importe7.data,
                            form.importe8.data,

                            False,
                            form.sub_total_sin_iva.data,
                            form.total_con_iva.data,
                            cliente.precio_metro,
                            notas = "")                    

         
        db.session.add(factura)
        try:
            db.session.commit()
            flash("Factura creada correctamente")
            return redirect(url_for('clientes'))
        except Exception as e:
            print("Error al crear la factura ", e)
            return redirect(url_for('clientes'))
    
    return render_template('crear_factura.html', form = form, cliente = cliente,fecha=fecha,num=num)

if __name__ == '__main__':
    app.run(debug=True)
    
