# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()
import datetime

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []

## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.janrain_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)

## UNIDADES DE CAPACIDADES DE LOS CONDENSADORES ##
db.define_table('Capacidades',
		Field('medida_capacidad','string',label="Unidad"),
		format='%(medida_capacidad)s'
		)

## COLORES DE LAS BANDAS DE LAS RESISTENCIAS ##
db.define_table('Colores_Resistencia',
		Field('Color_Banda','string',label="Color"),
		Field('Valor','integer',label="Valor"),
		format='%(Valor)s - %(Color_Banda)s'
		)

db.define_table('Medidas_Resistencia',
		Field('unidad','string',label="Unidad"),
		format='%(unidad)s'
		)
		
db.define_table('Tolerancia',
		Field('Valor_Tol','string',label="Unidad"),
		format='%(Valor_Tol)s'
		)
		
db.define_table('Potencia_Disipada',
		Field('Valor_Potencia','string',label="Unidad"),
		format='%(Valor_Potencia)s'
		)
		
db.define_table('N_Patillas',
		Field('Numero_Patillas','integer',label="Unidad"),
		format='%(Numero_Patillas)s'
		)
		
db.define_table('Medida_Frecuencia',
		Field('Medida','string',label="Unidad"),
		format='%(Medida)s'
		)
		
db.define_table('Medida_Inductancia',
		Field('Medida','string',label="Unidad"),
		format='%(Medida)s'
		)
		

db.define_table('Ceramicos',
        Field('descripcion','string',label="Descripción",notnull=True),
        Field('capacidad','string',label="Capacidad",notnull=True),
        Field('medida', db.Capacidades,notnull=True),
        Field('tension','integer',label="Tensión Maxima (V)"),
        Field('cantidad','integer',label="Cantidad",notnull=True),        
        )
db.Ceramicos.id.readable=False

db.define_table('Plastico',
        Field('descripcion','string',label="Descripción",notnull=True),
        Field('capacidad','string',label="Capacidad",notnull=True),
        Field('medida', db.Capacidades,notnull=True),
        Field('tension','integer',label="Tensión Maxima (V)"),
        Field('cantidad','integer',label="Cantidad",notnull=True),        
        )
db.Plastico.id.readable=False

db.define_table('Lenteja',
        Field('descripcion','string',label="Descripción",notnull=True),
        Field('capacidad','string',label="Capacidad",notnull=True),
        Field('medida', db.Capacidades,notnull=True),
        Field('tension','integer',label="Tensión Maxima (V)"),
        Field('cantidad','integer',label="Cantidad",notnull=True),        
        )
db.Lenteja.id.readable=False

db.define_table('Electrolitico',
        Field('capacidad','string',label="Capacidad",notnull=True),
        Field('medida', db.Capacidades,notnull=True),
        Field('tension','integer',label="Tensión Maxima (V)"),
        Field('cantidad','integer',label="Cantidad",notnull=True),        
        )
db.Electrolitico.id.readable=False

db.define_table('Resistencia',
		Field('valor','string',label="Valor",notnull=True),
		Field('medida_resistencia',db.Medidas_Resistencia,notnull=True),
        Field('banda_1',db.Colores_Resistencia,notnull=True),
        Field('banda_2',db.Colores_Resistencia,notnull=True),
        Field('banda_3',db.Colores_Resistencia,notnull=True),
        Field('tolerancia',db.Tolerancia,notnull=True),
        Field('Potencia',db.Potencia_Disipada,notnull=True),
        Field('cantidad','integer',label="Cantidad",notnull=True),        
        )
db.Resistencia.id.readable=False

db.define_table('Potenciometro',
		Field('descripcion','string',label="Descripción",notnull=True),
		Field('valor','string',label="Valor",notnull=True),
		Field('medida_resistencia',db.Medidas_Resistencia,notnull=True),
        Field('cantidad','integer',label="Cantidad",notnull=True),        
        )
db.Potenciometro.id.readable=False

db.define_table('Trimmer',
		Field('descripcion','string',label="Descripción",notnull=True),
		Field('valor','string',label="Valor",notnull=True),
		Field('medida_resistencia',db.Medidas_Resistencia,notnull=True),
        Field('cantidad','integer',label="Cantidad",notnull=True),        
        )
db.Trimmer.id.readable=False

db.define_table('Transistor',
		Field('descripcion','string',label="Descripción",notnull=True),
        Field('datasheet','upload',label="Datasheet",notnull=False),
        Field('cantidad','integer',label="Cantidad",notnull=True),         
        )
db.Transistor.id.readable=False

db.define_table('C_Integrado',
		Field('descripcion','string',label="Descripción",notnull=True),
		Field('numero_patillas',db.N_Patillas,notnull=False),
        Field('datasheet','upload',label="Datasheet",notnull=False),
        Field('cantidad','integer',label="Cantidad",notnull=True),         
        )
db.C_Integrado.id.readable=False

db.define_table('Cristal',
		Field('descripcion','string',label="Descripción",notnull=True),
        Field('frecuencia','string',label="Frecuencia",notnull=True),
        Field('unidad_frecuencia',db.Medida_Frecuencia,notnull=True),
        Field('cantidad','integer',label="Cantidad",notnull=True),         
        )
db.Cristal.id.readable=False

db.define_table('Rectificador',
		Field('descripcion','string',label="Descripción",notnull=True),
        Field('datasheet','upload',label="Datasheet",notnull=False),
        Field('cantidad','integer',label="Cantidad",notnull=True),         
        )
db.Rectificador.id.readable=False

db.define_table('Zener',
		Field('descripcion','string',label="Descripción",notnull=True),
        Field('datasheet','upload',label="Datasheet",notnull=False),
        Field('cantidad','integer',label="Cantidad",notnull=True),         
        )
db.Zener.id.readable=False

db.define_table('Puente',
		Field('descripcion','string',label="Descripción",notnull=True),
        Field('datasheet','upload',label="Datasheet",notnull=False),
        Field('cantidad','integer',label="Cantidad",notnull=True),         
        )
db.Puente.id.readable=False

db.define_table('Bobinas',
		Field('descripcion','string',label="Descripción"),
        Field('inductancia','integer',label="Inductancia"),
        Field('unidad_inductancia',db.Medida_Inductancia),
        Field('cantidad','integer',label="Cantidad"),         
        )
db.Bobinas.id.readable=False

db.define_table('Triac',
		Field('descripcion','string',label="Descripción",notnull=True),
        Field('datasheet','upload',label="Datasheet",notnull=True),
        Field('cantidad','integer',label="Cantidad",notnull=True),         
        )
db.Triac.id.readable=False

db.define_table('Diac',
		Field('descripcion','string',label="Descripción",notnull=True),
        Field('datasheet','upload',label="Datasheet",notnull=True),
        Field('cantidad','integer',label="Cantidad",notnull=True),         
        )
db.Diac.id.readable=False

db.define_table('Fusible',
        Field('Corriente','string',label="Corriente Max A",notnull=True),
        Field('Tension','string',label="Tension Max V",notnull=True),  
        Field('cantidad','integer',label="Cantidad",notnull=True),       
        )
db.Fusible.id.readable=False

