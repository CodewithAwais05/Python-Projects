# Library Management System

A simple command-line Library Management System built in Python. It lets you add, update, delete, display, borrow, and return books, with all data persisted to a local JSON file.

## Features

- **Add Book** – Create a new book record with details like title, author, publisher, category, edition, publication year, ISBN, and copy count.
- **Display Book** – View full details of a book by its Book ID.
- **Update Book** – Modify a book's author, title, publisher, or add new copies.
- **Delete Book** – Remove a book record from the library.
- **Borrow Book** – Check out a copy of a book (decreases available copies; marks as "Not Available" when copies run out).
- **Return Book** – Return a borrowed copy (increases available copies; marks as "Available" again).
- **Persistent Storage** – All book records are saved to `books.json` and automatically loaded on startup.

## Requirements

- Python 3.6+

No external dependencies are required — the project only uses Python's built-in `json` and `os` modules.

## Getting Started

1. Clone or download this repository.
2. Run the program:

   ```bash
   python library.py
   ```

3. Use the on-screen menu to interact with the library system.

## Usage

On launch, you'll see a menu:

```
========================================
        LIBRARY MANAGEMENT SYSTEM       
========================================

1. Add Book Record
2. Display Book Record
3. Update Book Record
4. Delete Book Record
5. Borrow Book
6. Return Book
7. Exit
```

Enter the number corresponding to the action you want to perform, then follow the prompts.

### Example: Adding a Book

```
Enter Book ID:  B001
Enter book Title:  The Pragmatic Programmer
Enter Author name:  David Thomas
Enter Publisher name:  Addison-Wesley
Enter book Category:  Software Engineering
Enter book Edition:  2nd
Enter Publication Year:  2019
Enter ISBN:  978-0135957059
Enter total copies:  3
Book Record created!
Record saved successfully!!!
```

### Example: Borrowing a Book

```
Enter Book ID tp borrow:  B001
Book borrowed successfully!
Record saved successfully!!!
```

## Data Storage

Book records are stored in `books.json`, structured as a dictionary keyed by `book_id`. Example entry:

```json
{
    "B001": {
        "book_id": "B001",
        "title": "The Pragmatic Programmer",
        "author": "David Thomas",
        "publisher": "Addison-Wesley",
        "category": "Software Engineering",
        "edition": "2nd",
        "publication_year": "2019",
        "isbn": "978-0135957059",
        "total_copies": 3,
        "available_copies": 3,
        "status": "Available"
    }
}
```

This file is created automatically the first time you add a book, and is read on every subsequent run so your data persists between sessions.

## Project Structure

```
.
├── library.py     # Main application script
├── books.json     # Auto-generated data file (created on first run)
└── README.md      # Project documentation
```

## Notes & Possible Improvements

- Input validation is minimal (e.g., entering non-numeric text for copy counts or menu choices will raise an error). Adding `try/except` blocks around numeric input would make the app more robust.
- Book IDs are not currently validated for uniqueness beyond dictionary key overwriting — adding a book with an existing ID will overwrite the previous record.
- Consider adding a search/list-all-books feature for easier browsing of the catalog.

## License

This project is free to use and modify for personal or educational purposes.