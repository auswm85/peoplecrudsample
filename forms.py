from wtforms import Form, StringField, DateTimeField, validators

class PersonForm(Form):
    firstname = StringField(u'First Name', [validators.InputRequired()])
    lastname = StringField(u'Last Name', [validators.InputRequired()])
    birthday = DateTimeField(u'Birthday', [validators.InputRequired()], format='%m/%d/%Y')
    zipcode = StringField(u'Zip Code', [validators.InputRequired(), 
      validators.Regexp(regex='\d{5}(?:-\d{4})?$', message='Invalid US zip code.')])
