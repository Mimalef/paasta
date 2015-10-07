from kernel.controllers import blueprint

@blueprint.route("/home")
def home():
	from kernel import logged
	
	if not logged():
		from flask import redirect
		
		return redirect('/')
	
	from kernel.models.users import select_session, Select
	from kernel.models.users import create_session, Create
	from kernel.models.core import tool_session, Tool
	
	tool_list = []
	selects = select_session.query(Select.tool_id)
	creates = create_session.query(Create.tool_id)
	
	for i in selects:
		tool_list.append(i[0])
	
	selects = tool_session.query(Tool.id, Tool.name).filter(
		Tool.id.in_(
			tool_list
		)
	)
	
	for i in creates:
		tool_list.append(i[0])
	
	creates = tool_session.query(Tool.id, Tool.name).filter(
		Tool.id.in_(
			tool_list
		)
	)
	
	from flask import render_template
	
	return render_template(
		'home.html',
		selects = selects,
		creates = creates
	)
