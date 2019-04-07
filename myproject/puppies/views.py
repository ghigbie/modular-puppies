from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.puppies.forms import AddForm, DelForm
from myproject.models import Puppy

puppies_blueprint = Blueprint('puppies', __name__, template_folder='templates/puppies')


def list():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

def delete():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.sesion.commit()

        return redirect(url_for('puppies.list'))
    return render_template('delete.html', form=form)