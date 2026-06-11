import json
import shutil
from library_system.book import Book
from library_system.member import Member


class Library:

    def __init__(self):
        self.books = {}
        self.members = {}

    # ---------------- BOOKS ----------------

    def add_book(self, title, author, isbn, year):

        if isbn in self.books:
            print("Book already exists.")
            return

        self.books[isbn] = Book(
            title,
            author,
            isbn,
            year
        )

        print("Book added successfully.")

    def remove_book(self, isbn):

        if isbn not in self.books:
            print("Book not found.")
            return

        del self.books[isbn]

        print("Book removed successfully.")

    def find_book(self, isbn):

        return self.books.get(isbn)

    # ---------------- MEMBERS ----------------

    def register_member(
        self,
        name,
        member_id
    ):

        if member_id in self.members:
            print("Member already exists.")
            return

        self.members[member_id] = Member(
            name,
            member_id
        )

        print(
            "Member registered successfully."
        )

    def find_member(self, member_id):

        return self.members.get(member_id)

    # ---------------- BORROW ----------------

    def borrow_book(
        self,
        isbn,
        member_id
    ):

        book = self.find_book(isbn)

        if not book:
            print("Book not found.")
            return

        member = self.find_member(member_id)

        if not member:
            print("Member not found.")
            return

        if not member.can_borrow():
            print(
                "Borrow limit reached."
            )
            return

        success, message = book.check_out(
            member_id
        )

        if success:
            member.borrow_book(isbn)

        print(message)

    # ---------------- RETURN ----------------

    def return_book(self, isbn):

        book = self.find_book(isbn)

        if not book:
            print("Book not found.")
            return

        if book.available:
            print(
                "Book already available."
            )
            return

        member = self.find_member(
            book.borrowed_by
        )

        if member:
            member.return_book(isbn)

        success, message = (
            book.return_book()
        )

        print(message)

    # ---------------- SEARCH ----------------

    def search_by_title(
        self,
        keyword
    ):

        results = []

        for book in self.books.values():

            if keyword.lower() in (
                book.title.lower()
            ):
                results.append(book)

        return results

    def search_by_author(
        self,
        keyword
    ):

        results = []

        for book in self.books.values():

            if keyword.lower() in (
                book.author.lower()
            ):
                results.append(book)

        return results

    def search_by_isbn(
        self,
        isbn
    ):

        if isbn in self.books:
            return [self.books[isbn]]

        return []

    # ---------------- VIEW ----------------

    def view_books(self):

        if not self.books:
            print("No books found.")
            return

        for book in self.books.values():
            print(book)

    def view_members(self):

        if not self.members:
            print("No members found.")
            return

        for member in self.members.values():
            print(member)

    # ---------------- OVERDUE ----------------

    def view_overdue_books(self):

        found = False

        for book in self.books.values():

            if book.is_overdue():

                found = True

                print(
                    f"{book.title} | "
                    f"{book.days_overdue()} "
                    f"days overdue"
                )

        if not found:
            print(
                "No overdue books found."
            )

    # ---------------- STATISTICS ----------------

    def show_statistics(self):

        total_books = len(self.books)

        available_books = sum(
            1
            for book in self.books.values()
            if book.available
        )

        borrowed_books = (
            total_books
            - available_books
        )

        print("\nLibrary Statistics")
        print("-" * 25)

        print(
            f"Total Books: "
            f"{total_books}"
        )

        print(
            f"Available Books: "
            f"{available_books}"
        )

        print(
            f"Borrowed Books: "
            f"{borrowed_books}"
        )

        print(
            f"Members: "
            f"{len(self.members)}"
        )

    # ---------------- SAVE ----------------

    def save_data(self):

        books_data = [
            book.to_dict()
            for book in self.books.values()
        ]

        members_data = [
            member.to_dict()
            for member in self.members.values()
        ]

        with open(
            "data/books.json",
            "w"
        ) as file:

            json.dump(
                books_data,
                file,
                indent=4
            )

        with open(
            "data/members.json",
            "w"
        ) as file:

            json.dump(
                members_data,
                file,
                indent=4
            )

        print(
            "Data saved successfully."
        )

    # ---------------- LOAD ----------------

    def load_data(self):

        try:

            with open(
                "data/books.json",
                "r"
            ) as file:

                books_data = (
                    json.load(file)
                )

            for item in books_data:

                book = (
                    Book.from_dict(item)
                )

                self.books[
                    book.isbn
                ] = book

        except:
            pass

        try:

            with open(
                "data/members.json",
                "r"
            ) as file:

                members_data = (
                    json.load(file)
                )

            for item in members_data:

                member = (
                    Member.from_dict(item)
                )

                self.members[
                    member.member_id
                ] = member

        except:
            pass

    # ---------------- BACKUP ----------------

    def backup_data(self):

        try:

            shutil.copy(
                "data/books.json",
                "data/backup/books_backup.json"
            )

            shutil.copy(
                "data/members.json",
                "data/backup/members_backup.json"
            )

            print(
                "Backup created successfully."
            )

        except:

            print(
                "Backup failed."
            )