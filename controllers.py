"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

import uuid

from py4web import action, request, abort, redirect, URL, Field
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.url_signer import URLSigner

from yatl.helpers import A
from . common import db, session, T, cache, auth, signed_url


url_signer = URLSigner(session)

# The auth.user below forces login.
@action('index')
@action.uses('index.html', db, auth.user, session) #auth.user is the sign in part thatc checks you are a user
def index():
	user_email = auth.current_user.get('email') #sets and gets email, hoping email is not none
	contacts = db(db.contacts.user_email == user_email).select() #return a list with data in it
	return dict(c=contacts, s=url_signer, user=auth.get_user() ) #naming c to be the key

#MAKING A CONTAAAAAAAAAAAAACT
@action('add_contact', method = ['GET' , 'POST'])
@action.uses('add_contact.html', session)
def add_contact():
	form = Form(db.contacts, csrf_session = session, formstyle=FormStyleBulma)
	if form.accepted:
		redirect(URL('index'))
	return dict(form=form, user=auth.get_user())

#THE EDIT BUTTOOOOOOOOOOON
@action('edit_contact/<contactID>', method = ['GET' , 'POST'])
@action.uses('add_contact.html', session, db)
def edit_contact(contactID = None):

	#parameters = request.params # THIS DIDN'T WORK
	#contactID = parameters.get('contact_id', None) # id none, sets record to none. NEED THIS CUZ WE DONT ALWAYS GET A VALUE BACK

	auth_user = auth.current_user
	email = auth_user.get('email')

	form = None

	contacts = db( (db.contacts.user_email == email) & (db.contacts.id == contactID) ).select() 

	if len(contacts) == 0: #checking len of contact list so we know to redirect or not
		redirect(URL('index'))

	form = Form(db.contacts, record = contactID, deletable = False, csrf_session = session, keep_values = True, formstyle=FormStyleBulma)
	if form.accepted:
		redirect(URL('index'))
	return dict(form=form, user=auth.get_user())

#THE DELETEEEEEEE BUTTOOOOOOOOOOON
@action('delete_contact', method = ['GET' , 'POST'])
@action.uses('index.html', session, db, url_signer.verify())
def delete_contact():

	parameters = request.params
	contact_id = parameters.get('contact_id', None)

	db(db.contacts.id == contact_id).delete()

	redirect(URL('index'))



