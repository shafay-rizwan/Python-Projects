# import time as t

# class ExpenseTracker():
#     def __init__(self):
#         self.expenses = [] # empty list to store expenses, name, amount, category

# # method for storing the expense in the list
#     def add_expense(self, expense_name, expense_amount, expense_category):
#         try:
#             expense_amount = float(expense_amount) # Checking the validation is of the numeric value
#             expense = {'expense_name' : expense_name, 'expense_amount' : expense_amount, 'expense_category' : expense_category } # Dictionary for expenses key value 
#             self.expenses.append(expense) # append to the empty list 
#             print(f"Expense Added: {expense}")
#         except:
#             print(f"Invalid number for amount ! {expense_amount} ")

# # method for viewing all the expenses inside our self.expenses lists
#     def view_all_expenses(self):

#         if not self.expenses:
#             print("No expenses available !")
#         else:
#             print("\nAll Expenses:")
#             for idx, expense in enumerate(self.expenses, start=1):
#                 print(f"{idx}. {expense['expense_name']} - ${expense['expense_amount']}, {expense['expense_ncategory']}")

# # method for calculating the total 
#     def calculate_total_expenses(self):
#         if not self.expenses:
#             print("There is no expense to calculate: ")
#         else:
#             print(f"Calculating Total Expenses....... 'Please Wait'\n")
#             t.sleep(10)
#             total = sum(expense['expense_amount'] for expense in self.expenses )
#             print(f"The sum of all the expenses are {total}")

# def filter_expenses_by_category(self, category):
#     # Create an empty list to store filtered expenses
#     filtered_expenses = []

#     # Loop through each expense in the list
#     for expense in self.expenses:
#         # Check if the expense's category matches the input category (case insensitive)
#         if expense["category"].lower() == category.lower():
#             filtered_expenses.append(expense)  # Add the expense to the filtered list

#     # Check if no expenses were found in the specified category
#     if not filtered_expenses:
#         print(f"No expenses found in the category: {category}")
#     else:
#         # Print the filtered expenses
#         print(f"\nExpenses in category '{category} ............ processing")
#         t.sleep(10)
#         for expense in filtered_expenses:
#             print(f"{expense['name']} - ${expense['amount']}")


# expense_tracker = ExpenseTracker() # instance of class ExpenseTracker for calling methods of this class

# # Menu for the Expense Tracker
# while True:
#     print("\nWelcome to the Expense Tracker!")
#     print("1. Add Expense")
#     print("2. View All Expenses")
#     print("3. Calculate Total Expenses")
#     print("4. Filter Expenses by Category")
#     print("5. Exit")

#     user_input = input("Choose an option: ")

#     if user_input == "1":
#         # Add expense option
#         name = input("Enter the name of the expense: ")
#         amount = input("Enter the amount: ")
#         category = input("Enter the category: ")
#         expense_tracker.add_expense(name, amount, category)

#     elif user_input == "2":
#         # View all expenses option
#         expense_tracker.view_all_expenses()

#     elif user_input == "3":
#         # Calculate total expenses option
#         expense_tracker.calculate_total_expenses()

#     elif user_input == "4":
#         # Filter expenses by category option
#         category = input("Enter the category to filter: ")
#         expense_tracker.filter_expenses_by_category(category)

#     elif user_input == "5":
#         # Exit the program
#         print("Thank you for using the Expense Tracker. Goodbye!")
#         break

#     else:
#         print("Invalid input. Please try again.")

# >>>>>>>>>>>>>>>> CHAT GPT PROMPT <<<<<<<<<<<<<<<<<<<<

class ExpenseTracker:
    # Initialize the tracker with an empty list for expenses
    def __init__(self):
        self.expenses = []  # List to store all expenses

    # Add a new expense
    def add_expense(self, name, amount, category):
        try:
            amount = float(amount)  # Ensure amount is a valid number
            expense = {"name": name, "amount": amount, "category": category}
            self.expenses.append(expense)  # Add expense to the list
            print(f"Expense added successfully: {expense}")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    # View all expenses
    def view_all_expenses(self):
        if not self.expenses:
            print("No expenses added yet.")
        else:
            print("\nAll Expenses:")
            for idx, expense in enumerate(self.expenses, start=1):
                print(f"{idx}. {expense['name']} - ${expense['amount']} ({expense['category']})")

    # Calculate total expenses
    def calculate_total_expenses(self):
        if not self.expenses:
            print("No expenses to calculate.")
        else:
            total = sum(expense["amount"] for expense in self.expenses)
            print(f"The total of all expenses is: ${total}")

    # Filter expenses by category
    def filter_expenses_by_category(self, category):
        filtered_expenses = [exp for exp in self.expenses if exp["category"].lower() == category.lower()]
        if not filtered_expenses:
            print(f"No expenses found in the category: {category}")
        else:
            print(f"\nExpenses in category '{category}':")
            for expense in filtered_expenses:
                print(f"{expense['name']} - ${expense['amount']}")

# Create an instance of the ExpenseTracker class
expense_tracker = ExpenseTracker()

# Menu for the Expense Tracker
while True:
    print("\nWelcome to the Expense Tracker!")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Expenses")
    print("4. Filter Expenses by Category")
    print("5. Exit")

    user_input = input("Choose an option: ")

    if user_input == "1":
        # Add expense option
        name = input("Enter the name of the expense: ")
        amount = input("Enter the amount: ")
        category = input("Enter the category: ")
        expense_tracker.add_expense(name, amount, category)

    elif user_input == "2":
        # View all expenses option
        expense_tracker.view_all_expenses()

    elif user_input == "3":
        # Calculate total expenses option
        expense_tracker.calculate_total_expenses()

    elif user_input == "4":
        # Filter expenses by category option
        category = input("Enter the category to filter: ")
        expense_tracker.filter_expenses_by_category(category)

    elif user_input == "5":
        # Exit the program
        print("Thank you for using the Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid input. Please try again.")
