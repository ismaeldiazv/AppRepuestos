# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
                  _class="brand",_href="http://www.web2py.com/")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    ('Inicio', False, URL('default','index'), []),
    ('Condensadores', False, URL(), 
    [
       ('Ceramicos', False, URL('Condensadores','Ceramicos'), []),
       ('Plastico', False, URL('Condensadores','Plastico'), []),
       ('Lenteja', False, URL('Condensadores','Lenteja'), []),
       ('Electrolíticos', False, URL('Condensadores','Electroliticos'), []),
    ]),
    ('Resistencias', False, URL(), 
    [
		('Fijas', False, URL('Resistencias','Resistencias'), []),
		('Potenciómetros', False, URL('Resistencias','Potenciometros'), []),
		('Trimmers', False, URL('Resistencias','Trimmers'), []),
    ]),
    
    ('Transistores', False, URL('Transistores','Transistores'), []),
    ('C. Integrados', False, URL('C_Integrados','C_Integrados'), []),
    ('Cristales Cuarzo', False, URL('Cristales','Cristales'), []),
    ('Diodos', False, URL(), 
    [
        ('Rectificadores', False, URL('Diodos','Rectificadores'), []),
        ('Puentes Rectificadores', False, URL('Diodos','Puentes'), []),
        ('Zener', False, URL('Diodos','Zeners'), []),
    ]),
    ('Bobinas', False, URL('Bobinas','Bobinas'), []),
    ('Triacs', False, URL('Triacs','Triacs'), []),
    ('Diacs', False, URL('Diacs','Diacs'), []),
    ('Fusibles', False, URL('Fusibles','Fusibles'), []),
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    
   
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
