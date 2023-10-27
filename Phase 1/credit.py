def credit_by_usage():
#if credit owed is less than 30%, score increases. If it is less than 10, even better
    avg_credit_owed=get_average(credit_owed)
    if avg_credit_owed <=10:
        if  (1.1*(100-avg_credit_owed))>100:
            return 100
        else:
            #decrease credit score
            return 1.1*(100-avg_credit_owed)
    elif avg_credit_owed<=30:
        return (100-avg_credit_owed)
    elif avg_credit_owed <= 40:
        #no change
        return 0
    elif avg_credit_owed >40:
        return (-1 * avg_credit_owed)

def credit_by_history_length():
    '''increases credit if the history is long'''
# let's increase credit by 5 if the length is more than 6 months as the user doesn't control it
    avg_history_length=get_average(history_length)
    if avg_history_length>6:
        return 5/0.15
    else:
        return 0
def credit_by_new_cards():
    '''changes credit if hard inquiries have been made'''
    return (-10*new_cards)
#if no new cards have been applied to, credit doesn't change
def credit_by_payment_history():
    avg_payment_history=get_average(payment_history)
    if avg_payment_history==5:
        return 0
        #nochange
    if avg_payment_history>5:
        #increase
        return avg_payment_history*10
    if avg_payment_history<5:
        #decrease
        return (10-avg_payment_history)*10
def get_average(list):
    '''Finds the average value from a list from 1 to n element'''
    average = 0
    for i in range(len(list)):
        average+= list[i] / (len(list))
    return round(average,2)
def print_all_average():
    print(f"the average credit usage is {get_average(credit_owed)}%")
    print(f"the average payment history is {get_average(payment_history)}")
    print(f"the average credit history length is {get_average(history_length)}months")

def get_score():
    credit_score=credit_by_payment_history()*0.35 +credit_by_usage()*0.30 +credit_by_history_length()*0.15 +credit_by_new_cards()*0.10 +credit_type*0.10
    new_credit_score=credit_score+prev_credit
    print(f"Your possible credit score according to the data is : {new_credit_score}")

payment_history=[]
credit_owed=[]
history_length=[]
new_cards=[]
credit_type=100
prev_credit=int(input("Enter your previous credit score : "))
new_cards= int(input ("Enter the number of new credit cards you have appllied to in the past year : "))
number_of_cards= int (input("How many credit cards do you currently possess?\n"))
#for each card, ask for details
for i in range (number_of_cards):
    payment_history.append( int(input(f"\nEnter the payment history for card number {i+1} : ")))
    amount_per_card=(int(input(f"Enter the amount you owe in credit for card number {i+1} : ")))
    credit_line=(int(input(f"Enter the credit line for card number {i+1} :")))
    history_length.append(int(input(f"Enter the time your account (card number {i+1} has been active for in months :")))
    credit_owed.append((amount_per_card/credit_line) *100) #credit owed percentage

print(payment_history)
print(credit_owed)
print(history_length)
print_all_average()
get_score()