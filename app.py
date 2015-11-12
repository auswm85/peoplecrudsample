from flask import Flask, render_template, request, redirect
from models import Person
from forms import PersonForm

app = Flask(__name__)
app.debug = True

@app.route("/", methods=['GET', 'POST'])
def index():
	people = Person.select()

	return render_template('index.html', people=people)

@app.route("/new", methods=['GET', 'POST'])
def create():
	form = PersonForm(request.form)

	if request.method == 'POST' and form.validate():
		person  = Person.create(
							firstname=form.firstname.data, 
							lastname=form.lastname.data, 
							birthday=form.birthday.data,
							zipcode=form.zipcode.data)
		
		return redirect('/')

	return render_template('create.html', form=form)

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
	person = Person.get(Person.id == id)
	form = PersonForm(request.form, person)

	if request.method == "POST" and form.validate():
		person.firstname = form.firstname.data
		person.lastname = form.lastname.data
		person.birthday = form.birthday.data
		person.zipcode = form.zipcode.data
		person.save()

		return redirect('/')

	return render_template('edit.html', form=form, person=person)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
	person = Person.get(Person.id == id)

	if request.method == 'POST':
		person.delete_instance()
		return redirect('/')

	return render_template('delete.html', person=person)

if __name__ == "__main__":
	app.run()