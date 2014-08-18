"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators
from wtforms.ext.appengine.ndb import model_form

from .models import ExampleModel


class ClassicExampleForm(wtf.Form):
    example_name = wtf.TextField('Name', validators=[validators.Required()])
    example_description = wtf.TextAreaField('Description', validators=[validators.Required()])

# App Engine ndb model form example
ExampleForm = model_form(ExampleModel, wtf.Form, field_args={
    'example_name': dict(validators=[validators.Required()]),
    'example_description': dict(validators=[validators.Required()]),
})

class NewDialogForm(wtf.Form):
    cmb_map = wtf.SelectField('Map:',
                              choices = [('Map one', 'Map one'), ('Map two', 'Map two'), ('Map three', ' Map three')],
                              validators=[validators.Required()])

    cmb_unit = wtf.SelectField('Unit:',
                               choices = [('Unit one', 'Unit one'), ('Unit two', 'Unit two'), ('Unit three', ' Unit three')],
                               validators=[validators.Required()])

    text_description = wtf.TextAreaField('Description:', validators=[validators.Required()])

class QuickListForm(wtf.Form):
    cmb_map = wtf.SelectField('Map:',
                              choices = [])

    text_description = wtf.TextField('Select map:')
