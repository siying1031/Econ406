
# Question 1
# This function takes deposited money and annual interest rate
# as input, and returns the total wealth after 10 years.

def totalWealth(P, IR, n):
    FV = P*((1+IR)**n)
    return FV

# Asks user to input numbers.
deposit_money = float(input("How much money deposit in Bank?"))
annual_interest = float(input("What is the annual interest rate?"))

# Calls the function to calculate the total wealth
total_wealth_Bill = totalWealth(deposit_money, annual_interest,10)
print("Bill's total wealth is $" + str(round(total_wealth_Bill,2)))

# Question 2:
# Calculates number of years that Bill's money will double 
# with a given interest rate.    
import math
def how_long(FV, P, IR):
    n = math.log(FV/P) / math.log(1+IR)
    return n

# Asks user to input numbers. 
deposit_money = float(input("How much money deposit in Bank?"))
annual_interest = float(input("What is the annual interest rate?"))
desire_value = 2*deposit_money

# Calls the function to calculate the total wealth
time_Bill = how_long(desire_value,deposit_money,annual_interest) 
print('It takes',str(round(time_Bill,2)) ,'years to double Bill’s money.')

# Question 3:
# Method 1
# Calculate actual value given by the IR and n.

deposit_money = float(input("How much money deposit in Bank?"))
annual_interest = float(input("What is the annual interest rate?"))
desire_value = 2*deposit_money

total_wealth_Jack = totalWealth(deposit_money,annual_interest,6)
if total_wealth_Jack >= desire_value:
    print(True)
else:
    print(False)
    
# Method 2
# Check if money will double in 6 years.
time_Jack = how_long(desire_value,deposit_money,annual_interest)
if time_Jack < 6:
    print(True)
else:
    print(False)

# Question 4: List
# Creates a list with the information of customer's savings.
customer_savings = ['Bill', 1000, 'Jack', 5000, 'Amy', 6700, 'Cindy', 5699, 'Harry', 6700]
print(customer_savings)

# Question 5: Dictionary
# Creates a dictionary with the information of customer's savings.    
Accounts = {}
Accounts['Bill']= 1000
Accounts['Jack']= 5000
Accounts['Amy']= 6700
Accounts['Cindy']= 5699
Accounts['Harry']= 6700
print(Accounts)

# Question 6: Tuples
# Creates a list of tuples that contain all the information in the dictionary.
# k,v is abbreviation of key value pair
new_list = [(k,v) for k,v in Accounts.items()]
print(new_list)


# Question 7: Differences among, list, dictionary, and sets

# List, dictionary,and sets are all fundamental data structures.
# List is mutable and can store a sequence of objects in a certain order,
# which the objects can be indexed.

# Dictionary is mutable with a key-value pair structure.
# However, it is not ordered, elements are accessed using key or value.

# Set is mutable and is an unordered collection data type. 
# It is a method for checking whether a specific element is contained in the set.

# When we have a set of unique keys, we can map those values to a key-value 
# structure using dictionary.
# When we have an ordered collection of items, we use list.

# List keeps order, dictionary and set do not.
# Dictionary connects each key with a value, but list and set contain only values.
# Set forbids duplicates, list does not. 


