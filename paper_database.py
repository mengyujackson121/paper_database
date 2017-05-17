import peewee
from peewee import *
db = MySQLDatabase('mengyu', user='root',passwd='MySQLpassword')    # create a connection with database, setup username and password
db.connect()


class BaseModel(Model):
    class Meta:
        database = db

# peewee magic talk to database

# FIXME
class Author(BaseModel):
    title = peewee.CharField()
    first_name = peewee.CharField()
    middle_name = peewee.CharField()
    last_name = peewee.CharField()


class Paper(BaseModel):
    author = ForeignKeyField(Author)
    title = peewee.TextField()

db.drop_tables([Author,Paper])
db.create_tables([Paper,Author], safe=True)
# Add new author with the given fields
# FIXME
def add_author(title=None, first_name=None, middle_name=None, last_name=None):
    author = Author(title=title, first_name=first_name, middle_name=middle_name, last_name=last_name)
    author.save()
    return author

#function get author and title from test_file, save in table: paper
# FIXME
def add_paper(author_id, title):
    paper = Paper(author=author_id, title=title)
    paper.save()

# found out all paper by the author
# FIXME
def get_papers_by_author(author):
    list_paper = []                                                     #list to store
    for book in Paper.filter(author=author):
        list_paper.append(book)
    return list_paper



