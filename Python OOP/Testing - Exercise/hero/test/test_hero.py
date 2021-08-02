from unittest import TestCase, main
from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("test", 50, 100, 1.15)
        self.enemy_hero = Hero("test2", 50, 100, 1.15)

    def test_hero_init(self):
        self.assertEqual("test", self.hero.username)
        self.assertEqual(50, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(1.15, self.hero.damage)

    def test_hero_fights_self_raises(self):
        self.enemy_hero.username = "test"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_fights_with_negative_health_raises(self):
        self.hero.health = -5
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_hero_fight_enemy_with_negative_health_raises(self):
        self.enemy_hero.health = -5
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight test2. He needs to rest", str(ex.exception))

    def test_hero_takes_damage_after_fighting(self):
        self.assertEqual(100, self.hero.health)
        self.hero.battle(self.enemy_hero)
        self.assertEqual(42.50000000000001, self.hero.health)

    def test_battle_end_draw(self):
        self.hero.damage = 2
        self.enemy_hero.damage = 2
        expected_result = "Draw"
        actual_result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_result, actual_result)

    def test_hero_wins_battle(self):
        self.hero.damage = 2
        expected_result = "You win"
        actual_result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(51, self.hero.level)
        self.assertEqual(47.50000000000001, self.hero.health)
        self.assertEqual(7, self.hero.damage)

    def test_hero_loses_battle(self):
        self.enemy_hero.damage = 2
        expected_result = "You lose"
        actual_result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(51, self.enemy_hero.level)
        self.assertEqual(47.50000000000001, self.enemy_hero.health)
        self.assertEqual(7, self.enemy_hero.damage)

    def test_hero_str_method(self):
        expected_result = "Hero test: 50 lvl\n" \
                          "Health: 100\n" \
                          "Damage: 1.15\n"
        actual_result = str(self.hero)
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
