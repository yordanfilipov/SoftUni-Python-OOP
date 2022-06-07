from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Ivan", 100, 200, 300)
        self.enemy_hero = Hero("Geogri", 100, 200, 300)
        self.strong_hero = Hero("Boiko", 1000, 200000, 3000)

    def test_init(self):
        self.assertEqual("Ivan", self.hero.username)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(200, self.hero.health)
        self.assertEqual(300, self.hero.damage)

    def test_equals_usernames_exception(self):
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(e.exception))

    def test_your_health_below_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_enemy_health_below_zero(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ve.exception))

    def test_draw(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("Draw", result)

    def test_win(self):
        result = self.strong_hero.battle(self.enemy_hero)
        self.assertEqual(result, "You win")
        self.assertEqual(self.strong_hero.health, 170005)
        self.assertEqual(self.strong_hero.damage, 3005)
        self.assertEqual(self.strong_hero.level, 1001)
        self.assertEqual(self.enemy_hero.health, -2999800)
        self.assertEqual(self.enemy_hero.damage, 300)
        self.assertEqual(self.enemy_hero.level, 100)

    def test_lose(self):
        result = self.enemy_hero.battle(self.strong_hero)
        self.assertEqual(result, "You lose")
        self.assertEqual(self.strong_hero.health, 170005)
        self.assertEqual(self.strong_hero.damage, 3005)
        self.assertEqual(self.strong_hero.level, 1001)
        self.assertEqual(self.enemy_hero.health, -2999800)
        self.assertEqual(self.enemy_hero.damage, 300)
        self.assertEqual(self.enemy_hero.level, 100)


    def test_str(self):
        self.assertEqual(str(self.hero),
                         f"Hero {self.hero.username}: {self.hero.level} lvl\n"
                         f"Health: {self.hero.health}\n"
                         f"Damage: {self.hero.damage}\n")


if __name__ == "__main__":
    main()
