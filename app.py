from flask import Flask, render_template, request
from models import Person
from forms import PersonForm

app = Flask(__name__)
app.debug = True

@app.route("/", methods=['GET', 'POST'])
def index():
	form = PersonForm(request.form)
	people = Person.select()

	if request.method == 'POST' and form.validate():
		person  = Person.create(
							firstname=form.firstname.data, 
							lastname=form.lastname.data, 
							birthday=form.birthday.data,
							zipcode=form.zipcode.data)
		return redirect('/')

	return render_template('index.html', form=form, people=people)

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
	person = Person.get(Person.id == id)
	form = PersonForm(request.form, person)

	if request.method == "POST" and form.validate():
		user.firstname = form.firstname.data
		user.lastname = form.lastname.data
		user.birthday = form.birthday.data
		user.zipcode = form.zipcode.data
		user.save()

	return render_template('edit.html', form=form)

if __name__ == "__main__":
	app.run()