from . import admin
from flask import request,render_template,url_for,redirect,flash
from flask_login import login_required
from ..utils import requires_roles  
@admin.route('/',methods=['GET','POST'])
@login_required
@requires_roles('admin')
def admin_default():
    return render_template("admin/base.html")
