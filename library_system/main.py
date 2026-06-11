from library_system.library import Library


def main():

    library = Library()

    library.load_data()

    while True:

        print("\n" + "=" * 40)
        print("     LIBRARY MANAGEMENT SYSTEM")
        print("=" * 40)

        print("1. Add New Book")
        print("2. Register New Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. View All Books")
        print("7. View All Members")
        print("8. View Overdue Books")
        print("9. Save & Exit")
        print("0. Exit Without Saving")

        choice = input(
            "\nEnter your choice: "
        )

        # ---------------- ADD BOOK ----------------

        if choice == "1":

            title = input(
                "Enter Title: "
            )

            author = input(
                "Enter Author: "
            )

            isbn = input(
                "Enter ISBN: "
            )

            year = input(
                "Enter Year: "
            )

            library.add_book(
                title,
                author,
                isbn,
                year
            )

        # ---------------- REGISTER MEMBER ----------------

        elif choice == "2":

            name = input(
                "Enter Member Name: "
            )

            member_id = input(
                "Enter Member ID: "
            )

            library.register_member(
                name,
                member_id
            )

        # ---------------- BORROW BOOK ----------------

        elif choice == "3":

            isbn = input(
                "Enter ISBN: "
            )

            member_id = input(
                "Enter Member ID: "
            )

            library.borrow_book(
                isbn,
                member_id
            )

        # ---------------- RETURN BOOK ----------------

        elif choice == "4":

            isbn = input(
                "Enter ISBN: "
            )

            library.return_book(
                isbn
            )

        # ---------------- SEARCH BOOK ----------------

        elif choice == "5":

            print("\nSearch By")
            print("1. Title")
            print("2. Author")
            print("3. ISBN")

            search_choice = input(
                "Enter Choice: "
            )

            keyword = input(
                "Enter Search Value: "
            )

            if search_choice == "1":

                results = (
                    library.search_by_title(
                        keyword
                    )
                )

            elif search_choice == "2":

                results = (
                    library.search_by_author(
                        keyword
                    )
                )

            elif search_choice == "3":

                results = (
                    library.search_by_isbn(
                        keyword
                    )
                )

            else:

                print(
                    "Invalid choice."
                )

                continue

            if results:

                for book in results:
                    print(book)

            else:

                print(
                    "No books found."
                )

        # ---------------- VIEW BOOKS ----------------

        elif choice == "6":

            library.view_books()

        # ---------------- VIEW MEMBERS ----------------

        elif choice == "7":

            library.view_members()

        # ---------------- OVERDUE ----------------

        elif choice == "8":

            library.view_overdue_books()

        # ---------------- SAVE & EXIT ----------------

        elif choice == "9":

            library.save_data()

            library.backup_data()

            print(
                "\nData saved successfully."
            )

            print(
                "Goodbye!"
            )

            break

        # ---------------- EXIT ----------------

        elif choice == "0":

            print(
                "\nExited without saving."
            )

            break

        else:

            print(
                "Invalid choice."
            )


if __name__ == "__main__":
    main()