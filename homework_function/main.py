from pathlib import Path
import csv
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "Corp_Summary.csv"
OUTPUT_FILE = BASE_DIR / "report.csv"


# Читаем файл
def read_file(file_name):
    with open(file_name, "r") as f:
        reader = csv.DictReader(f, delimiter=";")
        return list(reader)


# Вариант 1: иерархия департаментов
def get_department_hierarchy(employees) -> None:
    departments = defaultdict(set)
    for employee in employees:
        department = employee["Департамент"]
        team = employee["Отдел"]
        departments[department].add(team)

    for department, teams in departments.items():
        print(department)
        for team in sorted(teams):
            print(f"\t{team}")


# Вариант 2: Сводка по зарплатам
def get_salary_summary(employees: list[dict]) -> list[dict]:
    salaries = defaultdict(list)
    for employee in employees:
        department = employee["Департамент"]
        salary = int(employee["Оклад"])
        salaries[department].append(salary)

    result = []

    for department, salaries in salaries.items():
        count = len(salaries)
        min_salary = min(salaries)
        max_salary = max(salaries)
        avg_salary = sum(salaries) / count

        result.append(
            {
                "department": department,
                "count": count,
                "min_salary": min_salary,
                "max_salary": max_salary,
                "avg_salary": avg_salary,
            }
        )

    return result


# Вывод отчета на экран
def print_report(report: list[dict]) -> None:
    for row in report:
        print(row)
        print()


# Вывод отчета в файл
def get_salary_summary_write_file(report: list[dict]) -> None:
    with open(OUTPUT_FILE, "w") as f:
        writer = csv.DictWriter(f, fieldnames=report[0].keys())
        writer.writeheader()
        writer.writerows(report)

    print(f"Report written to {OUTPUT_FILE}")


def main(variant: int) -> None:
    employees = read_file(INPUT_FILE)

    match variant:
        case 1:
            get_department_hierarchy(employees)
        case 2:
            report = get_salary_summary(employees)
            print_report(report)
        case 3:
            report = get_salary_summary(employees)
            get_salary_summary_write_file(report)
        case _:
            print("Invalid variant")


if __name__ == "__main__":
    variant = int(input("Enter variant: "))
    main(variant)
