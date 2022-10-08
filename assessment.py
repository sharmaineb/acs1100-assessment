# test = "aman,1234,Andy Allman,1000".split(',')
# print(test[0]) # aman
# print(test[1]) # 1234
# print(test[2]) # Andy Allman
# print(test[3]) # 1000

# prompt for a user name
# prompt for a password
# look up the user matching both the user name and the password
# print out the user's full name and account balance

# store the file name in a variable:
# filename = open("data.txt", "r").readlines()

# # open the file in readmode
# f = open(file_lines, 'r')

# # using .readlines(), create a list wheere each element is 
# # a line from the file.
# lines = infile.readlines()
# 
# # create a dictionary
# customer_list = []

# for line in lines:
# remove the new line character from line
# stripped_line = line.strip()
# split string into two separate strings
# split_line = stripped_line.split(',')

# access the key and value from the split list
# key = split_line[0]
# value = split_line[1]

# add to the dictionary 
# customer_list[key] = value
# print(customer_list)
# print(customer_list)
# --------------------------------------------------------------------------------------------------------------------------------------------
# Notice string `split()` takes a delimeter (comma in this case ",") and splits the string on this character returning an array of substrings. 
# From here you can access each element using the list syntax: 
# Write a function to load data. 
# Parameter: file_lines, 
# returns a list of users (customer_list).
def load_data(file_lines):
    f = open(file_lines, "r")
    bank_list = f.readlines()
    f.close()

    return bank_list
# --------------------------------------------------------------------------------------------------------------------------------------------
# Write a login function that takes username and password as parameters 
# and returns a user dictionary. 
# Parameters: input_username, input_password
def login(input_username, input_password):
    input_username = input("Enter Username: ")
    input_password = input("Enter Password: ")
    # create a dictionary
    customer_information = {}
    # Loop through the customers in the customer_list and checks if a customer is not in customer_list
    # checks if the username and password the user inputs is in the list from customer_list.
    for customer in bank_list:
        username, password, name, balance = customer.strip().split(",") # splits text after (",") into each line
        if input_username == username and input_password == password: # checks if the username and password input by the customer is in the bank_list
            customer_information = {"Name": name, "Balance":"$" + str(balance)} # can only concatenate str to str when concatenating str to list
    # return a user dictionary        
    return customer_information

# --------------------------------------------------------------------------------------------------------------------------------------------
# Write a function to display the user information. 
# Parameters: one or more strings, or an array and return a formatted string. 
# Parameters: customer, error_message
# If the user name and password are not found it should print the message: "User name and password not found"
def display(customer): 
    if customer == {}: # checks if the username and password are in customer_information
      print("Sorry. Username and Password Not Found. Try Again.") # if not found print
    customer_account = f"Name: {customer['Name']}\nBalance: {customer['Balance']}"
    print(customer_account)
    return()

#--------------------------------------------------------------------------------------------------------------------------------------------   
# Your program should load the data. 
input_username = login
input_password = login
bank_list = load_data("data.txt")
customer = login(input_username, input_password)


display(customer)