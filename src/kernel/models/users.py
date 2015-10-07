from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from kernel.config import DATA_DIR
from flask import session

Base = declarative_base()

user_engine = create_engine('sqlite:///' + DATA_DIR + 'users/' + str(session['id']) + '.sqlite')
select_session = sessionmaker(bind = user_engine)
create_session = sessionmaker(bind = user_engine)
select_session = select_session()
create_session = create_session()

class Select(Base):
	from sqlalchemy import Column, Integer
	
	__tablename__ = "selects"
	
	tool_id = Column(Integer, nullable = False, unique = True, primary_key = True)

	def __init__(self, tool_id):
		self.tool_id = tool_id
		
class Create(Base):
	from sqlalchemy import Column, Integer, ForeignKey
	
	__tablename__ = "creates"
	
	tool_id = Column(Integer, nullable = False, unique = True, primary_key = True)

	def __init__(self, tool_id):
		self.tool_id = tool_id
		
Base.metadata.create_all(user_engine)
