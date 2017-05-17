import paper_database


def create_paper_test(id_1, id_2):
    paper_database.add_paper(author_ids=[id_1], title="Steven's Masterpiece")
    paper_database.add_paper(author_ids=[id_2], title="Mengyu's Even Better Book!")
    papers_1 = paper_database.get_papers_by_author(id_1)
    assert papers_1[0].title == "Steven's Masterpiece"
    papers_2 = paper_database.get_papers_by_author(id_2)
    assert papers_2[0].title == "Mengyu's Even Better Book!"


def create_author_test():
    new_author = paper_database.add_author(title="Mr.", first_name="Steven", middle_name="Tecumseh",
                                           last_name="Jackson")
    new_author_2 = paper_database.add_author(title="Mrs.", first_name="Mengyu", middle_name="Bai", last_name="Jackson")
    return new_author.id, new_author_2.id


def one_paper_two_authors_test(id_1, id_2):
    paper_name = "Work together!"
    paper_database.add_paper(author_ids=[id_1, id_2], title=paper_name)
    assert paper_name in [paper.title for paper in paper_database.get_papers_by_author(id_1)]
    assert paper_name in [paper.title for paper in paper_database.get_papers_by_author(id_2)]


def main():
    id_1, id_2 = create_author_test()
    create_paper_test(id_1, id_2)
    one_paper_two_authors_test(id_1, id_2)


if __name__ == '__main__':
    main()
