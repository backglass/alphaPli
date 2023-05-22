
from wtforms import Form, StringField, TextAreaField, BooleanField, validators,IntegerField,ValidationError,SelectField,SubmitField
from flask_wtf import FlaskForm

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
    
    
class Listado_facturas(FlaskForm):
    selection = SelectField('Ordenar por', choices=[('numero_factura', 'Numero factura'),("fecha","Fecha"), ('importe', 'Importe')], default = "Numero factura")
    submit = SubmitField('Buscar')        

#Formulario para crear login
class Login(FlaskForm):
    nombre = StringField("Nombre",validators=[validators.DataRequired()])
    password = StringField("Password",validators=[validators.DataRequired()])
