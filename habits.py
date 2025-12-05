from dataclasses import dataclass, field
from datetime import date
from typing import List, Dict


@dataclass
class Habit:
    """Класс, описывающий привычку."""
    id: int
    name: str
    created_at: date
    done_dates: List[date] = field(default_factory=list)


# Простое "хранилище" привычек в памяти
_habits: Dict[int, Habit] = {}
_next_id: int = 1


def add_habit(name: str) -> Habit:
    """
    Добавляет новую привычку и возвращает её объект.
    """
    global _next_id
    habit = Habit(id=_next_id, name=name, created_at=date.today())
    _habits[_next_id] = habit
    _next_id += 1
    return habit


def list_habits() -> List[Habit]:
    """
    Возвращает список всех привычек.
    """
    return list(_habits.values())


def mark_done(habit_id: int, on_date: date | None = None) -> None:
    """
    Отмечает привычку выполненной в указанную дату (или сегодня).
    Если привычка не найдена, бросает KeyError.
    """
    if on_date is None:
        on_date = date.today()

    habit = _habits[habit_id]  # если нет такого id, будет KeyError
    if on_date not in habit.done_dates:
        habit.done_dates.append(on_date)


def get_stats(habit_id: int) -> Dict[str, int]:
    """
    Возвращает простую статистику по привычке:
    - total_done: сколько раз выполнена
    """
    habit = _habits[habit_id]
    return {"total_done": len(habit.done_dates)}
