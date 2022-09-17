from logging import exception
from typing import Final

# from itsdangerous import exc


class Library:
    def Borrow(self,a):
        with open("Student_Records.txt","a+") as f:
            f.write(f"\n{a} book is borrowed")
            print("Book borrowed!!!")
    # def List(self,books):
    #     print("Avialable Books are: ")
    #     for i, item in enumerate (books): 
    #          print(f"\n {i} ".join(books))    
    def Return(self,a):
        with open("Student_Records.txt","a+") as f:
            f.write(f"\n{a} book is returned")
            print("Book is returned!!!")
class Student:
    def __init__(self) -> None:
        a = input("Enter your name: ")
        b = int(input("Enter your Enrollment Number: "))
        self.name = a 
        self.Enumber = str(b)
        with open("Student_Records.txt","a+") as f:
            f.write(f"\n\nName: {self.name}     Enrollment Number: {self.Enumber}")


kong = Library()
Books = ["Ramayanam", "Mahabharat","Bhagavat Gita","Shiva Mahapuranam","Devi Bhagavatam"]
Borrowed = []
while True:
    try:
        
        print("********************Welcome to Student Library********************")
        a = input("Do you want to enter: \n(y/n)")
        if a == "y":
            k = Student()
            while True:
                a = int(input("********************MENU********************\n1. List of Books\n2. Borrow a Book\n3. Return Book\n4. Quit\n"))
                if a == 1:
                    if Books:
                        print("The books available are: \n")
                        for ji, item in enumerate(Books):
                            print(ji+1,item)
                    else:
                        print("No books are available")
                elif a == 2:
                    if Books:
                        print("Select one of the following books: ")
                        for ji, item in enumerate(Books):
                            print(ji+1,item)
                        i = int(input(""))
                        z = Books.pop(i-1)
                        Borrowed.append(z)
                        kong.Borrow(z)
                    else:
                        print("No books available to borrow")
                elif a == 3:
                    if Borrowed:
                        print("Books to be returned are: ")
                        for ji, item in enumerate(Borrowed):
                            print(ji+1,item)
                        i = int(input(""))
                        z = Borrowed.pop(i-1)
                        Books.append(z)
                        kong.Return(z)
                    else:
                        print("No books are currently borrowed")
                elif a == 4:
                    break
        elif a == "n":
                    break
    
    except ValueError as e:
        print("Invalid option")
    except ZeroDivisionError as e:
        print("Infinity`")
    except exception as e:
        print("An error Occured")