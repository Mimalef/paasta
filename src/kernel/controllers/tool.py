from kernel.controllers import blueprint
	
@blueprint.route('/tools/<tool_id>', methods = ['GET', 'POST'])
def tool(tool_id = None):
	from kernel import logged
	
	if not logged():
		from flask import redirect
		
		return redirect('/')
	
	if not registered(tool_id):
		from flask import redirect
		
		return redirect('/select?id=' + str(tool_id))
	
	from kernel.config import TOOLS_DIR
	
	tool_folder = TOOLS_DIR + str(tool_id) + '/'
	template_folder = 'templates/'
	
	preload_file = open(TOOLS_DIR + 'preload.py', 'r')
	main_file = open(tool_folder + 'main.py', 'r')
	
	code = preload_file.read() + main_file.read()
	
	from subprocess import Popen, PIPE
	
	p = Popen(
		[
			'python',
			'-c ' + code,
			tool_id
		],
		stdout = PIPE,
		stderr = PIPE
	)
	output, err = p.communicate()
	
	if err:
		return '<pre>' + err + '</pre>'
	
	return output

	from flask import render_template

	return render_template(
		'tool.html',
		view = output
	)

def registered(tool_id):
	from kernel.models.users import select_session, Select
	
	row = select_session.query(Select.tool_id).\
		filter_by(tool_id = tool_id).first()
	
	if row:
		return True
	
	return False
