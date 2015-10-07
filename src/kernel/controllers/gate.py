from kernel.controllers import blueprint

@blueprint.route("/", methods=['GET', 'POST'])
def gate():
	from kernel import logged
	
	if logged():
		from flask import redirect
		
		return redirect('/home')
	
	from flask import request
	
	if request.method == 'POST':
		if request.form['username'] and request.form['password']:
			username = request.form['username']
			password = request.form['password']
			button = request.form['submit']
			
		else:
			return 'error'
		
		if(button == 'Register'):
			if not register(username, password):
				return 'Error'
			
			if login(username, password):
				from flask import redirect
				
				return redirect('/home')
		
		if(button == 'Login'):
			if login(username, password):
				from flask import redirect
				
				return redirect('/home')
			
			return 'Wrong Username or Password'

	from flask import render_template
	
	return render_template('gate.html')

def register(username, password):
	from kernel.models.core import user_session, User
	
	new_user = User(
		username,
		password
	)
	
	try:
		user_session.add(new_user)
		user_session.commit()
		
	except Exception, e:
		user_session.rollback()
		
		return False
	
	return True
	
def login(username, password):
	from kernel.models.core import user_session, User
	from flask import session
	
	row = user_session.query(User.id).\
		filter_by(username = username).\
		filter_by(password = password).first()
	
	if row:
		session['id'] = row[0]
		
		return True
	
	return False
