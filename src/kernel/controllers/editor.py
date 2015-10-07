from kernel.controllers import blueprint

@blueprint.route('/editor', methods=['GET'])
def edit():
	from kernel import logged
	
	if not logged():
		from flask import redirect
		
		return redirect('/')
	
	from flask import request
	
	try:
		path = request.args['path']
		tool = request.args['id']	
	except Exception:
		return 'invalid parameter(s)'
	
	try:
		code = request.args['code']
		save = request.args['save']		
	except Exception:
		code = None
		save = None
	
	from kernel.config import TOOLS_DIR
	from os.path import exists
	
	full_path = TOOLS_DIR + tool + '/' + path
	
	if(not exists(full_path)):
		return 'invalid path'
	
	if save and code:
		f = open(full_path, 'w')
		f.write(code)
		
		from flask import redirect
		
		return redirect('/editor?id=' + tool + '&path=' + path)
	
	f = open(full_path, 'r')
	content = f.read()
	
	from flask import render_template
	
	return render_template(
		'editor.html',
		tool = tool,
		path = path,
		content = content
	)