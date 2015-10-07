from kernel.controllers import blueprint

@blueprint.route('/explorer', methods=['GET', 'POST'])
def explorer():
	from kernel import logged
	
	if not logged():
		from flask import redirect
		
		return redirect('/')
	
	from flask import request
	
	try:
		path = request.args['path']
	except Exception:
		path = ''
	
	try:
		tool = request.args['id']
	except Exception:
		return 'invalid parameter(s)'
	
	from kernel.config import TOOLS_DIR
	from os import listdir
	from os.path import isfile, exists
	
	full_path = TOOLS_DIR + tool + '/' + path
	
	if(not exists(full_path)):
		return 'invalid path'
	
	dirs = []
	files = []

	for item in listdir(full_path):
		if isfile(full_path + '/' + item):
			files.append(item)
		else:
			dirs.append(item)
		
	if path == '/' or path == '':
		back = None
	else:
		back = path[:path.rfind('/')]
	
	from flask import render_template
	
	return render_template(
		'explorer.html',
		path = path,
		tool = tool,
		dirs = dirs,
		files = files,
		back = back
	)

@blueprint.route('/explorer/create_file', methods=['GET', 'POST'])
def explorer_create_file():
	from kernel import logged
	
	if not logged():
		from flask import redirect
		
		return redirect('/')
	
	from flask import request
	
	try:
		tool = request.args['id']
		path = request.args['path']
	except Exception:
		return 'invalid parameter(s)'
	
	try:
		name = request.args['name']
		create = request.args['name']
	except Exception:
		name = None
		create = None
	
	if name and create:
		from kernel.config import TOOLS_DIR
		
		new_file = TOOLS_DIR + tool + '/' + path + '/' + name
		
		open(new_file, 'w').close()
		
		from flask import redirect
		
		return redirect('/explorer?id=' + tool)
	
	from flask import render_template
	
	return render_template(
		'create.html',
		tool = tool,
		path = path
	)

@blueprint.route('/explorer/create_folder', methods=['GET', 'POST'])
def explorer_create_folder():
	from kernel import logged
	
	if not logged():
		from flask import redirect
		
		return redirect('/')
	
	from flask import request
	
	try:
		tool = request.args['id']
		path = request.args['path']
	except Exception:
		return 'invalid parameter(s)'
	
	try:
		name = request.args['name']
		create = request.args['name']
	except Exception:
		name = None
		create = None
	
	if name and create:
		from kernel.config import TOOLS_DIR
		from os import mkdir
		from os.path import exists
		
		new_directory = TOOLS_DIR + tool + '/' + path + '/' + name
		
		if not exists(new_directory):
			mkdir(new_directory)
		
		from flask import redirect
		
		return redirect('/explorer?id=' + tool)
	
	from flask import render_template
	
	return render_template(
		'create.html',
		tool = tool,
		path = path
	)
