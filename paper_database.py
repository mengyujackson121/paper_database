import peewee
from peewee import *
db = MySQLDatabase('mengyu', user='root',passwd='MySQLpassword')    # create a connection with database, setup username and password


#function get author and title from test_file, save in table: paper
def add_paper(author, title):
    paper = Paper(author=author, title=title)
    paper.save()

#found out all paper by the author
def get_papers_by_author(author):
    list_paper = []                                                     #list to store
    for book in Paper.filter(author=author):
        list_paper.append(book)
    return list_paper

#peewee magic talk to database
class Paper(peewee.Model):
    author = peewee.CharField()
    title = peewee.TextField()

    class Meta:
        database = db



