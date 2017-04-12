from sqlalchemy import create_engine
from coolscrapy.settings import DATABASE

from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

#declare a mapping
Base = declarative_base()

#connect the database
def db_connect():
	#drivername, host,  = DATABASE['host']
	engine = create_engine(''+DATABASE['drivername']+'://'+DATABASE['username']+':'+DATABASE['password']+'@'+DATABASE['host']+'/'+DATABASE['database']+'?charset='+DATABASE['query']['charset'])
	return engine

def create_news_table(engine):
	#create table
	Base.metadata.create_all(engine)


#declare table "Article"
"""
class Article(Base):
	__tablename__ = 'sina_article'
	id = Column(Integer, primary_key=True)
	url = Column(String(200))
	title = Column(Text)
	publish_time = Column(String(20))
	#summary = Column(Text)
	body = Column(Text)
	keywords = Column(Text)
	uploadTime = Column(TIMESTAMP)
	#source_site = Column(String(50))

	def __repr__(self):
		return "<Article(url='%s', title='%s', publish_time='%s', body='%s', keywords='%s')>" % \
			   (self.url, self.title, self.publish_time, self.body, self.keywords)
"""
class Article(Base):
	__tablename__ = 'baike_artists'
	id = Column(Integer, primary_key=True)
	url = Column(String(200))
	name = Column(Text)
	#publish_time = Column(String(20))
	summary = Column(Text)
	#content = Column(Text)
	#tagItems = Column(Text)
	uploadTime = Column(TIMESTAMP)
	#source_site = Column(String(50))

	def __repr__(self):
		return "<Article(url='%s', name='%s',  summary='%s')>" % \
			   (self.url, self.name, self.summary)
