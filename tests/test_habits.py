import unittest
from datetime import date
from habits import add_habit, list_habits, mark_done, get_stats


class TestHabits(unittest.TestCase):

    def test_add_habit(self):
        habit = add_habit("Пить воду")
        self.assertEqual(habit.name, "Пить воду")
        self.assertGreater(habit.id, 0)

    def test_list_habits(self):
        add_habit("Читать книгу")
        habits = list_habits()
        self.assertGreaterEqual(len(habits), 1)

    def test_mark_done(self):
        habit = add_habit("Утренняя зарядка")
        mark_done(habit.id)
        stats = get_stats(habit.id)
        self.assertEqual(stats["total_done"], 1)

    def test_mark_done_with_date(self):
        habit = add_habit("Медитация")
        custom_date = date(2023, 1, 1)
        mark_done(habit.id, on_date=custom_date)
        stats = get_stats(habit.id)
        self.assertEqual(stats["total_done"], 1)


if __name__ == '__main__':
    unittest.main()
