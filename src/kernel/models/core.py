from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from kernel.config import DATA_DIR

core_engine = create_engine('sqlite:///' + DATA_DIR + 'core.sqlite')
user_session = sessionmaker(bind = core_engine)
tool_session = sessionmaker(bind = core_engine)
user_session = user_session()
tool_session = tool_session()
Base = declarative_base()

class User(Base):
	from sqlalchemy import Column, Integer, String
	
	__tablename__ = 'users'
	
	id = Column(Integer, primary_key = True)
	username = Column(String, nullable = False, unique = True)
	password = Column(String, nullable = False)

	def __init__(self, username, password):
		self.username = username
		self.password = password

class Tool(Base):
	from sqlalchemy import Column, Integer, String, Binary
	
	__tablename__ = 'tools'
	
	id = Column(Integer, primary_key = True)
	name = Column(String, nullable = False, unique = True)
	creator = Column(Integer, nullable = False)
	describe = Column(String)
	license = Column(String)

	def __init__(self, name, creator, describe, license = 'GPL'):
		self.name = name
		self.creator = creator
		self.describe = describe
		self.license = license

Base.metadata.create_all(core_engine)