# Databricks notebook source
from book_manager import *

def show_menu():
    while True:
        print('=== Library Management System ===')
        print('1. Add Book')
        print('2. Search Books')
        print('3. View All Books')
        print('4. Delete a Book')
        print('5. Exit')
        choice = input('Enter your choice (1-5):')

        if choice == '1':
            add_book()
        elif choice == '2':
            search_book()       
        elif choice == '3':
            view_books()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            break
        else: 
            print('Invalid choice. Try again')
        input('\n Press Enter to Continue')

if __name__ == '__main__':
    show_menu()

# COMMAND ----------

class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
r1 = Rectangle(10, 20)
r2 = Rectangle(30, 40)
print(r1.area())   
print(r2.perimeter())