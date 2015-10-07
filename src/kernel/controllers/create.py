from kernel.controllers import blueprint

@blueprint.route("/create", methods=['GET', 'POST'])
def create():
	from kernel import logged
	
	if not logged():
		from flask import redirect
		
		return redirect('/')
	
	from flask import request
	
	try:
		name = request.args['name']
		create = request.args['create']
	except Exception:
		name = None
		create = None
	
	if name and create:
		from flask import session
		
		creator = session['id']
		
		tool_id = register(name, creator)
		
		if not tool_id:
			return 'error'
		
		from kernel.config import TOOLS_DIR
		
		template_folder = TOOLS_DIR + 'template/'
		new_tool_folder = TOOLS_DIR + str(tool_id) + '/'
		
		from os import mkdir
		
		mkdir(new_tool_folder)
		clone(template_folder, new_tool_folder)
		
		from flask import redirect
		
		return redirect('/explorer?id=' + str(tool_id))

	from flask import render_template
	
	return render_template(
		'create.html',
		tool = '',
		path = ''
	)

def register(name, creator):	
	from kernel.models.core import tool_session, Tool
	from kernel.models.users import create_session, Create
	
	new_tool = Tool(
		name,
		creator,
		''
	)
	
	try:
		tool_session.add(new_tool)
		tool_session.commit()
		
	except Exception, e:
		tool_session.rollback()
		return None
	
	row = tool_session.query(Tool.id).\
		filter_by(name = name).first()
	
	tool_id = row[0]
	
	new_create = Create(
		tool_id
	)
	
	try:
		create_session.add(new_create)
		create_session.commit()
		
	except Exception, e:
		create_session.rollback()
		return False
	
	return tool_id
	
def clone(source, dest):
	from os import listdir
	from os.path import isfile
	
	for item in listdir(source):
		if isfile(source + item):
			source_file = open(source + item , 'r')
			dest_file = open(dest + item , 'w')
			
			dest_file.write(source_file.read())
			
		else:
			from os import mkdir
			
			mkdir(dest + item)
			clone(source + item + '/', dest + item + '/')
