#Part 2 Analyzing Spending
from prettytable import PrettyTable
import numpy as np
import random
def get_table():
    table=PrettyTable(['S/N','Item','Price','Frequency','Total'])
    for i in range(len(items_array)):
        #adding table rows
        table.add_row([i+1,items_array[i],price_array[i],frequency_array[i],moneyspent_array[i]])
    print(table)
def get_most_spent_item():
    most_spent_on_item_name=items_array[moneyspent_array.argmax()]
    most_spent_on_item_price=price_array[moneyspent_array.argmax()]
    most_spent_on_item_frequency=frequency_array[moneyspent_array.argmax()]
    most_spent=moneyspent_array[moneyspent_array.argmax()]
    print(f"The item you spent most on was {most_spent_on_item_name}\nYou spent a total of ${most_spent} on {most_spent_on_item_frequency} items\nThe cost of each {most_spent_on_item_name} was ${most_spent_on_item_price}\n")
    if most_spent_on_item_name in fresh_produce:
         print (f"It looks like you purchased Premium {most_spent_on_item_name}. Maybe buying the regular kind might be better for your budget")
    elif most_spent_on_item_name in snacks:
         print(f"It looks like you spent alot on snacks. Maybe consuming more homemade foods might be budget friendly.")
def cheap_or_expensive():
    avg_price=price_array.mean()
    if price_array[moneyspent_array.argmax()]<avg_price: # if the item spent most on is less than avg prices in the list
            print(f"This item looks like one of the cheaper ones.\nThe average price of each item you spent on is ${avg_price:.2f}\nYou might be surprised how those small, cheap purchases can add up to a significant expense over time. \nIs this item really worth the long-term cost?\n")
    elif price_array[moneyspent_array.argmax()]>avg_price:# if the item spent most on is more than avg prices in the list
         print(f"This Item looks like an expensive one.\nThe average price of each item you spent on is ${avg_price:.2f}\nBefore you make that purchase, ask yourself: Is this item worth the price, or are there more affordable alternatives that can still meet your needs?\n")
fresh_produce=np.array(["Apples","Bananas","Strawberries","Avocados","Bell Peppers","Carrot","Garlic","Lemons/Limes","Onion","Parsley","Cilantro","Spinach","Tomatoes"])
snacks=["Crackers","Nuts","Quick Oats","Popcorn","Tortilla Chips","Cereal"]
items_array=np.array(["Crackers","Nuts","Quick Oats","Popcorn","Tortilla Chips","Cereal","Apples","Bananas","Strawberries","Avocados","Bell Peppers","Carrot","Garlic","Lemons/Limes","Onion","Parsley","Cilantro","Spinach","Tomatoes",'Video games','Meat','Potatoes','Mushroom','Water','Internet','Gas','Electricity','Netflix','McDonalds'])
price_array=np.random.randint(10,70,size =29)
frequency_array=np.random.randint(10,size =29) 
moneyspent_array=price_array*frequency_array
total_spent=moneyspent_array.sum()

print('Spending Analyzer\n')
print(f"Total spent this month : ${total_spent}\n")
get_most_spent_item()
cheap_or_expensive()
show_table= input("Do you want to see a table on what you have spent on? (Y/N)\n")
if show_table.upper()=='Y':
    get_table()
