from kernel.controllers import blueprint

@blueprint.route('/select')
def select():
	from kernel import logged
	
	if not logged():
		from flask import redirect
		
		return redirect('/')
	
	from flask import request
	
	agree = None
	
	try:
		tool = request.args['id']
		
		try:
			agree = request.args['agree']
		
		except Exception:
			pass
		
	except Exception:
		return 'invalid parameter(s)'
	
	if agree:
		if registered(tool):
			from flask import redirect
			
			return redirect('/tools/' + tool)
		
		else:
			return 'Error'
	
	from kernel.models.core import tool_session, Tool
	
	license = tool_session.query(Tool.license).filter_by(id = tool).first()
	
	if not license:
		return 'Not found'
	
	from flask import render_template
	
	return render_template(
		'select.html',
		tool = tool,
		license = license
	)

def registered(tool_id):
	from kernel.models.users import select_session, Select
	
	new_select = Select(
		tool_id
	)
	
	try:
		select_session.add(new_select)
		select_session.commit()
	
	except Exception, e:
		select_session.rollback()
		return False
	
	return True
