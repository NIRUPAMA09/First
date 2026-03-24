import json
import os
from datetime import date

# -------------------- Book --------------------
class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "quantity": self.quantity
        }

    @staticmethod
    def from_dict(d):
        return Book(d["book_id"], d["title"], d["author"], d["quantity"])


# -------------------- Student --------------------
class Student:
    def __init__(self, student_id, name, dept, issued_books=None):
        self.student_id = student_id
        self.name = name
        self.dept = dept
        self.issued_books = issued_books if issued_books else []

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "dept": self.dept,
            "issued_books": self.issued_books
        }

    @staticmethod
    def from_dict(d):
        return Student(d["student_id"], d["name"], d["dept"], d.get("issued_books", []))


# -------------------- Issue Record --------------------
class IssueRecord:
    def __init__(self, student_id, book_id, issue_date, return_date=None):
        self.student_id = student_id
        self.book_id = book_id
        self.issue_date = issue_date
        self.return_date = return_date

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "book_id": self.book_id,
            "issue_date": self.issue_date,
            "return_date": self.return_date
        }

    @staticmethod
    def from_dict(d):
        return IssueRecord(d["student_id"], d["book_id"], d["issue_date"], d["return_date"])


# -------------------- Library --------------------
class Library:
    def __init__(self):
        self.books = []
        self.students = []
        self.issues = []

        self.load_books()
        self.load_students()
        self.load_issues()

    # ---------- Books ----------
    def save_books(self):
        data = [b.to_dict() for b in self.books]
        with open("books.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_books(self):
        if os.path.exists("books.json"):
            with open("books.json", "r") as f:
                try:
                    data = json.load(f)
                    self.books = [Book.from_dict(x) for x in data]
                except json.JSONDecodeError:
                    self.books = []
        else:
            self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.book_id == book.book_id:
                return False, "Book ID already exists."
        self.books.append(book)
        self.save_books()
        return True, "Book added successfully."

    def view_books(self):
        return self.books

    def search_book(self, keyword):
        result = []
        keyword = keyword.lower()
        for b in self.books:
            if keyword in b.title.lower() or keyword in b.author.lower() or keyword in b.book_id.lower():
                result.append(b)
        return result

    # ---------- Students ----------
    def save_students(self):
        data = [s.to_dict() for s in self.students]
        with open("students.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_students(self):
        if os.path.exists("students.json"):
            with open("students.json", "r") as f:
                try:
                    data = json.load(f)
                    self.students = [Student.from_dict(x) for x in data]
                except json.JSONDecodeError:
                    self.students = []
        else:
            self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.student_id == student.student_id:
                return False, "Student ID already exists."
        self.students.append(student)
        self.save_students()
        return True, "Student added successfully."

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    # ---------- Issues ----------
    def save_issues(self):
        data = [i.to_dict() for i in self.issues]
        with open("issues.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_issues(self):
        if os.path.exists("issues.json"):
            with open("issues.json", "r") as f:
                try:
                    data = json.load(f)
                    self.issues = [IssueRecord.from_dict(x) for x in data]
                except json.JSONDecodeError:
                    self.issues = []
        else:
            self.issues = []

    def issue_book_to_student(self, student_id, book_id, max_books=3):
        student = self.find_student(student_id)
        if not student:
            return False, "Student not found."

        if len(student.issued_books) >= max_books:
            return False, "Student has reached max issued books limit."

        for book in self.books:
            if book.book_id == book_id:
                if book.quantity <= 0:
                    return False, "Book not available."

                # Issue book
                book.quantity -= 1
                student.issued_books.append(book_id)
                record = IssueRecord(student_id, book_id, str(date.today()), None)
                self.issues.append(record)

                self.save_books()
                self.save_students()
                self.save_issues()
                return True, "Book issued successfully."

        return False, "Book not found."

    def return_book_from_student(self, student_id, book_id):
        student = self.find_student(student_id)
        if not student:
            return False, "Student not found."

        if book_id not in student.issued_books:
            return False, "This book was not issued to this student."

        # Increase book quantity
        for book in self.books:
            if book.book_id == book_id:
                book.quantity += 1
                break

        # Update student
        student.issued_books.remove(book_id)

        # Update issue record
        for rec in self.issues:
            if rec.student_id == student_id and rec.book_id == book_id and rec.return_date is None:
                rec.return_date = str(date.today())
                break

        self.save_books()
        self.save_students()
        self.save_issues()
        return True, "Book returned successfully."

    def view_issues(self):
        return self.issues
