
TOOLS_DIR = '/srv/tools/'

def tool_id():
	from sys import argv
	
	return argv[1]

def set_env():
	from os import environ
	
	for i in environ:
		environ[i] = ''
	
def set_path():
	from sys import path

	path.append(TOOLS_DIR + tool_id)

def render_template(template_file, **arguments):
	from jinja2 import Template
	
	tool_folder = TOOLS_DIR + tool_id
	template_folder = 'views'
	
	f = open(tool_folder + '/' + template_folder + '/' + template_file)
	
	template = Template(f.read())
	
	return template.render(arguments)

tool_id = tool_id()
set_path()
