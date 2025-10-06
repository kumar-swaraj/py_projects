from datetime import datetime

import pandas as pd
from habit_tracker import Habit, track_habit
from tabulate import tabulate


def main() -> None:
    habits: list[Habit] = [
        track_habit("Coffee", datetime(2025, 8, 3), cost=1, minutes_used=5),
        track_habit("Alcohol", datetime(2025, 9, 5, 22), cost=5, minutes_used=15),
        track_habit("Sugar drinks", datetime(2025, 9, 16, 19), cost=1, minutes_used=3),
        track_habit("Being lazy", datetime(2025, 10, 5, 17), cost=1, minutes_used=3),
    ]

    df = pd.DataFrame(habits)

    print(
        tabulate(
            df.values.tolist(),
            headers=df.columns.tolist(),
            tablefmt="psql",
            showindex=True,
        )
    )


if __name__ == "__main__":
    main()
