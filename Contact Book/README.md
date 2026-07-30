# Contact Book

A simple command-line contact management application written in Python. Contacts are stored in memory during use and persisted to a local `contacts.json` file.

## Features

- **Add Contact** — Create a new contact with an ID, full name, phone number, email, and address.
- **Save Contacts** — Write all in-memory contacts to `contacts.json`.
- **Update Contact** — Edit an existing contact's name, phone, email, or address.
- **Search Contact** — Look up and display a single contact by ID.
- **Delete Contact** — Remove a contact by ID (also saves automatically).
- **Display All Contacts** — List every stored contact.
- **Exit** — Quit the application.

## Requirements

- Python 3.x
- No external dependencies (uses only the standard library: `json`, `os`)

## Usage

Run the script from the terminal:

```bash
python contact_book.py
```

You'll see a menu:

```
==========================================
               Contact Book
==========================================

1. Add Contact
2. Save Contacts
3. Update Contact
4. Search Contact
5. Delete Contact
6. Display All Contacts
7. Exit
Enter choice:
```

Enter the number corresponding to the action you want to perform, then follow the prompts.

## Data Storage

- Contacts are stored in a dictionary keyed by `contact_id` while the program runs.
- Selecting **Save Contacts** (or performing an update/delete) writes the current data to `contacts.json` in the same directory as the script.
- On startup, if `contacts.json` already exists, it is loaded automatically so previous contacts are available.

> **Note:** After adding a new contact, be sure to choose **Save Contacts** (option 2) if you want it persisted to disk — `add_contact` only updates the in-memory data.

## File Structure

```
.
├── contact_book.py    # Main application script
└── contacts.json       # Auto-generated data file (created on first save)
```

## Example Session

```
Enter choice:  1
Enter Contact ID:  001
Enter full name:  Jane Doe
Enter Phone Number:  555-1234
Enter Email:  jane@example.com
Enter Address:  123 Main St

Enter choice:  2
Data saved successfully!!!

Enter choice:  4
Enter Contact ID:  001
Contact ID:                 001
Full Name:                  Jane Doe
Phone Number:               555-1234
Email:                      jane@example.com
Address:                    123 Main St
```

## Potential Improvements

- Auto-save immediately after adding a contact.
- Input validation for phone numbers and email addresses.
- Duplicate-ID checks with clearer feedback in the menu flow.
- Export contacts to CSV.