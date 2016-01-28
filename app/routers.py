from app import app 
"""Monirivinen kommentti: Ensimmäinen app viittaa app -kansioon 
    ja toinen __init__.py -tiedostossa määritettyyn app -nimeen"""
#Yksirivinen kommentti: importilla voi tuoda toisessa tiedostossa määritettyjä moduuleja

#render_template gives you access to Jinja2 template engine
#request -objektilla saadaan requestin käsittely routeille
#make_response -objektilla voidaan lisätä 'header' -tietojen käsittely pyynnöille
from flask import render_template,request,make_response
from app.forms import loginForm

@app.route('/',methods=['GET','POST'])
def index():
    login = loginForm()
    return render_template('template_index.html',form=login)

    #name = 'Jussi'
    #address = 'Jokukatu 1'
    #response = make_response(render_template('template_index.html',name=name,title=address))
    #response.headers.add('Cache-Control','no-cache')
    #return response
    #return render_template('template_index.html',title=address,name=name)
    #return 'Hello World'
    
@app.route('/user/<username>')
def user(username):
    print(request.headers.get('User-Agent'))
    print(request.headers.get('Accept-Language'))
    print(request.headers.get('Accept-Encoding'))
    return render_template('template_user.html',name=username)

#Example how you can define route methods
#Tälle routelle voidaan lähettää dataa GET ja POST -metodeilla. GET on default, jos ei ole määritetty.
@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')   #luetaan /user -kontekstiin tulevasta pyynnöstä attribuutti 'name'
    return render_template('template_user.html',name=name)