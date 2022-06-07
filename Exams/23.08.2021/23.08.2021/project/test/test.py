from project.library import Library

from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.lib = Library("SU")

    def test_init(self):
        self.assertEqual(self.lib.name, "SU")
        self.assertEqual(self.lib.books_by_authors, {})
        self.assertEqual(self.lib.readers, {})

    def test_if_name_empty(self):
        new = ""
        exp = "Name cannot be empty string!"

        with self.assertRaises(ValueError) as context:
            self.lib.name = new

        self.assertEqual(exp, str(context.exception))

    def test_add_book_if_not_author(self):
        self.lib.books_by_authors = {}
        self.lib.add_book("Ivan Vazov", "Pod Igoto")
        exp = {"Ivan Vazov": ['Pod Igoto']}

        self.assertEqual(exp, self.lib.books_by_authors)

    def test_add_book_if_not_title(self):
        self.lib.books_by_authors = {"Ivan Vazov": ['Pod Igoto']}
        self.lib.add_book("Ivan Vazov", "Chichovci")
        exp = {"Ivan Vazov": ['Pod Igoto', 'Chichovci']}

        self.assertEqual(exp, self.lib.books_by_authors)

    def test_add_reader_if_not_in_list(self):
        self.lib.readers = {}
        self.lib.add_reader("Ivan")
        exp = {"Ivan": []}

        self.assertEqual(exp, self.lib.readers)

    def test_add_reader_already_in_list(self):
        self.lib.readers = {"Ivan": []}
        exp = f"Ivan is already registered in the SU library."

        self.assertEqual(exp, self.lib.add_reader("Ivan"))

    def test_rent_book_if_reader_name_not_in_readers(self):
        self.lib.readers = {"Ivan": []}
        self.lib.books_by_authors = {"Ivan Vazov": ['Pod Igoto']}
        act = self.lib.rent_book("Gosho", "Ivan Vazov", "Pod Igoto")
        exp = f"Gosho is not registered in the SU Library."

        self.assertEqual(exp, act)

    def test_rent_book_if_book_author_not_in_authors(self):
        self.lib.readers = {"Ivan": []}
        self.lib.books_by_authors = {"Ivan Vazov": ['Pod Igoto']}
        act = self.lib.rent_book("Ivan", "Aleko Konstantinov", "Pod Igoto")
        exp = f"SU Library does not have any Aleko Konstantinov's books."

        self.assertEqual(act, exp)

    def test_rent_book_if_book_title_not_in_author_titles(self):
        self.lib.readers = {"Ivan": []}
        self.lib.books_by_authors = {"Ivan Vazov": ['Pod Igoto']}
        act = self.lib.rent_book("Ivan", "Ivan Vazov", "Chichovci")
        exp = f"""SU Library does not have Ivan Vazov's "Chichovci"."""
        self.assertEqual(act, exp)

    def test_rent_book_if_everything_is_ok(self):
        self.lib.readers = {"Ivan": []}
        self.lib.books_by_authors = {"Ivan Vazov": ['Pod Igoto']}
        self.lib.rent_book("Ivan", "Ivan Vazov", "Pod Igoto")
        exp_reader = {'Ivan': [{'Ivan Vazov': 'Pod Igoto'}]}
        exp_author = {"Ivan Vazov": []}

        self.assertEqual(exp_reader, self.lib.readers)
        self.assertEqual(exp_author, self.lib.books_by_authors)

if __name__ == "__main__":
    main()
