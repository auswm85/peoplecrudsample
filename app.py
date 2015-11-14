from flask import Flask, render_template, request, redirect, jsonify, url_for
from models import Person
from forms import PersonForm

app = Flask(__name__)
app.debug = True

@app.route("/", methods=['GET', 'POST'], endpoint="index")
def index():
	people = Person.select()
	form = PersonForm()

	return render_template('index.html', people=people, form=form)

@app.route("/new", methods=['GET', 'POST'], endpoint="create")
def create():
	form = PersonForm(request.form)

	if request.method == 'POST' and form.validate():
		person  = Person.create(
							firstname=form.firstname.data, 
							lastname=form.lastname.data, 
							birthday=form.birthday.data,
							zipcode=form.zipcode.data)
		
		if request.is_xhr:
			return jsonify(success=True, person=person.serialize())
		else:
			return redirect(url_for('index'))

	# if it's an ajax request and if fails form validation return message to client
	if request.is_xhr and request.method == 'POST' and not form.validate():
		return jsonify(success=False, errors=form.errors)

	return render_template('create.html', form=form)

@app.route("/edit/<int:id>", methods=['GET', 'POST'], endpoint="edit")
def edit(id):
	person = Person.get(Person.id == id)
	form = PersonForm(request.form, person)

	if request.method == "POST" and form.validate():
		person.firstname = form.firstname.data
		person.lastname = form.lastname.data
		person.birthday = form.birthday.data
		person.zipcode = form.zipcode.data
		person.save()

		return redirect(url_for('index'))

	return render_template('edit.html', form=form, person=person)

@app.route('/delete/<int:id>', methods=['GET', 'POST'], endpoint="delete")
def delete(id):
	person = Person.get(Person.id == id)

	if request.method == 'POST':
		person.delete_instance()

		if request.is_xhr:
			return jsonify(success=True, person=person.serialize())
		else:
			return redirect(url_for('index'))

	return render_template('delete.html', person=person)

if __name__ == "__main__":
	Person.create_table(fail_silently=True)
	app.run()