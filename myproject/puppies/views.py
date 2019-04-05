from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import AddForm, DelForm

puppies_blueprint = Blueprint('puppies', __name__, template_folder='templates/puppies')

def add():
    form = AddForm
    if form.valid_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('add.html', form=form)

def list():
    