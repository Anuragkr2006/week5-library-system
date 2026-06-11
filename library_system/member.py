class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

        self.borrowed_books = []

        self.max_books = 5

    def can_borrow(self):

        return len(
            self.borrowed_books
        ) < self.max_books

    def borrow_book(self, isbn):

        if not self.can_borrow():
            return (
                False,
                "Borrow limit reached."
            )

        if isbn in self.borrowed_books:
            return (
                False,
                "Book already borrowed."
            )

        self.borrowed_books.append(isbn)

        return (
            True,
            "Book added successfully."
        )

    def return_book(self, isbn):

        if isbn not in self.borrowed_books:
            return (
                False,
                "Book not found."
            )

        self.borrowed_books.remove(isbn)

        return (
            True,
            "Book returned successfully."
        )

    def to_dict(self):

        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):

        member = cls(
            data["name"],
            data["member_id"]
        )

        member.borrowed_books = data.get(
            "borrowed_books",
            []
        )

        return member

    def __str__(self):

        return (
            f"Name: {self.name} | "
            f"Member ID: {self.member_id} | "
            f"Borrowed Books: "
            f"{len(self.borrowed_books)}"
        )