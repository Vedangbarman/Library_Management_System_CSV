import os 
import csv

bookid = 1
memberid = 1 


import csv

def get_next_book_id():
    max_id = 0
    try:
        with open("Library.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                current_id = int(row['BookID'])
                if current_id > max_id:
                    max_id = current_id
    except FileNotFoundError:
        max_id = 0
    return max_id + 1

def get_next_member_id():
    max_id = 0
    try:
        with open("Member.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                current_id = int(row['MemberID'])
                if current_id > max_id:
                    max_id = current_id
    except FileNotFoundError:
        max_id = 0
    return max_id + 1

bookid = get_next_book_id()
memberid = get_next_member_id()



def create_book_table():
    file = open("Library.csv","w")
    writer = csv.writer(file)
    writer.writerow(['BookID','Title','Author','Year','Status','Issued_To_ID'])
    file.close()

def create_member_table():
    file = open("Member.csv","w")
    writer = csv.writer(file)
    writer.writerow(['MemberID','Name'])
    file.close()


def add_member():
    global memberid

    name=input("Enter Name")

    file = open("Member.csv","a")
    writer = csv.writer(file)
    writer.writerow([memberid,name])

    print("Member Added Successfully!")

    memberid += 1

    file.close()

def add_book():
    global bookid

    title = input("Enter Book Title")
    author = input("Enter Author Name")
    year = int(input("Enter Year"))
    Issued_To_ID = int(input("Enter ID of member the book was issued to(Optional Leave 0 if issued to none) : "))
    if Issued_To_ID == '' or Issued_To_ID == '0':
        Issued_To_ID = '0'
    file = open("Library.csv","a")
    writer = csv.writer(file)
    writer.writerow([bookid,title,author,year,'Available',Issued_To_ID])

    print("Book Added Succesfully!")
    bookid += 1

    file.close()


def print_info():
    print('''
1. Print All Members
2. Print All Books 
3. Print Members By ID
4. Print Books by ID
5. Print Issued Books
6. Exit
''')
    choice = int(input("Enter Choice :"))

    if choice == 1:
        with open("Member.csv", "r") as member_file:
            reader = csv.DictReader(member_file)
            for row in reader:
                print(row)

    elif choice == 2:
        with open("Library.csv", "r") as book_file:
            reader = csv.DictReader(book_file)
            for row in reader:
                print(row)

    elif choice == 3:
        member_id = input("Enter MemberID: ").strip()
        with open("Member.csv", "r") as member_file:
            reader = csv.DictReader(member_file)
            found = False
            for row in reader:
                if row['MemberID'] == member_id:
                    print(row)
                    found = True
            if not found:
                print("Member not found.")

    elif choice == 4:
        book_id = input("Enter BookID: ").strip()
        with open("Library.csv", "r") as book_file:
            reader = csv.DictReader(book_file)
            found = False
            for row in reader:
                if row['BookID'] == book_id:
                    print(row)
                    found = True
            if not found:
                print("Book not found.")

    elif choice == 5:
        with open("Library.csv", "r") as book_file:
            reader = csv.DictReader(book_file)
            issued_books = [row for row in reader if row['Status'] == 'Issued']
            if issued_books:
                for row in issued_books:
                    print(row)
            else:
                print("No books currently issued.")

    elif choice == 6:
        return

    else:
        print("Invalid choice!")


def remove():
    print('''
1. Remove Book
2. Remove Member
3. Exit
''')

    choice = int(input("Enter Choice: "))

    if choice == 1:
        book_id = input("Enter Book ID: ").strip()
        input_file = "Library.csv"
        temp_file = "Temp_Library.csv"

        with open(input_file, 'r', newline='') as infile, open(temp_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            rows_written = 0
            for row in reader:
                if row['BookID'] != book_id:
                    writer.writerow(row)
                    rows_written += 1

        # If number of rows written is less than original (excluding header), means a row was removed
        with open(input_file, 'r', newline='') as infile:
            total_rows = sum(1 for _ in infile) - 1  # subtract header

        if rows_written < total_rows:
            os.replace(temp_file, input_file)
            print("Book Removed")
        else:
            os.remove(temp_file)
            print("Book ID not found")

    elif choice == 2:
        member_id = input("Enter Member ID: ").strip()
        input_file = "Member.csv"
        temp_file = "Temp_Member.csv"

        with open(input_file, 'r', newline='') as infile, open(temp_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            rows_written = 0
            for row in reader:
                if row['MemberID'] != member_id:
                    writer.writerow(row)
                    rows_written += 1

        with open(input_file, 'r', newline='') as infile:
            total_rows = sum(1 for _ in infile) - 1

        if rows_written < total_rows:
            os.replace(temp_file, input_file)
            print("Member Removed")
        else:
            os.remove(temp_file)
            print("Member ID not found")

    elif choice == 3:
        return

    else:
        print("Invalid choice!")



def issue():
    book_id = input("Enter Book Id: ").strip()
    member_id = input("Enter Member Id: ").strip()

    book_found = False
    issued = False

    file = open("Library.csv", "r", newline='')
    temp = open("Library_temp.csv", "w", newline='')

    reader = csv.DictReader(file)
    writer = csv.DictWriter(temp, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        if row['BookID'] == book_id:
            book_found = True
            if row['Status'] == 'Issued':
                issued = True
                print("Book is already issued.")
            else:
                row['Status'] = 'Issued'
                row['Issued_To_ID'] = member_id
                print("Book issued successfully.")
        writer.writerow(row)

    file.close()
    temp.close()

    if not book_found:
        print("Book not found.")
    else:
        os.replace("Library_temp.csv", "Library.csv")


def return_book():
    import csv
    import os

    book_id = input("Enter Book Id: ").strip()
    member_id = input("Enter Member Id: ").strip()

    book_found = False
    book_already_available = False

    file = open("Library.csv", "r", newline='')
    temp = open("Library_temp.csv", "w", newline='')

    reader = csv.DictReader(file)
    writer = csv.DictWriter(temp, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        if row['BookID'] == book_id:
            book_found = True
            if row['Status'] == 'Available':
                book_already_available = True
                print("Book not issued!")
            else:
                # Check if the member returning is the one who issued it
                if row['Issued_To_ID'] == member_id:
                    row['Status'] = 'Available'
                    row['Issued_To_ID'] = '0'  # or blank string if you want
                    print("Book returned successfully.")
                else:
                    print("Book was issued to another member.")
        writer.writerow(row)

    file.close()
    temp.close()

    if not book_found:
        print("Book not found.")

    os.replace("Library_temp.csv", "Library.csv")



while True:
    print(''' 
1. Add Book
2. Add Member
3. Print Info
4. Issue Book 
5. Remove Book/Member
6. Return Book
7. Exit                    
''')
    choice = int(input("Enter Choice : "))

    if choice == 1:
        add_book()

    elif choice == 2:
        add_member()
    
    elif choice == 3:
        print_info()

    elif choice == 4:
        issue()

    elif choice == 5:
        remove()
    
    elif choice == 6:
        return_book()

    elif choice == 7:
        break

    else:
        print("Invalid Choice")








