from kernel.controllers import blueprint

@blueprint.route('/tools')
def tools():
	from kernel.models.core import tool_session, Tool
	
	ids = []
	names = []
	rows = tool_session.query(Tool.id, Tool.name)
	
	for row in rows:
		ids.append(row[0])
		names.append(row[1])
	
	from flask import render_template
	
	return render_template(
		'tools.html',
		count = len(ids),
		ids = ids,
		names = names
	)
