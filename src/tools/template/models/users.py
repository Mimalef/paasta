from kernel.models.tools import Base, tool_engine
from sqlalchemy.orm import sessionmaker

user_engine = tool_engine(tool)
user_session = sessionmaker(bind = user_engine)
user_session = user_session()

class User(Base):
	from sqlalchemy import Column, Integer
	
	__tablename__ = "users"
	
	user_id = Column(Integer, nullable = False, unique = True)

	def __init__(self, user_id):
		self.user_id = user_id
		
Base.metadata.create_all(user_engine)