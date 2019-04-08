from flask import Blueprint, render_template, redirect, url_for
from myproject import db
<<<<<<< HEAD
from myproject.models import Puppy
from myproject.puppies.forms import AddForm, DelForm
=======
from myproject.puppies.forms import AddForm, DelForm
from myproject.models import Puppy
>>>>>>> 7065eb3a8961dbc10b821b79b8f36ade66f13785

puppies_blueprint = Blueprint('puppies', __name__, template_folder='templates/puppies')

@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def add():
<<<<<<< HEAD
    form = AddForm
    if form.valid_on_submit():
=======
    form = AddForm()

    if form.validate_on_submit():
>>>>>>> 7065eb3a8961dbc10b821b79b8f36ade66f13785
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('puppies.list'))
<<<<<<< HEAD
=======

>>>>>>> 7065eb3a8961dbc10b821b79b8f36ade66f13785
    return render_template('add.html', form=form)

@puppies_blueprint.route('/list')
def list():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@puppies_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DelForm()
<<<<<<< HEAD
=======

>>>>>>> 7065eb3a8961dbc10b821b79b8f36ade66f13785
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
<<<<<<< HEAD
        db.session.commit()
        return redirect(url_for('puupies.list'))
    return render_template('delete.html', form=form)
=======
        db.sesion.commit()

        return redirect(url_for('puppies.list'))
    return render_template('delete.html', form=form)
>>>>>>> 7065eb3a8961dbc10b821b79b8f36ade66f13785
