from flask import Blueprint


admin=Blueprint('Admin',__name__,url_prefix='/Admin')
from . import views
