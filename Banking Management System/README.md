# Bank Management System

A simple console-based **Bank Management System** built in Python. It supports admin and customer logins, account creation, deposits, withdrawals, and persistent storage using a JSON file.

## Features

- **Admin Panel**
  - Add new customer accounts
  - Search for a customer by account number
  - Display all customer accounts
- **Customer Panel**
  - View account details
  - Deposit money
  - Withdraw money (with balance validation)
  - Update email or phone number
  - Change password
- **Data Persistence**
  - All account data is saved to and loaded from `bank_data.json`, so records persist between sessions

## Tech Stack

- **Language:** Python 3
- **Storage:** JSON (`bank_data.json`)
- **Libraries:** `json`, `os` (standard library only — no external dependencies)

## Project Structure

```
Bank Management System/
├── bank_management.py   # Main application file
├── bank_data.json        # Auto-generated data file (created on first run)
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/CodewithAwais05/Python-Projects.git
   ```
2. Navigate to the project folder:
   ```bash
   cd "Python-Projects/Bank Management System"
   ```
3. Run the script:
   ```bash
   python bank_management.py
   ```

## Usage

On launch, you'll see the main menu:

```
1. Admin Login
2. Customer Login
3. Exit
```

### Admin Login

Use the default admin credentials:
- **Username:** `awais123`
- **Password:** `awais@123`

> ⚠️ **Security Note:** These credentials are hardcoded in the source file for demo purposes. If you plan to deploy or share this project publicly, move credentials to an environment variable or a separate config file, and avoid committing real credentials to version control.

From the admin menu, you can add customers, search accounts, and view all accounts.

### Customer Login

Customers log in with the username and password set up for them by the admin. From the customer menu, they can view their account, deposit/withdraw funds, update contact details, and change their password.

## Sample Data Format (`bank_data.json`)

```json
{
    "1001": {
        "name": "John Doe",
        "account_no": "1001",
        "username": "johnd",
        "password": "pass123",
        "email": "john@example.com",
        "phone_no": "03001234567",
        "balance": 5000.0
    }
}
```

## Known Limitations / Ideas for Improvement

- Passwords are stored in plain text — consider hashing them (e.g., with `hashlib` or `bcrypt`) for real-world use
- No input validation for empty fields or malformed email/phone formats
- No transaction history / statement generation
- Admin credentials are hardcoded rather than configurable

## Author

**Awais Raza**

## License

This project is open source and available for learning purposes. Feel free to fork and modify it.