from . import admin
from  ...models.users import User,Organization,Questions
from flask_admin.contrib.sqla import ModelView
from FMSapp import adminpg,db
from flask import request,render_template,url_for,redirect,flash

#@admin.route('/',methods=['GET','POST'])
#def admin_default():
#    return render_template("admin/base.html")
adminpg.add_view(ModelView(User,db.session))
adminpg.add_view(ModelView(Organization,db.session))
