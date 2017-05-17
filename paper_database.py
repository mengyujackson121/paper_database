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
    title = peewee.TextField()

class AuthorPaper(BaseModel):
    author = ForeignKeyField(Author)
    paper = ForeignKeyField(Paper)


db.drop_tables([Author,AuthorPaper,Paper], safe=True)
db.create_tables([Paper,AuthorPaper,Author], safe=True)


# Add new author with the given fields
def add_author(title=None, first_name=None, middle_name=None, last_name=None):
    author = Author(title=title, first_name=first_name, middle_name=middle_name, last_name=last_name)
    author.save()
    return author

#function get author and title from test_file, save in table: paper
# FIXME
def add_paper(author_ids, title):
    paper = Paper(title=title)
    paper.save()
    for author_id in author_ids:
        authorPaper = AuthorPaper(author=author_id, paper = paper.id)
        authorPaper.save()

# found out all paper by the author
# FIXME
def get_papers_by_author(author_id):
    list_paper = []                                                     #list to store
    for paper in Paper.select().join(AuthorPaper).join(Author).where((Author.id==author_id)):
        list_paper.append(paper)
    return list_paper



