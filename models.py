from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Date, DateTime, Integer, String, Column, ForeignKey, func, cast, Float

db = SQLAlchemy()

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

    def __init__(self, nif, nombre, telefono, teledono_movil, email, direccion, ciudad, provincia, cp, precio_metro, notas):
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
    
