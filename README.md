# Library Management System (CLI)

A simple command-line Python application to manage a library’s books and members using CSV files.

---

## Features

- Add new books with auto-incremented BookIDs  
- Add new members with auto-incremented MemberIDs  
- View all books and members  
- Search books or members by their ID  
- Issue books to members  
- Return books from members  
- Remove books or members  
- Data persistence using CSV files  

---

## Requirements

- Python 3.x

---

## Setup & Running

1. Clone or download this repository  
2. Make sure `Library.csv` and `Member.csv` exist with proper headers, or run the program to create and add entries  
3. Run the script:
python library_management.py

Follow the on-screen menu prompts to use the system


## How It Works
IDs (BookID, MemberID) are automatically generated based on existing CSV data, so they persist across runs

Books and members are stored in separate CSV files

Issuing or returning books updates the status and links books to member IDs

Removing records rewrites CSV files without the removed entries


**Usage**
On running the script, you'll see a menu like:


1. Add Book  
2. Add Member  
3. Print Info  
4. Issue Book  
5. Remove Book/Member  
6. Return Book  
7. Exit  
Choose options by entering the number, and follow prompts for details.

## Notes
**All IDs are handled as strings internally to avoid conversion issues**

**CSV files must have the following headers:**

Library.csv
BookID,Title,Author,Year,Status,Issued_To_ID

Member.csv
MemberID,Name

Book statuses: "Available" or "Issued"

Example
mathematics
Enter Choice : 2  
Enter Name: John Doe  
Member Added Successfully!

Enter Choice : 1  
Enter Book Title: Python 101  
Enter Author Name: Jane Smith  
Enter Year: 2020  
Enter ID of member the book was issued to(Optional Leave 0 if issued to none) : 0  
Book Added Successfully!

Enter Choice : 4  
Enter Book Id: 1  
Enter Member Id: 1  
Book issued successfully.


# Happy managing!


