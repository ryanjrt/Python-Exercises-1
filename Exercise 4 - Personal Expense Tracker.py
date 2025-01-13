#Design decisions:
# 1. Prompt user for inputs separately (1 question each for expense, amount, category)
# 2. Categories to be created free-form
# 3. Amounts to be standardised in USD (currency will be prompted)


# Create an expense
def create_expense():
    desc = input("Describe your expense: ")  
    
    try:
        input_amt = float(input("How much did you spend: "))
    except:
        print('Invalid input. Please input an amount.\n')
    
    while True:
        currency = input("What was the currency? Please use the ISO code (e.g. USD, GBP, EUR): ")
        if currency != "USD":
            try:
                amount = convert_usd(input_amt, currency)
                break
            except:
                print('ISO code is not valid!')
        else:
            amount = input_amt
            break
            
    category = input("Please classify this expense: ").strip()
    if not category.strip():
        print('Category cannot be empty. Please input category of expense.\n')    

    return {'Description': desc, 'Amount': amount, 'Currency': currency, 'Category': category} 

# Convert expense amount to standard USD currency (SELECTED PACKAGE NOT WORKING)
# def convert_usd(input_amt, currency):
#     from forex_python.converter import CurrencyRates
#     c = CurrencyRates()
#     fx_rate = c.get_rate(currency, "USD") #add currency in here
#     converted = input_amt * fx_rate
#     return converted
    
# Summarize expenses
def summarize_expenses(expense_list): #enter expense database as argument
    # get each category of expense
    
    summary_list = {}
    for expense in expense_list:
        d = expense['Category']
        if d in summary_list:
          summary_list[d] += expense['Amount']
        else:
          summary_list[d] = expense['Amount']  
          
    print(summary_list)
    # sum the amounts relevant to each category
    # returns a dictionary: category : Amount

# Main program
def main():

    import json
    print("Welcome to Expense Tracker.io!\n")
    
    try:
        with open("saved_expenses.json", "r") as file:
            loaded_expenses = json.load(file)
            expense_list = loaded_expenses
    except:
        expense_list = []
    
    while True:
        choice = get_option()
        
        if choice == "1":
            created_expense = create_expense()
            expense_list.append(created_expense)
            
        elif choice == "2":
            summarize_expenses(expense_list)
            
        elif choice == "3":
            #Serialize file to json
            saved_expenses = json.dumps(expense_list, indent = 4)
            
            #Save file
            with open("saved_expenses.json", "w") as save:
                save.write(saved_expenses)    
            print("Thank you for using Expense Tracker.io!")
            break
        
    
# Let user select options
def get_option():

    valid_choice = ["1", "2", "3"]
    
    print("What would you like to do? Please select a number.")
    print("1. Add an expense")
    print("2. View all expenses by category")
    print("3. Exit program")
    
    user_choice = input("Selection: ")
    
    if user_choice in valid_choice:
        return user_choice
    else:
        print('Please select a valid option!\n')

if __name__ == "__main__":
    main()