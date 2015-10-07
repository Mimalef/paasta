from kernel.controllers import blueprint

@blueprint.route("/logout")
def logout():
	from flask import redirect, session
	
	session.clear()
	
	return redirect('/')