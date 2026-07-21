import json, argparse

# Open and Read contents of expenses.json with exception handling
def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("file dosen't exist")
        return []

def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)
        return expenses

def add_expenses(item):
    current = load_expenses()
    current.append(item)
    save_expenses(current)

def delete_expenses(id):
        current = [i for i in load_expenses() if i["id"] != id]
        save_expenses(current)


def list_expenses(category=None):
    for i in load_expenses():
        if category is None or i["category"] == category:
            for key, value in i.items():
                print(f"{key}: {value}")
            print()

list_expenses()

# delete_expenses()
save_expenses(load_expenses())



def main():
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
        new_id = max([e["id"] for e in current], default=0) + 1
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



