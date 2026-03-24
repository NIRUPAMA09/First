import tkinter as tk
from tkinter import ttk, messagebox
from backend import Library, Book, Student
from datetime import date

lib = Library()

root = tk.Tk()
root.title("Library Management System")
root.geometry("900x600")

#ADD BOOK
def add_book_window():
    win = tk.Toplevel(root)
    win.title("Add Book")

    tk.Label(win,text="Book ID").grid(row=0,column=0)
    tk.Label(win,text="Title").grid(row=1,column=0)
    tk.Label(win,text="Author").grid(row=2,column=0)
    tk.Label(win,text="Quantity").grid(row=3,column=0)

    id_entry=tk.Entry(win)
    title_entry=tk.Entry(win)
    author_entry=tk.Entry(win)
    qty_entry=tk.Entry(win)

    id_entry.grid(row=0,column=1)
    title_entry.grid(row=1,column=1)
    author_entry.grid(row=2,column=1)
    qty_entry.grid(row=3,column=1)

    def add_book():
        book=Book(
            id_entry.get(),
            title_entry.get(),
            author_entry.get(),
            int(qty_entry.get())
        )

        ok,msg=lib.add_book(book)

        if ok:
            messagebox.showinfo("Success",msg)
        else:
            messagebox.showerror("Error",msg)

    tk.Button(win,text="Add Book",command=add_book).grid(row=4,column=1)

# VIEW BOOKS
def view_books():
    win=tk.Toplevel(root)
    win.title("Books")

    cols=("ID","Title","Author","Quantity")

    table=ttk.Treeview(win,columns=cols,show="headings")

    for c in cols:
        table.heading(c,text=c)

    table.pack(fill="both",expand=True)

    for b in lib.view_books():
        table.insert("",tk.END,values=(b.book_id,b.title,b.author,b.quantity))

# SEARCH BOOK
def search_book():
    win=tk.Toplevel(root)
    win.title("Search Book")

    tk.Label(win,text="Keyword").pack()

    entry=tk.Entry(win)
    entry.pack()

    cols=("ID","Title","Author","Quantity")
    table=ttk.Treeview(win,columns=cols,show="headings")

    for c in cols:
        table.heading(c,text=c)

    table.pack(fill="both",expand=True)

    def search():
        table.delete(*table.get_children())

        result=lib.search_book(entry.get())

        for b in result:
            table.insert("",tk.END,values=(b.book_id,b.title,b.author,b.quantity))

    tk.Button(win,text="Search",command=search).pack()

# ADD STUDENT
def add_student_window():

    win=tk.Toplevel(root)
    win.title("Add Student")

    tk.Label(win,text="Student ID").grid(row=0,column=0)
    tk.Label(win,text="Name").grid(row=1,column=0)
    tk.Label(win,text="Department").grid(row=2,column=0)

    sid=tk.Entry(win)
    name=tk.Entry(win)
    dept=tk.Entry(win)

    sid.grid(row=0,column=1)
    name.grid(row=1,column=1)
    dept.grid(row=2,column=1)

    def add_student():

        s=Student(sid.get(),name.get(),dept.get())

        ok,msg=lib.add_student(s)

        if ok:
            messagebox.showinfo("Success",msg)
        else:
            messagebox.showerror("Error",msg)

    tk.Button(win,text="Add Student",command=add_student).grid(row=3,column=1)

# VIEW STUDENTS
def view_students():

    win=tk.Toplevel(root)
    win.title("Students")

    cols=("ID","Name","Department","Issued Books")

    table=ttk.Treeview(win,columns=cols,show="headings")

    for c in cols:
        table.heading(c,text=c)

    table.pack(fill="both",expand=True)

    for s in lib.students:
        table.insert("",tk.END,values=(s.student_id,s.name,s.dept,len(s.issued_books)))

# ISSUE BOOK
def issue_book_window():

    win=tk.Toplevel(root)
    win.title("Issue Book")

    tk.Label(win,text="Student ID").grid(row=0,column=0)
    tk.Label(win,text="Student Name").grid(row=1,column=0)
    tk.Label(win,text="Book ID").grid(row=2,column=0)
    tk.Label(win,text="Book Title").grid(row=3,column=0)
    tk.Label(win,text="Issue Date").grid(row=4,column=0)
    tk.Label(win,text="Due Date").grid(row=5,column=0)
    tk.Label(win,text="Issued By").grid(row=6,column=0)

    sid=tk.Entry(win)
    sname=tk.Entry(win)
    bid=tk.Entry(win)
    btitle=tk.Entry(win)
    issue_date=tk.Entry(win)
    due_date=tk.Entry(win)
    issued_by=tk.Entry(win)

    sid.grid(row=0,column=1)
    sname.grid(row=1,column=1)
    bid.grid(row=2,column=1)
    btitle.grid(row=3,column=1)
    issue_date.grid(row=4,column=1)
    due_date.grid(row=5,column=1)
    issued_by.grid(row=6,column=1)

    issue_date.insert(0,str(date.today()))

    def issue():

        ok,msg=lib.issue_book_to_student(
            sid.get(),
            bid.get()
        )

        if ok:
            messagebox.showinfo("Success",msg)
        else:
            messagebox.showerror("Error",msg)

    tk.Button(win,text="Issue Book",command=issue).grid(row=7,column=1)

# RETURN BOOK
def return_book_window():

    win=tk.Toplevel(root)
    win.title("Return Book")

    tk.Label(win,text="Student ID").grid(row=0,column=0)
    tk.Label(win,text="Book ID").grid(row=1,column=0)
    tk.Label(win,text="Return Date").grid(row=2,column=0)

    sid=tk.Entry(win)
    bid=tk.Entry(win)
    rdate=tk.Entry(win)

    sid.grid(row=0,column=1)
    bid.grid(row=1,column=1)
    rdate.grid(row=2,column=1)

    rdate.insert(0,str(date.today()))

    def return_book():

        ok,msg=lib.return_book_from_student(
            sid.get(),
            bid.get()
        )

        if ok:
            messagebox.showinfo("Returned",msg)
        else:
            messagebox.showerror("Error",msg)

    tk.Button(win,text="Return Book",command=return_book).grid(row=3,column=1)

# VIEW ISSUE RECORDS
def view_issues():

    win=tk.Toplevel(root)
    win.title("Issue Records")

    cols=("Student ID","Book ID","Issue Date","Return Date")

    table=ttk.Treeview(win,columns=cols,show="headings")

    for c in cols:
        table.heading(c,text=c)

    table.pack(fill="both",expand=True)

    for i in lib.view_issues():
        table.insert("",tk.END,values=(
            i.student_id,
            i.book_id,
            i.issue_date,
            i.return_date
        ))

# MAIN MENU BUTTONS
tk.Label(root,text="Library Management System",
         font=("Arial",20)).pack(pady=20)

tk.Button(root,text="Add Book",width=20,command=add_book_window).pack(pady=5)
tk.Button(root,text="View Books",width=20,command=view_books).pack(pady=5)
tk.Button(root,text="Search Book",width=20,command=search_book).pack(pady=5)

tk.Button(root,text="Add Student",width=20,command=add_student_window).pack(pady=5)
tk.Button(root,text="View Students",width=20,command=view_students).pack(pady=5)

tk.Button(root,text="Issue Book",width=20,command=issue_book_window).pack(pady=5)
tk.Button(root,text="Return Book",width=20,command=return_book_window).pack(pady=5)

tk.Button(root,text="View Issue Records",width=20,command=view_issues).pack(pady=5)

tk.Button(root,text="Exit",width=20,command=root.quit).pack(pady=20)

root.mainloop()