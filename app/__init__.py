from flask import Flask

#ext tarkoittaa flaskin laajennusta ja bootstrap on package, josta importoidaan luokka Bootstrap. Vaatii flaskin.
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

#Luodaan Flask -objekti ja sijoitetaan se muuttujaan 'app'. Tätä voi kutsua toisista app-packagen tiedostoista importilla
#__name__ sisältää Python packagen nimen, eli tässä tapauksessa 'app'
app = Flask(__name__)


#This line configures our app using the config.py file
app.config.from_object('config')
bootstrap = Bootstrap(app)
#Annetaan funktiolle app objekti, joka sisältää config.py tiedot
db = SQLAlchemy(app)
from app import routers