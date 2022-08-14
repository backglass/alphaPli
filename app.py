from datetime import datetime
import time
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Date, DateTime, Integer, String, Column, ForeignKey, func
from wtforms import Form, StringField, TextAreaField, BooleanField, validators,IntegerField,ValidationError
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
    telefono = StringField("Teléfono", validators=[validators.DataRequired()])
    telefono_movil = StringField("Teléfono Movil")
    email = StringField("Email")
    direccion = StringField("Dirección", validators=[validators.DataRequired()])
    ciudad = StringField("Ciudad")
    provincia = StringField("Provincia")
    cp = StringField("CP")
    precio_metro = StringField("Precio Metro",validators=[validators.DataRequired()])
    notas = TextAreaField("Notas")
    
    def validate_nif(self, nif):
          
        """
        Función para validar el NIF del cliente, usada dentro del la propia clase
        para comporbar si el nif tiene nueve caracteres y si no tiene un punto
        """
        if len(nif.data) != 9:  
            raise validators.ValidationError("El NIF debe tener 9 caracteres")
        if "." in nif.data:
            raise validators.ValidationError("El NIF no puede contener puntos")


# Clase para crear formulario facturas 
class Nueva_factura(FlaskForm):
    
    numero = IntegerField("Número",validators = [validators.DataRequired()])
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
    precio9 = StringField("Precio9")
    precio10 = StringField("Precio10")

    descripcion1 = StringField("Descripcion1")
    descripcion2 = StringField("Descripción2")
    descripcion3 = StringField("Descripción3")
    descripcion4 = StringField("Descripción4")
    descripcion5 = StringField("Descripción5")
    descripcion6 = StringField("Descripción6")
    descripcion7 = StringField("Descripción7")
    descripcion8 = StringField("Descripción8")
    descripcion9 = StringField("Descripción9")
    descripcion10 = StringField("Descripción10")
    
    metros1 = StringField("Metros1")
    metros2 = StringField("Metros2")
    metros3 = StringField("Metros3")
    metros4 = StringField("Metros4")
    metros5 = StringField("Metros5")
    metros6 = StringField("Metros6")
    metros7 = StringField("Metros7")
    metros8 = StringField("Metros8")
    metros9 = StringField("Metros9")
    metros10 = StringField("Metros10")

    faldas1 = StringField("Faldas1")
    faldas2 = StringField("Faldas2")
    faldas3 = StringField("Faldas3")
    faldas4 = StringField("Faldas4")
    faldas5 = StringField("Faldas5")
    faldas6 = StringField("Faldas6")
    faldas7 = StringField("Faldas7")
    faldas8 = StringField("Faldas8")
    faldas9 = StringField("Faldas9")
    faldas10 = StringField("Faldas10")

    importe1 = StringField("Importe1")
    importe2 = StringField("Importe2")
    importe3 = StringField("Importe3")
    importe4 = StringField("Importe4")
    importe5 = StringField("Importe5")
    importe6 = StringField("Importe6")
    importe7 = StringField("Importe7")
    importe8 = StringField("Importe8")
    importe9 = StringField("Importe9")
    importe10 = StringField("Importe10")

    pagada = BooleanField(default=False)
    precio_metro = StringField("Precio Metro")                    # Estos campos tienen un nombre un poco confuso para mí.
    sub_total_sin_iva  = StringField("Subtotal",default="0")      # Se necesita poner el valor en 0, por si al hacer una factura se queda el valor en blanco daria un error..
    total_con_iva = StringField("Total",default="0")              # confuso
    notas = TextAreaField("Notas")

#Formulario para crear login
class Login(FlaskForm):
    nombre = StringField("Nombre",validators=[validators.DataRequired()])
    password = StringField("Password",validators=[validators.DataRequired()])

# Clase cliente hereda de db.Model, servira para crear la tabla en la base de datos y usar sus propiedades
class Clientes(db.Model):

    __tablename__ = "cliente"

    nif = db.Column(db.String(15), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(100))
    teledono_movil = db.Column(db.String(100))
    email = db.Column(db.String(100))
    direccion = db.Column(db.String(100))
    ciudad = db.Column(db.String(100))
    provincia = db.Column(db.String(100))
    cp = db.Column(db.String(10))
    precio_metro = db.Column(db.String(10))
    notas = db.Column(db.String(10000))
    pubs = db.relationship('Facturas', backref='cliente', lazy='dynamic')

    def __init__(self, nif, nombre, telefono, teledono_movil, email, direccion,ciudad,provincia,cp,precio_metro, notas):
        self.nif = nif
        self.nombre = nombre
        self.telefono = telefono
        self.teledono_movil = teledono_movil
        self.email = email
        self.direccion = direccion
        self.ciudad = ciudad
        self.provincia = provincia
        self.cp = cp
        self.direccion = direccion
        self.precio_metro = precio_metro
        self.notas = notas


            
    def __repr__(self):
        return f"Cliente('{self.nif}', '{self.nombre}', '{self.telefono}', '{self.teledono_movil}', '{self.email}', '{self.direccion}','{self.precio_metro} '{self.notas}')"
 


    
class Facturas(db.Model): # Clase Facturas hereda de db.Model, servira para crear la tabla en la base de datos y usar sus propiedades
                          # Esta clase es así por que el usuario no tiene "productos especificos", casi siempre son facturas totalmente independientes de productos.

    __tablename__ = "factura"

    num = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
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
    precio9 = db.Column(db.String(10))
    precio10 = db.Column(db.String(10))
    
    descripcion1 = db.Column(db.String(100))
    descripcion2 = db.Column(db.String(100))
    descripcion3 = db.Column(db.String(100))
    descripcion4 = db.Column(db.String(100))
    descripcion5 = db.Column(db.String(100))
    descripcion6 = db.Column(db.String(100))
    descripcion7 = db.Column(db.String(100))
    descripcion8 = db.Column(db.String(100))
    descripcion9 = db.Column(db.String(100))
    descripcion10 = db.Column(db.String(10000))

    metros1 = db.Column(db.String(10))
    metros2 = db.Column(db.String(10))
    metros3 = db.Column(db.String(10))
    metros4 = db.Column(db.String(10))
    metros5 = db.Column(db.String(10))
    metros6 = db.Column(db.String(10))
    metros7 = db.Column(db.String(10))
    metros8 = db.Column(db.String(10))
    metros9 = db.Column(db.String(10))
    metros10 = db.Column(db.String(10))

    faldas1 = db.Column(db.String(10))
    faldas2 = db.Column(db.String(10))
    faldas3 = db.Column(db.String(10))
    faldas4 = db.Column(db.String(10))
    faldas5 = db.Column(db.String(10))
    faldas6 = db.Column(db.String(10))
    faldas7 = db.Column(db.String(10))
    faldas8 = db.Column(db.String(10))
    faldas9 = db.Column(db.String(10))
    faldas10 = db.Column(db.String(10))

    importe1 = db.Column(db.String(10))
    importe2 = db.Column(db.String(10))
    importe3 = db.Column(db.String(10))
    importe4 = db.Column(db.String(10))
    importe5 = db.Column(db.String(10))
    importe6 = db.Column(db.String(10))
    importe7 = db.Column(db.String(10))
    importe8 = db.Column(db.String(10))
    importe9 = db.Column(db.String(10))
    importe10 = db.Column(db.String(10))

    pagada = db.Column(db.Boolean)
    subtotal  = db.Column(db.String(10))
    total = db.Column(db.String(10))
    precio_metro = db.Column(db.Float())
    notas = db.Column(db.String(1000))

    def __init__(self,numero, nif, fecha,
                 precio1,precio2,precio3,precio4,precio5,precio6,precio7,precio8,precio9,precio10,
                 descripcion1,descripcion2,descripcion3,descripcion4,descripcion5,descripcion6,descripcion7,descripcion8,descripcion9,descripcion10,
                 metros1,metros2,metros3,metros4,metros5,metros6,metros7,metros8,metros9,metros10,
                 faldas1,faldas2,faldas3,faldas4,faldas5,faldas6,faldas7,faldas8,faldas9,faldas10,
                 importe1,importe2,importe3,importe4,importe5,importe6,importe7,importe8,importe9,importe10,
                 pagada,subtotal,total,precio_metro,notas):

        self.numero = numero
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
        self.precio9 = precio9
        self.precio10 = precio10

        self.descripcion1 = descripcion1
        self.descripcion2 = descripcion2
        self.descripcion3 = descripcion3
        self.descripcion4 = descripcion4
        self.descripcion5 = descripcion5
        self.descripcion6 = descripcion6
        self.descripcion7 = descripcion7
        self.descripcion8 = descripcion8
        self.descripcion9 = descripcion9
        self.descripcion10 = descripcion10
        
        self.metros1 = metros1
        self.metros2 = metros2
        self.metros3 = metros3
        self.metros4 = metros4
        self.metros5 = metros5
        self.metros6 = metros6
        self.metros7 = metros7
        self.metros8 = metros8
        self.metros9 = metros9
        self.metros10 = metros10

        self.faldas1 = faldas1
        self.faldas2 = faldas2
        self.faldas3 = faldas3
        self.faldas4 = faldas4
        self.faldas5 = faldas5
        self.faldas6 = faldas6
        self.faldas7 = faldas7
        self.faldas8 = faldas8
        self.faldas9 = faldas9
        self.faldas10 = faldas10

        
        self.importe1 = importe1
        self.importe2 = importe2
        self.importe3 = importe3
        self.importe4 = importe4
        self.importe5 = importe5
        self.importe6 = importe6
        self.importe7 = importe7
        self.importe8 = importe8
        self.importe9 = importe9
        self.importe10 = importe10
        
        self.pagada = pagada
        self.subtotal = subtotal
        self.total = total
        self.precio_metro = precio_metro
        self.notas = notas
    

    def __repr__(self):
        return '<Factura %r>' % self.id
    
#Clase para la tabla de clientes y sus propiedades
class Usuarios(db.Model):

    __tablename__ = "usuario"

    nombre = db.Column(db.String(15), primary_key=True)
    password = db.Column(db.String(100))


    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password
    def __repr__(self):
        return '<Usuario %r>' % self.nombre
    


db.create_all()  # Crea la tabla en la base de datos


@app.route('/',methods = ['POST','GET'])  # Ruta raiz
def index():
    """
    Ruta raiz de la aplicacion. En ella se muestra el formulario de login y el formulario de registro.
    Es una ruta que se encargara de activar la session y redirigir al la rura "clientes"
    """
    form = Login() #Insancia del formulario de login.
    
    # Valida los datos que vienen del formulario "form" y si existe el usuario activa la session y si no lo redirige a la pagina de login(index)
    if form.validate_on_submit():
        
        nombre = form.nombre.data
        password = form.password.data
        print (type(nombre),nombre)
        if nombre == "" or password == "":               # Si el nombre o el password estan vacios redirige a la pagina de login(index)
            return render_template('index.html',error="Introduce un usuario y contraseña",form=form)
       
        try:   ### Por si el usuario introducido no existe en la base de datos, se usará el try para que no explote el programa   
            usuario = Usuarios.query.filter_by(nombre=nombre).first()
            print (usuario.nombre, usuario.password)
        except:
            flash('Usuario no existe','danger')
            print("usuario no existe")

            return render_template('index.html',form=form)

        if usuario.nombre == nombre and usuario.password == password: # Si el usuario existe y el password es correcto activa la session y redirige "a clientes"
            session['username'] = nombre
            print("test")
            return redirect('clientes')
                
        else:                                                         # Si el usuario no existe o el password es incorrecto redirige a la pagina de login(index)
                return render_template('index.html')
    return render_template('index.html',form=form)
    



@app.route('/clientes')  # Ruta para la pagina de lista de clientes 
def clientes():
    
    """
    Esta ruta se encargara de mostrar la lista de todos los clientes de la base de datos.
    Comprueba si la session esta activa y renderiza la web con todos los datos, de la tabla clientes en la base de datos.
    """

    if 'username' not in session:  # Si no existe la session redirige a la pagina de login(index)
        return redirect('/')
    clientes = Clientes.query.order_by(Clientes.nombre.asc()).all() # Muestra todos los clientes en la base de datos por orden alfabetico.
    return render_template('clientes.html',clientes=clientes)
    

@app.route('/clientes/ver/<ver_cliente>',methods=["GET", "POST"]) # Ruta para la pagina de ver un cliente es dinamica porque se le pasa el nif del cliente 
def ver_cliente(ver_cliente):
   
    """
    Aquí se mostrará la información de un cliente en concreto.Sea el nif que entra por parámetro
    También se encargara de calcular los valores del cliente en todas sus facturas, como la suma del iva, la suma
    de las facturas sin pagar y la suma de las facturas pagadas.
    En el html que asocia a esta ruta hay un formulario oculto, que según se pinche en los iconos de pagado o no pagado,cambiara true o false a la columna pagada 
    de la tabla facturas en la BBDD.

    """

    if 'username'not in session:  # Si no existe la session redirige a la pagina de login(index)
        return redirect('/')

    cliente = Clientes.query.filter_by(nif=ver_cliente).first()                                # Busca el cliente en la base de datos
    factura = Facturas.query.filter_by(nif=ver_cliente).order_by(Facturas.numero.desc()).all() # Busca las facturas del cliente(su nif) y las ordena de mayor a menor
    numero_facturas = Facturas.query.filter_by(nif = ver_cliente).count()                      # Cuenta el numero de facturas del cliente, para mostrarlo en el html	
    
    ### Calcula el total de las facturas pagadas y el de las no pagadas, para mostrarlo en la pagina html
    iva_total_pagada = 0
    suma_pagada = 0
    suma_no_pagada = 0

    #Recorre factura y si el valor de la columna pagada es false lo suma el valor de la columna total y lo mete en la variable "suma_no_pagada"
    #Así sabe cuanto ha de pagar el cliente
    #Por el contrario si el valor de la columna pagada es true lo suma el valor de la columna total y lo mete en la variable "suma_pagada"
    # y también calculara el iva de las facturas pagadas y lo mete en la variable "iva_total_pagada"
    for i in factura:
        if i.pagada == False:
         suma_no_pagada = suma_no_pagada + float(i.total)
        else:
            suma_pagada = suma_pagada + float(i.total)
            iva_total_pagada = round(suma_pagada * 0.21,2)
            suma_pagada = round(suma_pagada,2)
            suma_no_pagada = round(suma_no_pagada,2)

    ## Formulario que se usara para cambiar el valor de factura es un swith para cambiar el valor de la factura ture false
    form_estado = Nueva_factura()
    if form_estado.validate_on_submit():
        
        num = form_estado.numero.data    # Recoge el numero de la factura al pinchar en el icono(verde o rojo)
        pagada = form_estado.pagada.data # Recoge el valor de la columna pagada(true o false)
        
        nueva_factura = Facturas.query.filter_by(num=num).first()  # 
        nueva_factura.pagada = pagada #Asigna el valor false o true, que viene de pinchar en el icono.
        try:
            db.session.commit() # Guarda los cambios en la base de datos con el nuevo valor de la columna pagada(true o false)
            #Comprobar el valor "pagada" para mostrar los mensajes flash
            if pagada == True:  
                flash('Factura pagada','info')
            if pagada == False:
                flash('Factura no pagada',"danger")
        
            return redirect(url_for('ver_cliente', ver_cliente=ver_cliente))
        except Exception as e:
            flash('Error al actualizar la factura','danger')
            return redirect(url_for('ver_cliente', ver_cliente=ver_cliente))
        
    return render_template('ver_cliente.html',cliente=cliente, facturas=factura, form_estado = form_estado,suma_no_pagada=suma_no_pagada,suma_pagada=suma_pagada,iva_total_pagada=iva_total_pagada,numero_facturas=numero_facturas) # Devuelve la variable cliente con los datos del nif pasado por parametro



@app.route("/clientes/crear", methods=["GET", "POST"]) # Ruta para la pagina de crear cliente 
def crear_cliente():
    
    """
    Esta ruta se encargara de crear un cliente en la base de datos.
    Se creará una instancia de formulario "Insertar_cliente" que manejará los datos del cliente que vienen del formulario html.
    Creará un objeto de la clase Clientes y lo guardará los datos del formulario en la base de datos.
    """
    
    if 'username'not in session:  # Si no existe la session redirige a la pagina de login(index)
        return redirect('/')

    form = Insertar_cliente()     # Crea el formulario de crear cliente objeto form 
    if form.validate_on_submit(): # Si el formulario es validado
        
        # Crea un nuevo cliente con los datos del formulario 
        cliente = Clientes(form.nif.data, form.nombre.data, form.telefono.data, form.telefono_movil.data, form.email.data, form.direccion.data,form.ciudad.data,form.provincia.data,form.cp.data,form.precio_metro.data, form.notas.data)
        db.session.add(cliente)
        
        try:                                      # Intenta guardar los datos en la base de datos
            db.session.commit()                   # Guarda los datos en la base de datos
            flash("Cliente creado correctamente","info") # Muestra un mensaje de que el cliente se ha creado correctamente
            return redirect(url_for('clientes'))  # Redirige a la pagina de lista de clientes
        
        except:                                   # Si no se puede guardar en la base de datos 
            flash("Error al crear el cliente, parece que el cliente ya existe","danger") # Muestra un mensaje de error
            return redirect(url_for('clientes'))
        
    return render_template('crear_cliente.html',form=form)


@app.route("/clientes/editar/<nif>", methods=["GET", "POST"]) # Ruta para la pagina de editar cliente
def editar_cliente(nif):
    
    """
    Esta ruta sirve para editar los datos de un cliente.
    Se creara una instancia de formulario "Editar_cliente" que manejará los datos del cliente que vienen del formulario html.
    Buscará el cliente con el nif pasado por parametro  y cambiará los datos del cliente con los datos del formulario.
    """
    
    if 'username'not in session:  # Si no existe la session redirige a la pagina de login(index)
        return redirect('/')
   
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
        flash("Cliente editado correctamente","info")
        return redirect(url_for('clientes'))
        
    return render_template('editar_cliente.html', form=form, cliente=cliente) # manda form y cliente a la pagina de editar cliente


@app.route("/clientes/eliminar/<nif>", methods=["GET", "POST"]) # Ruta para la pagina de eliminar cliente
def eliminar_cliente(nif):
    """
    Eliminar cliente de la base de datos.
    """
    if 'username'not in session:  # Si no existe la session redirige a la pagina de login(index)
        return redirect('/')
    
    cliente = Clientes.query.filter_by(nif=nif).first()   # Busca el cliente en la base de datos con el nif que se le pasa por la ruta
    db.session.delete(cliente)
    db.session.commit()
    flash("Cliente eliminado correctamente")
    return redirect(url_for('clientes'))


@app.route("/facturas") # Ruta para ver la lista de todas las facturas
def facturas():
    """
    Esta ruta se encargara de mostrar la lista de todas la facturas de la base de datos.
    """
    
    if 'username'not in session:  # Si no existe la session redirige a la pagina de login(index)
        return redirect('/')

    # Busca todas las facturas de los clientes en la base de datos ordenadas con fecha mas actual
    factura = Facturas.query.order_by(Facturas.numero.desc()).all()

    return render_template('facturas.html', facturas = factura) # Muestra todas las facturas en la base de datos


@app.route("/facturas/crear/<nif>", methods = ["GET","POST"]) # Ruta para la pagina de crear factura
def crear_factura(nif):
    """
    Esta ruta se encargara de crear una factura para un cliente.
    """
    
    if 'username'not in session:  
        return redirect('/')
 
    fecha = time.strftime("%d/%m/%y")     # Obtiene la fecha actual y la guarda en la variable fecha que se le pasa al template para que se muestre en el formulario
    form = Nueva_factura()                # Crea una instancia del formulario de crear factura
    cliente = Clientes.query.filter_by(nif=nif).first() # Busca el cliente en la base de datos con el nif que se le pasa por la ruta
    
    if form.validate_on_submit():

        now = datetime.now()  ## Obtiene la fecha actual para que me funciones en heroku postgresql              
        # Inserta todos los datos de la factura en un registro nuevo de la base de datos. 
        # Todos los datos se obtienen del form.

        factura = Facturas( form.numero.data,cliente.nif,now,
                            form.precio1.data,
                            form.precio2.data,
                            form.precio3.data,
                            form.precio4.data,
                            form.precio5.data,
                            form.precio6.data,
                            form.precio7.data,
                            form.precio8.data,
                            form.precio9.data,
                            form.precio10.data,

                            form.descripcion1.data,
                            form.descripcion2.data,
                            form.descripcion3.data,
                            form.descripcion4.data,
                            form.descripcion5.data,
                            form.descripcion6.data,
                            form.descripcion7.data,
                            form.descripcion8.data,
                            form.descripcion9.data,
                            form.descripcion10.data,

                            form.metros1.data,
                            form.metros2.data,
                            form.metros3.data,
                            form.metros4.data,
                            form.metros5.data,
                            form.metros6.data,
                            form.metros7.data,
                            form.metros8.data,
                            form.metros9.data,
                            form.metros10.data,

                            form.faldas1.data,
                            form.faldas2.data,
                            form.faldas3.data,
                            form.faldas4.data,
                            form.faldas5.data,
                            form.faldas6.data,
                            form.faldas7.data,
                            form.faldas8.data,
                            form.faldas9.data,
                            form.faldas10.data,

                            form.importe1.data,
                            form.importe2.data,
                            form.importe3.data,
                            form.importe4.data,
                            form.importe5.data,
                            form.importe6.data,
                            form.importe7.data,
                            form.importe8.data,
                            form.importe9.data,
                            form.importe10.data,

                            False,
                            form.sub_total_sin_iva.data,
                            form.total_con_iva.data,
                            cliente.precio_metro,
                            form.notas.data)                  

         
        db.session.add(factura)
        try:
            db.session.commit()
            flash("Factura creada correctamente","success")
            return redirect(url_for('ver_cliente', ver_cliente=nif))
            
        except Exception as e:
            print("Error al crear la factura ", e)
            return redirect(url_for('clientes'))
    
    return render_template('crear_factura.html', form = form, cliente = cliente,fecha=fecha)


@app.route("/facturas/editar/<num>", methods=["GET", "POST"]) # Ruta para la pagina de editar factura
def editar_factura(num):
    """
     Ruta para editar una factura., se diferencia de la ruta "crear_factura" porque de inicio recibe los valores de la factura en la base de datos
     El proceso de actualizar una factura con datos nuevos se hace en el mismo que en "crear_factura"
    """

    if 'username'not in session:  
        return redirect('/')
   
    ##cliente = Clientes.query.filter_by(nif=nif).first() # Busca el cliente en la base de datos con el nif que se le pasa en la ruta
    factura = Facturas.query.filter_by(num=num).first()
    cliente = Clientes.query.filter_by(nif=factura.nif).first()
    form = Nueva_factura()                           # Crea una instancia del formulario

    if form.validate_on_submit():
        factura.fecha = form.fecha.data
        factura.numero = form.numero.data
        factura.precio1 = form.precio1.data
        factura.precio2 = form.precio2.data
        factura.precio3 = form.precio3.data
        factura.precio4 = form.precio4.data
        factura.precio5 = form.precio5.data
        factura.precio6 = form.precio6.data
        factura.precio7 = form.precio7.data
        factura.precio8 = form.precio8.data
        factura.precio9 = form.precio9.data
        factura.precio10 = form.precio10.data

        factura.descripcion1 = form.descripcion1.data
        factura.descripcion2 = form.descripcion2.data
        factura.descripcion3 = form.descripcion3.data
        factura.descripcion4 = form.descripcion4.data
        factura.descripcion5 = form.descripcion5.data
        factura.descripcion6 = form.descripcion6.data
        factura.descripcion7 = form.descripcion7.data
        factura.descripcion8 = form.descripcion8.data
        factura.descripcion9 = form.descripcion9.data
        factura.descripcion10 = form.descripcion10.data

        factura.metros1 = form.metros1.data
        factura.metros2 = form.metros2.data
        factura.metros3 = form.metros3.data
        factura.metros4 = form.metros4.data
        factura.metros5 = form.metros5.data
        factura.metros6 = form.metros6.data
        factura.metros7 = form.metros7.data
        factura.metros8 = form.metros8.data
        factura.metros9 = form.metros9.data
        factura.metros10 = form.metros10.data

        factura.faldas1 = form.faldas1.data
        factura.faldas2 = form.faldas2.data
        factura.faldas3 = form.faldas3.data
        factura.faldas4 = form.faldas4.data
        factura.faldas5 = form.faldas5.data
        factura.faldas6 = form.faldas6.data
        factura.faldas7 = form.faldas7.data
        factura.faldas8 = form.faldas8.data
        factura.faldas9 = form.faldas9.data
        factura.faldas10 = form.faldas10.data

        factura.importe1 = form.importe1.data
        factura.importe2 = form.importe2.data
        factura.importe3 = form.importe3.data
        factura.importe4 = form.importe4.data
        factura.importe5 = form.importe5.data
        factura.importe6 = form.importe6.data
        factura.importe7 = form.importe7.data
        factura.importe8 = form.importe8.data
        factura.importe9 = form.importe9.data
        factura.importe10 = form.importe10.data

        factura.subtotal = form.sub_total_sin_iva.data
        factura.total = form.total_con_iva.data
        factura.precio_metro = cliente.precio_metro
        factura.notas = form.notas.data
        
        try:
            db.session.commit()
            flash("Factura actualizada correctamente","success")
            return redirect(url_for('ver_cliente', ver_cliente=factura.nif)) # Crea la url dinamicamente para redirigir a la pagina de ver cliente con su nif

        except Exception as e:
            print("Error al actualizar la factura ", e)
            return redirect(url_for('ver_cliente', ver_cliente=factura.nif))   # Redirige a la pagina de ver cliente con el nif que se le pasa en la ruta
        
    return render_template('editar_factura.html', form = form,factura=factura,cliente = cliente)



@app.route("/facturas/ver/<num>", methods=["GET", "POST"])  
def ver_factura(num):
    """
    Esta ruta es igual a la ruta "editar_factura" 
    El cambio aquí esta mas en el template html, que quita bordes y cositas para que se imprima la factura con un formato decente.
    """

    if 'username'not in session:  # Si no existe la session redirige a la pagina de login(index)
        return redirect('/')

    ##cliente = Clientes.query.filter_by(nif=nif).first() # Busca el cliente en la base de datos con el nif que se le pasa en la ruta
    factura = Facturas.query.filter_by(num=num).first()
    cliente = Clientes.query.filter_by(nif=factura.nif).first()
    form = Nueva_factura()                           # Crea una instancia del formulario 
     
    if form.validate_on_submit():
        factura.numero = form.numero.data
        factura.precio1 = form.precio1.data
        factura.precio2 = form.precio2.data
        factura.precio3 = form.precio3.data
        factura.precio4 = form.precio4.data
        factura.precio5 = form.precio5.data
        factura.precio6 = form.precio6.data
        factura.precio7 = form.precio7.data
        factura.precio8 = form.precio8.data
        factura.precio9 = form.precio9.data
        factura.precio10 = form.precio10.data

        factura.descripcion1 = form.descripcion1.data
        factura.descripcion2 = form.descripcion2.data
        factura.descripcion3 = form.descripcion3.data
        factura.descripcion4 = form.descripcion4.data
        factura.descripcion5 = form.descripcion5.data
        factura.descripcion6 = form.descripcion6.data
        factura.descripcion7 = form.descripcion7.data
        factura.descripcion8 = form.descripcion8.data
        factura.descripcion9 = form.descripcion9.data
        factura.descripcion10 = form.descripcion10.data

        factura.metros1 = form.metros1.data
        factura.metros2 = form.metros2.data
        factura.metros3 = form.metros3.data
        factura.metros4 = form.metros4.data
        factura.metros5 = form.metros5.data
        factura.metros6 = form.metros6.data
        factura.metros7 = form.metros7.data
        factura.metros8 = form.metros8.data
        factura.metros9 = form.metros9.data
        factura.metros10 = form.metros10.data

        factura.faldas1 = form.faldas1.data
        factura.faldas2 = form.faldas2.data
        factura.faldas3 = form.faldas3.data
        factura.faldas4 = form.faldas4.data
        factura.faldas5 = form.faldas5.data
        factura.faldas6 = form.faldas6.data
        factura.faldas7 = form.faldas7.data
        factura.faldas8 = form.faldas8.data
        factura.faldas9 = form.faldas9.data
        factura.faldas10 = form.faldas10.data

        factura.importe1 = form.importe1.data
        factura.importe2 = form.importe2.data
        factura.importe3 = form.importe3.data
        factura.importe4 = form.importe4.data
        factura.importe5 = form.importe5.data
        factura.importe6 = form.importe6.data
        factura.importe7 = form.importe7.data
        factura.importe8 = form.importe8.data
        factura.importe9 = form.importe9.data
        factura.importe10 = form.importe10.data

        factura.subtotal = form.sub_total_sin_iva.data
        factura.total = form.total_con_iva.data
        factura.precio_metro = cliente.precio_metro
        factura.notas = form.notas.data

        return redirect(url_for('ver_factura',num=factura.num)) # Crea la url dinamicamente para redirigir a la pagina de ver cliente con su nif

    return render_template('ver_factura.html', form = form,factura=factura,cliente = cliente)


@app.route("/clientes/etiqueta/<nif>", methods=["GET", "POST"])
def etiqueta(nif):
    """
    Ruta para crear etiquetas de clientes
    se mandan los datos del cliente y el html genera las etiquetas con los datos del cliente
    """    

    if 'username'not in session:  # Si no existe la session redirige a la pagina de login(index)
        return redirect('/')
    cliente = Clientes.query.filter_by(nif=nif).first()
  
    return render_template('etiquetas.html', cliente=cliente)


if __name__ == '__main__':
  # app.run()
   app.run(debug=True)
    
