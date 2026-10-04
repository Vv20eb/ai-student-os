import json


def load_tasks():
    with open("data/tasks.json", "r") as file:
        tasks = json.load(file)

    return tasks


def show_tasks(tasks):
    categories = ["SCHOOL", "GROWTH", "LIFE"]

    print("\n======================")
    print("     AI STUDENT OS")
    print("======================")

    for category in categories:
        print(f"\n{category}")
        print("-" * 20)

        category_tasks = [
            task
            for task in tasks
            if task["category"] == category
        ]

        if not category_tasks:
            print("No tasks.")

        for task in category_tasks:
            status = task["status"]
            priority = task["priority"]
            title = task["title"]

            print(f"[{status}] [{priority}] {title}")


def main():
    tasks = load_tasks()
    show_tasks(tasks)


if __name__ == "__main__":
    main()