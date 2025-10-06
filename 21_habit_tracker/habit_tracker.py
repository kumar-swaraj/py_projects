from dataclasses import dataclass
from datetime import datetime


@dataclass
class Habit:
    name: str
    time_since: str
    remaining_days: str
    minutes_saved: float
    money_saved: str


def track_habit(name: str, start: datetime, cost: float, minutes_used: float) -> Habit:
    """Calculates the time elapse, time remaining, cost and minutes wasted on a habit.

    Args:
        name (str): The name of the habit.
        start (datetime): The start date of the habit.
        cost (float): The cost of the habit per day.
        minutes_used (float): The amount of minutes used perfoming the habit.

    Returns:
        Habit: An habit object with given data.
    """

    goal: int = 60
    hourly_wage: int = 30

    time_elapsed: float = (datetime.now() - start).total_seconds()

    hours: float = round(time_elapsed / 60 / 60, 1)
    days: float = round(hours / 24, 2)

    money_saved = cost * days
    minutes_used = round(days * minutes_used)
    total_money_saved = f"${round(money_saved + (minutes_used / 60 * hourly_wage), 2)}"

    days_to_go: float = round(goal - days)

    remaining_days: str = "Cleared!" if days_to_go <= 0 else str(days_to_go)
    time_since = f"{days} days" if hours > 72 else f"{hours} hours"

    return Habit(
        name,
        time_since,
        remaining_days,
        minutes_used,
        total_money_saved,
    )
