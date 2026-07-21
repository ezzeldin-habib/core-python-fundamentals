# CLI Expense Tracker

A simple Command Line Interface (CLI) utility built to manage and track daily expenses. The project demonstrates core Python functionalities, including structured file handling, exception handling, data parsing, and user input validation using `argparse`. It reads from and writes to a local `expenses.json` file as a lightweight data store.

## 🛠️ Features

*   **Add Expenses**: Appends a new expense entry with auto-incrementing unique IDs.
*   **List Expenses**: Displays stored expenses with optional filtering by category.
*   **Delete Expenses**: Safely removes a specific entry using its unique ID.
*   **Robust Error Handling**: Uses safe dictionary extraction (`.get()`) to read data records without crashing if optional fields are missing.

## 🚀 Usage

Run the script from your terminal using the following subcommands:

### 1. Add an Expense
```bash
python "CLI expense tracker.py" add --name "Coffee" --category "food" --amount 3.50 --date "2026-07-18" --description "Iced latte"
```

### 2. List All Expenses
```bash
python "CLI expense tracker.py" list
```

### 3. Filter Expenses by Category
```bash
python "CLI expense tracker.py" list --category "food"
```

### 4. Delete an Expense
```bash
python "CLI expense tracker.py" delete 1
```

## 📊 Data Schema Example

Data is permanently retained inside `expenses.json` using a unified layout structure:

```json
[
    {
        "id": 1,
        "name": "Coffee",
        "category": "food",
        "amount": 3.5,
        "date": "2026-07-18",
        "description": "Iced latte"
    }
]
```
