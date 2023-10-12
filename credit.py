def get_score():
    pass
#the first element in each list is the percentage it affects the credit
payment_history=[35]
credit_owed=[30]
history_length=[15]
new_cards=[10]
credit_type=[10]
new_cards= input ("Enter the number of new credit cards you have appllied to in the past year : ")
number_of_cards= int (input("How many credit cards do you currently possess?\n"))
#for each card, ask for details
for i in range (number_of_cards):
    payment_history.append( int(input(f"\nEnter the payment history for card number {i+1} : ")))
    amount_per_card=(int(input(f"Enter the amount you owe in credit for card number {i+1} : ")))
    credit_line=(int(input(f"Enter the credit line for card nunber {i+1}")))
    history_length.append(input(f"Enter the time your account (card number {i+1} has been active for :"))
    credit_owed.append((amount_per_card/credit_line) *100)
print(payment_history)
print(credit_owed)
print(history_length)
