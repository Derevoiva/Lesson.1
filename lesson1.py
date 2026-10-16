"""Corrected Python 3 solutions for the six Lesson 1 exercises.

Original course submission is preserved in `1.Задание.`.
Run: python lesson1.py
"""
from __future__ import annotations


def format_values(first_text: str, first_number: int, second_text: str, second_number: int) -> str:
    return f"{first_text:>10} {first_number:5d} {second_text:>10} {second_number:5d}"


def format_seconds(total_seconds: int) -> str:
    """Convert non-negative seconds to HH:MM:SS (hours may exceed 24)."""
    if total_seconds < 0:
        raise ValueError("Time cannot be negative")
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def repeated_digit_sum(digit: int) -> int:
    """Calculate n + nn + nnn for a single digit n."""
    if not 0 <= digit <= 9:
        raise ValueError("Enter one digit from 0 through 9")
    return digit + (digit * 11) + (digit * 111)


def largest_digit(number: int) -> int:
    """Find the largest decimal digit using arithmetic and a while loop."""
    number = abs(number)
    maximum = 0
    while True:
        number, digit = divmod(number, 10)
        maximum = max(maximum, digit)
        if number == 0:
            return maximum


def business_result(revenue: float, costs: float, employees: int | None = None) -> dict:
    """Report profit, loss and (when profitable) profit margin and profit per employee."""
    if revenue < 0 or costs < 0:
        raise ValueError("Revenue and costs must be non-negative")
    profit = revenue - costs
    result = {"profit": profit, "status": "profit" if profit > 0 else "loss" if profit < 0 else "break-even"}
    if profit > 0:
        result["margin"] = profit / revenue
        if employees is not None:
            if employees <= 0:
                raise ValueError("Employee count must be positive")
            result["profit_per_employee"] = profit / employees
    return result


def running_target_day(initial_distance: float, target_distance: float) -> int:
    """Return the first day reaching target with 10% daily distance growth."""
    if initial_distance <= 0 or target_distance <= 0:
        raise ValueError("Distances must be positive")
    day, distance = 1, initial_distance
    while distance < target_distance:
        distance *= 1.1
        day += 1
    return day


def main() -> None:
    print("Lesson 1 — corrected exercise solutions")
    print("1: variables  2: time  3: repeated digit  4: largest digit  5: business  6: running")
    try:
        choice = input("Choose an exercise (1–6): ").strip()
        if choice == "1":
            first_text = input("First text: ")
            first_number = int(input("First integer: "))
            second_text = input("Second text: ")
            second_number = int(input("Second integer: "))
            print(format_values(first_text, first_number, second_text, second_number))
        elif choice == "2":
            print(format_seconds(int(input("Time in seconds: "))))
        elif choice == "3":
            print(repeated_digit_sum(int(input("Single digit: "))))
        elif choice == "4":
            print(largest_digit(int(input("Integer: "))))
        elif choice == "5":
            revenue = float(input("Revenue: "))
            costs = float(input("Costs: "))
            employees = int(input("Employees (positive integer): ")) if revenue > costs else None
            print(business_result(revenue, costs, employees))
        elif choice == "6":
            initial = float(input("First day distance: "))
            target = float(input("Target distance: "))
            print(f"Target reached on day {running_target_day(initial, target)}")
        else:
            print("Unknown exercise")
    except ValueError as exc:
        print(f"Input error: {exc}")


if __name__ == "__main__":
    main()
