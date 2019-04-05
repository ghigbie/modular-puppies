from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.froms import AddForm

owners_blueprint = Blueprint('owners', __name__, template_folder='templates/owners')

def add():

    from = AddForm

    if form.validate_on_submit():
        name = form.name.data