from datetime import datetime, timedelta


class Book:

    def __init__(self, title, author, isbn, year=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

        self.available = True
        self.borrowed_by = None
        self.due_date = None

        self.date_added = datetime.now().strftime("%Y-%m-%d")

    def check_out(self, member_id, loan_period=14):

        if not self.available:
            return False, "Book is already borrowed."

        self.available = False
        self.borrowed_by = member_id

        due = datetime.now() + timedelta(days=loan_period)

        self.due_date = due.strftime("%Y-%m-%d")

        return True, f"Book issued successfully. Due Date: {self.due_date}"

    def return_book(self):

        if self.available:
            return False, "Book is already available."

        overdue = self.is_overdue()

        self.available = True
        self.borrowed_by = None
        self.due_date = None

        if overdue:
            return True, "Book returned (Overdue)."

        return True, "Book returned successfully."

    def is_overdue(self):

        if self.available:
            return False

        if not self.due_date:
            return False

        due = datetime.strptime(
            self.due_date,
            "%Y-%m-%d"
        )

        return datetime.now() > due

    def days_overdue(self):

        if not self.is_overdue():
            return 0

        due = datetime.strptime(
            self.due_date,
            "%Y-%m-%d"
        )

        return (
            datetime.now() - due
        ).days

    def to_dict(self):

        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "available": self.available,
            "borrowed_by": self.borrowed_by,
            "due_date": self.due_date,
            "date_added": self.date_added
        }

    @classmethod
    def from_dict(cls, data):

        book = cls(
            data["title"],
            data["author"],
            data["isbn"],
            data.get("year")
        )

        book.available = data.get(
            "available",
            True
        )

        book.borrowed_by = data.get(
            "borrowed_by"
        )

        book.due_date = data.get(
            "due_date"
        )

        book.date_added = data.get(
            "date_added",
            datetime.now().strftime("%Y-%m-%d")
        )

        return book

    def __str__(self):

        if self.available:
            status = "Available"
        else:
            status = (
                f"Borrowed by "
                f"{self.borrowed_by} "
                f"(Due: {self.due_date})"
            )

        return (
            f"{self.title} | "
            f"{self.author} | "
            f"ISBN: {self.isbn} | "
            f"{status}"
        )