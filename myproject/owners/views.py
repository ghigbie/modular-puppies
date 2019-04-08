from flask import Blueprint, render_template, redirect, url_for
<<<<<<< HEAD
from myproject import db
from myproject.models import Owner
from myproject.owners.froms import AddForm

owners_blueprint = Blueprint('owners', __name__, template_folder='templates/owners')

@owners_blueprint.route('/add', methos=['GET', 'POST'])
def add():
    form = AddForm
=======
from myproject import db 
from myproject.models import Owner 
from myproject.owners.forms import AddForm

owners_bluprint = Blueprint('owners', __name__, template_folder, templates=owners)

@owners_blueprint.route('/add', mehtods=['GET', 'POST'])
def add():
    form = AddForm()
>>>>>>> 7065eb3a8961dbc10b821b79b8f36ade66f13785
    if form.valid_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        new_owner = Owner(name, pup_id)
<<<<<<< HEAD
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('add_owner.html', form=form)
=======
        db.sesion.add(new_owner)
        db.sesion.commit()

        return redirect(url_for('puppies.list'))
    return render_template('add_owner.html', form=form)
>>>>>>> 7065eb3a8961dbc10b821b79b8f36ade66f13785
