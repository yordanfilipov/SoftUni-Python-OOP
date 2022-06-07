from project.movie import Movie

from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Matrix", 1999, 7.7)
        self.movie.actors = []

    def test_init(self):
        self.assertEqual("Matrix", self.movie.name)
        self.assertEqual(1999, self.movie.year)
        self.assertEqual(7.7, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_set_movie_name_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_set_movie_year_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_already_added(self):
        self.movie.actors = ["Keanu"]
        res = self.movie.add_actor("Keanu")
        self.assertEqual("Keanu is already added in the list of actors!", res)

    def test_add_actor(self):
        self.movie.actors = ["Keanu"]
        self.movie.add_actor("Neo")
        self.assertEqual(["Keanu", "Neo"], self.movie.actors)

    def test_greater_than(self):
        other = Movie("American Pie", 1999, 5.5)
        res = self.movie.__gt__(other)
        self.assertEqual('"Matrix" is better than "American Pie"', res)

    def test_not_greater_than(self):
        other = Movie("Home", 2009, 8.5)
        res = self.movie.__gt__(other)
        self.assertEqual('"Home" is better than "Matrix"', res)

    def test_repr(self):
        self.movie.add_actor("Keanu")
        self.movie.add_actor("Neo")
        expected = f'Name: Matrix\nYear of Release: 1999\n' \
                   f'Rating: 7.70\nCast: Keanu, Neo'
        res = repr(self.movie)
        self.assertEqual(expected, res)


if __name__ == '__main__':
    main()
