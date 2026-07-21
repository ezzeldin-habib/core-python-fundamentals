import json
import argparse

def load_expenses():
    """
    Ingests and parses the JSON data store.
    Handles missing file exceptions safely by returning an empty list.
    """
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("file dosen't exist")
        return []

def save_expenses(expenses):
    """
    Serializes the in-memory payload back into a structured JSON file.
    Applies an indentation level of 4 for human-readable layout.
    """
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)
        return expenses

def add_expenses(item):
    """
    Appends a newly structured data record to the existing dataset.
    Triggers an immediate file-write pipeline update to save changes.
    """
    current = load_expenses()
    current.append(item)
    save_expenses(current)

def delete_expenses(id):
    """
    Filters out a specific record from the data payload using list comprehension.
    Performs a safe state update by using .get() to check unique 'id' values.
    """
    current = [i for i in load_expenses() if i.get("id") != id]
    save_expenses(current)


def list_expenses(category=None):
    """
    Iterates through the data store and streams formatted key-value pairs to stdout.
    Uses fallback dictionary logic to safely parse fields without crashing.
    """
    for i in load_expenses():
        # Safely read the category attribute using .get() to prevent missing key errors
        item_category = i.get("category")
        if category is None or (item_category and item_category.lower() == category.lower()):
            # Define fallback structural schema keys to guarantee clean terminal output
            schema_keys = ["id", "name", "category", "amount", "date", "description"]
            for key in schema_keys:
                print(f"{key}: {i.get(key, 'N/A')}")
            print()

# list_expenses()
# delete_expenses()
# save_expenses(load_expenses())


def main():
    """
    Defines the Command Line Interface (CLI) routing matrix using argparse.
    Maps subcommands (add, delete, list) to their respective functions.
    """
    parser = argparse.ArgumentParser(description="Simple expense tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--name", type=str, required=True)
    add_parser.add_argument("--category", type=str, required=True)
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--date", type=str, required=True)
    add_parser.add_argument("--description", type=str, default="")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--category", type=str, default=None)

    args = parser.parse_args()

    if args.command == "add":
        current = load_expenses()
        # Uses .get() to safely calculate a unique incrementing key index
        new_id = max([e.get("id", 0) for e in current], default=0) + 1
        new_expense = {
            "id": new_id,
            "name": args.name,
            "category": args.category,
            "amount": args.amount,
            "date": args.date,
            "description": args.description
        }
        add_expenses(new_expense)
        print(f"Added expense {new_id}")

    elif args.command == "delete":
        delete_expenses(args.id)
        print(f"Deleted expense {args.id}")

    elif args.command == "list":
        list_expenses(args.category)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
