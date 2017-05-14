import peewee
from peewee import *
db = MySQLDatabase('mengyu', user='root',passwd='MySQLpassword')    # create a connection with database, setup username and password
db.connect()


# peewee magic talk to database
class Paper(peewee.Model):
    author = peewee.CharField()
    title = peewee.TextField()

    class Meta:
        database = db


# FIXME
class Author(peewee.Model):
    class Meta:
        database = db


db.create_tables([Paper], safe=True)


# Add new author with the given fields
# FIXME
def add_author(title=None, first_name=None, middle_name=None, last_name=None):
    pass


#function get author and title from test_file, save in table: paper
# FIXME
def add_paper(author_id, title):
    paper = Paper(author=author, title=title)
    paper.save()


# found out all paper by the author
# FIXME
def get_papers_by_author(author):
    list_paper = []                                                     #list to store
    for book in Paper.filter(author=author):
        list_paper.append(book)
    return list_paper




