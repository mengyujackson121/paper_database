import paper_database


def create_paper_test():
    paper_database.add_paper(author="steven jackson", title="foo")
    papers = paper_database.get_papers_by_author(author="steven jackson")
    assert papers[0].title == "foo"


def main():
    create_paper_test()


if __name__ == '__main__':
    main()
