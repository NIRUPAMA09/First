Library Management System (Python)
A complete **Library Management System** developed using **Python**, implementing **Object-Oriented Programming (OOP)** and **file handling (JSON)**.
The project provides both **console-based and GUI-based interfaces** for efficient library operations.

Features:
* Add, view, and search books
* Manage student records
* Issue books to students
* Return books with tracking
* View issue/return history
* Persistent data storage using JSON
* Dual interface:
  * Console-based (CLI)
  * GUI-based (Tkinter)

Tech Stack

* Language: Python
* Programming Paradigm: Object-Oriented Programming (OOP)
* GUI Framework: Tkinter
* Data Storage: JSON (File Handling)
* Libraries Used:
  * tkinter
  * json
  * datetime
  * os

Project Structure

```
LibraryManagementSystem/
│
├── backend.py          # Core logic (OOP + file handling)
├── console_app.py      # Console-based interface
├── gui.py              # Tkinter GUI application
│
├── books.json          # Book data storage
├── students.json       # Student data storage
└── issues.json         # Issue records
```

Installation & Setup:

Clone the Repository

```
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```
Run the Project

Run Console Version

```
python console_app.py
```

Run GUI Version

```
python gui.py
```

System Architecture:

The project follows a **modular layered architecture**:

```
GUI / Console Interface
        ↓
   Backend Logic (OOP)
        ↓
   JSON File Storage
```

Functional Workflow

1. User interacts through GUI or console
2. Input is passed to backend classes
3. Backend processes logic (add/search/issue/return)
4. Data is stored/retrieved from JSON files
5. Output is displayed to the user

Key Concepts Implemented

* Object-Oriented Programming (Classes & Objects)
* Encapsulation and modular design
* File handling using JSON
* Event-driven programming (Tkinter GUI)
* Data validation and error handling

Limitations

* Uses file-based storage instead of a database
* No authentication system
* Single-user desktop application

Future Enhancements

* User authentication (Admin/Student login)
* Database integration (MySQL / SQLite)
* Web-based version (Flask/Django)
* Fine calculation system
* Report generation


Author

* Nirupama Sahu

Acknowledgement

This project was developed as part of a **B.Tech 6th Semester academic mini project**, focusing on practical implementation of OOP and file handling concepts in Python.

