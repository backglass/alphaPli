from datetime import datetime
import time
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Date, DateTime, Integer, String, Column, ForeignKey, func
from wtforms import Form, StringField, TextAreaField, BooleanField, validators
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

# Clase para crear formulario facturas 
class Nueva_factura(FlaskForm):
    numero = StringField("Número")
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

    pagada = BooleanField(default=False)
    precio_metro = StringField("Precio Metro")        # Estos campos tienen un nombre un poco confuso para mí.
    sub_total_sin_iva  = StringField("Subtotal")      # Estos campos tienen un nombre un poco confuso para mí.
    total_con_iva = StringField("Total")              # Estos campos tienen un nombre un poco confuso para mí.
    notas = TextAreaField("Notas")


# Clase cliente hereda de db.Model, servira para crear la tabla en la base de datos y usar sus datos
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
    importe8 = db.Column(db.String(10))

    pagada = db.Column(db.Boolean)
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




db.create_all()  # Crea la tabla en la base de datos



@app.route('/')  # Ruta raiz
def index():
    return render_template('index.html')



@app.route('/clientes')  # Ruta para la pagina de lista de clientes 
def clientes():
    clientes = Clientes.query.order_by(Clientes.nombre.asc()).all() # Muestra todos los clientes en la base de datos por orden alfabetico.
    return render_template('clientes.html', clientes=clientes) 



@app.route('/clientes/ver/<ver_cliente>',methods=["GET", "POST"]) # Ruta para la pagina de ver un cliente es dinamica porque se le pasa el nif del cliente 
def ver_cliente(ver_cliente):
    cliente = Clientes.query.filter_by(nif=ver_cliente).first() # Busca el cliente en la base de datos
    factura = Facturas.query.filter_by(nif=ver_cliente).order_by(Facturas.num.desc()).all() # Busca las facturas del cliente(su nif) y las ordena de mayor a menor
    numero_facturas = Facturas.query.filter_by(nif = ver_cliente).count()

    # for i in factura_ordenada:
    #     print(i.num)

     #num  = db.session.query(func.max(Facturas.num)).scalar() 
    #factura_totales = Facturas.query.filter_by(nif=ver_cliente).filter_by(pagada=False).all() # Busca las facturas del cliente en la base de datos
    
    ### Calcula el total de las facturas pagadas y el de las no pagadas, para mostrarlo en la pagina de ver_cliente
    iva_total_pagada = 0
    suma_pagada = 0
    suma_no_pagada = 0
    for i in factura:
        if i.pagada == False:
            suma_no_pagada = suma_no_pagada + float(i.total)
        else:
            suma_pagada = suma_pagada + float(i.total)
    iva_total_pagada = round(suma_pagada- suma_pagada / 1.21,2)
    suma_pagada = round(suma_pagada,2)
    suma_no_pagada = round(suma_no_pagada,2)
    ## Formulario que se usara para cambiar el valor de factura es un swith para cambiar el valor de la factura ture false
    form_estado = Nueva_factura()
    if form_estado.validate_on_submit():
        
        num = form_estado.numero.data
        pagada = form_estado.pagada.data
        print(pagada)
        nueva_factura = Facturas.query.filter_by(num=num).first()
        nueva_factura.pagada = pagada
        try:
            db.session.commit()
            if pagada == True:
                flash('Factura pagada','info')
            if pagada == False:
                flash('Factura no pagada',"danger")
        
            return redirect(url_for('ver_cliente', ver_cliente=ver_cliente))
        except Exception as e:
            flash('Error al actualizar la factura','danger')
            return redirect(url_for('ver_cliente', ver_cliente=ver_cliente))
        

        db.session.commit()
        return redirect(url_for('ver_cliente', ver_cliente=ver_cliente))
    return render_template('ver_cliente.html',cliente=cliente, facturas=factura, form_estado = form_estado,suma_no_pagada=suma_no_pagada,suma_pagada=suma_pagada,iva_total_pagada=iva_total_pagada,numero_facturas=numero_facturas) # Devuelve la variable cliente con los datos del nif pasado por parametro



@app.route("/clientes/crear", methods=["GET", "POST"]) # Ruta para la pagina de crear cliente 
def crear_cliente():
    
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
    
    cliente = Clientes.query.filter_by(nif=nif).first()   # Busca el cliente en la base de datos con el nif que se le pasa por la ruta
    db.session.delete(cliente)
    db.session.commit()
    flash("Cliente eliminado correctamente")
    return redirect(url_for('clientes'))


@app.route("/facturas") # Ruta para ver la lista de todas las facturas
def facturas():

    cliente = Facturas.query.all() # Busca todos los clientes en la base de datos
      # Busca todas las facturas de los clientes en la base de datos
    factura = Facturas.query.all()
    for p in factura:
        print(p.num,p.cliente.nombre) ### Esto es importante!!!!!!! porque p.cliente.nombre es el nombre del cliente el cual es el nif en la tabla facturas
    # facturas1=Facturas.query.all()# Busca todas las facturas en la base de datos
    # print (facturas1[1].nif)
    return render_template('facturas.html', facturas = Facturas.query.all()) # Muestra todas las facturas en la base de datos


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
    

# @app.route("/ver_factura/<nif>", methods = ["GET","POST"]) # Ruta para la pagina de ver factura
# def ver_factura(nif):
#     factura = Facturas.query.filter_by(nif=nif).first()
#     cliente = Clientes.query.filter_by(nif=nif).first()
    
#     return render_template('ver_factura.html', factura=factura, cliente=cliente)



@app.route("/facturas/crear/<nif>", methods = ["GET","POST"]) # Ruta para la pagina de crear factura
def crear_factura(nif):
    print(nif)

    fecha = time.strftime("%d/%m/%y")     # Obtiene la fecha actual y la guarda en la variable fecha que se le pasa al template para que se muestre en el formulario
    form = Nueva_factura()                # Crea una instancia del formulario de crear factura
    cliente = Clientes.query.filter_by(nif=nif).first()
    try:
        num  = db.session.query(func.max(Facturas.num)).scalar()       # Cuenta el numero de facturas que hay en la base de datos para poner el numero de factura correcto en el formulario
       # Obtiene el numero de factura que hay en la base de datos y le suma 1 para que sea el numero de factura correcto
        numero = num + 1
    except Exception as e:
        numero = num = 1
    if form.validate_on_submit():
        now = datetime.now()  ## Obtiene la fecha actual para que me funciones en heroku postgresql              
        factura = Facturas( cliente.nif,now,
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
                            form.notas.data)                  

         
        db.session.add(factura)
        try:
            db.session.commit()
            flash("Factura creada correctamente","success")
            return redirect(url_for('ver_cliente', ver_cliente=nif))
            
        except Exception as e:
            print("Error al crear la factura ", e)
            return redirect(url_for('clientes'))
    
    return render_template('crear_factura.html', form = form, cliente = cliente,fecha=fecha,numero=numero)


@app.route("/facturas/editar/<num>", methods=["GET", "POST"]) # Ruta para la pagina de editar factura
def editar_factura(num):

   
    ##cliente = Clientes.query.filter_by(nif=nif).first() # Busca el cliente en la base de datos con el nif que se le pasa en la ruta
    factura = Facturas.query.filter_by(num=num).first()
    cliente = Clientes.query.filter_by(nif=factura.nif).first()
    form = Nueva_factura()                           # Crea una instancia del formulario de cr


  


    if form.validate_on_submit():

        factura.precio1 = form.precio1.data
        factura.precio2 = form.precio2.data
        factura.precio3 = form.precio3.data
        factura.precio4 = form.precio4.data
        factura.precio5 = form.precio5.data
        factura.precio6 = form.precio6.data
        factura.precio7 = form.precio7.data
        factura.precio8 = form.precio8.data

        factura.descripcion1 = form.descripcion1.data
        factura.descripcion2 = form.descripcion2.data
        factura.descripcion3 = form.descripcion3.data
        factura.descripcion4 = form.descripcion4.data
        factura.descripcion5 = form.descripcion5.data
        factura.descripcion6 = form.descripcion6.data
        factura.descripcion7 = form.descripcion7.data
        factura.descripcion8 = form.descripcion8.data

        factura.metros1 = form.metros1.data
        factura.metros2 = form.metros2.data
        factura.metros3 = form.metros3.data
        factura.metros4 = form.metros4.data
        factura.metros5 = form.metros5.data
        factura.metros6 = form.metros6.data
        factura.metros7 = form.metros7.data
        factura.metros8 = form.metros8.data

        factura.faldas1 = form.faldas1.data
        factura.faldas2 = form.faldas2.data
        factura.faldas3 = form.faldas3.data
        factura.faldas4 = form.faldas4.data
        factura.faldas5 = form.faldas5.data
        factura.faldas6 = form.faldas6.data
        factura.faldas7 = form.faldas7.data
        factura.faldas8 = form.faldas8.data

        factura.importe1 = form.importe1.data
        factura.importe2 = form.importe2.data
        factura.importe3 = form.importe3.data
        factura.importe4 = form.importe4.data
        factura.importe5 = form.importe5.data
        factura.importe6 = form.importe6.data
        factura.importe7 = form.importe7.data
        factura.importe8 = form.importe8.data

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
    ##cliente = Clientes.query.filter_by(nif=nif).first() # Busca el cliente en la base de datos con el nif que se le pasa en la ruta
    factura = Facturas.query.filter_by(num=num).first()
    cliente = Clientes.query.filter_by(nif=factura.nif).first()
    form = Nueva_factura()                           # Crea una instancia del formulario de cr


 
    if form.validate_on_submit():

        factura.precio1 = form.precio1.data
        factura.precio2 = form.precio2.data
        factura.precio3 = form.precio3.data
        factura.precio4 = form.precio4.data
        factura.precio5 = form.precio5.data
        factura.precio6 = form.precio6.data
        factura.precio7 = form.precio7.data
        factura.precio8 = form.precio8.data

        factura.descripcion1 = form.descripcion1.data
        factura.descripcion2 = form.descripcion2.data
        factura.descripcion3 = form.descripcion3.data
        factura.descripcion4 = form.descripcion4.data
        factura.descripcion5 = form.descripcion5.data
        factura.descripcion6 = form.descripcion6.data
        factura.descripcion7 = form.descripcion7.data
        factura.descripcion8 = form.descripcion8.data

        factura.metros1 = form.metros1.data
        factura.metros2 = form.metros2.data
        factura.metros3 = form.metros3.data
        factura.metros4 = form.metros4.data
        factura.metros5 = form.metros5.data
        factura.metros6 = form.metros6.data
        factura.metros7 = form.metros7.data
        factura.metros8 = form.metros8.data

        factura.faldas1 = form.faldas1.data
        factura.faldas2 = form.faldas2.data
        factura.faldas3 = form.faldas3.data
        factura.faldas4 = form.faldas4.data
        factura.faldas5 = form.faldas5.data
        factura.faldas6 = form.faldas6.data
        factura.faldas7 = form.faldas7.data
        factura.faldas8 = form.faldas8.data

        factura.importe1 = form.importe1.data
        factura.importe2 = form.importe2.data
        factura.importe3 = form.importe3.data
        factura.importe4 = form.importe4.data
        factura.importe5 = form.importe5.data
        factura.importe6 = form.importe6.data
        factura.importe7 = form.importe7.data
        factura.importe8 = form.importe8.data

        factura.subtotal = form.sub_total_sin_iva.data
        factura.total = form.total_con_iva.data
        factura.precio_metro = cliente.precio_metro
        factura.notas = form.notas.data

        
        
        try:
            db.session.commit()
            flash("Factura Imprimida correctamente","info")
            return redirect(url_for('ver_factura',num=factura.num)) # Crea la url dinamicamente para redirigir a la pagina de ver cliente con su nif
        except Exception as e:
            flash("Error al imprimir la factura", "danger")
            return redirect(url_for('ver_factura',num=factura.num))   # Redirige a la pagina de ver cliente con el nif que se le pasa en la ruta
        

    return render_template('ver_factura.html', form = form,factura=factura,cliente = cliente)

if __name__ == '__main__':
   #app.run()
   app.run(debug=True)
    
