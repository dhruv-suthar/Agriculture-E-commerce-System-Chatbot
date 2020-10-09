import os , math
import requests
import json
from flask import Flask , render_template ,flash , redirect , url_for , session , request ,logging , abort ,jsonify , make_response , Response
from flask_wtf.file import FileField , FileAllowed , FileRequired 
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import and_ , any_ , or_ , func , extract
from sqlalchemy.exc import IntegrityError
# import flask.ext.whooshalchemy as wa
from functools import wraps
from wtforms import Form , StringField , TextAreaField , PasswordField , validators , SelectField  , ValidationError , RadioField , SelectMultipleField
from wtforms.fields.html5 import IntegerField, TelField ,EmailField
from wtforms.validators import InputRequired
from passlib.hash import sha256_crypt
from flask_mail import Message , Mail
import os.path
from datetime import datetime , timedelta
from werkzeug import secure_filename
import math, random , string
from demo import *
from Payment_Gateway import Checksum
from flaskext.csrf import csrf , csrf_exempt
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
import cv2
import numpy as np



app=Flask(__name__)


app.config.from_pyfile('config.py')




#init sqlalchemy
db=SQLAlchemy(app)
mail = Mail(app)
from views import *
from admin_views import *



if __name__=='__main__':
    app.secret_key='any key'
    app.run(debug = True,host='192.168.43.47',port = 2588, threaded=True)

