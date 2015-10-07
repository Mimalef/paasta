def logged():
	from flask import session
	
	try:
		if session['id']:
			return True
	except Exception:
		return False