#Smart Budget tracker
income=int(input("Enter your monthly income:"))
l=int(input("What is your home rent:"))
f=int(input("How much do you spend on grocieries?:"))
n=int(input("Enter any other necessary expense,excluding rent and grocieries:"))
w=int(input("What is your unnessary expense[wants]:"))
print("For this Month-")
total_expense= l+n+f+w
print(total_expense)
savings=income-total_expenses
if income>total_expense:
    print("Great,you are on the right way!")
else:
    print("you must reduce your expenses")
print("Following the 50/30/20 rule-")
if (l+n+f)/income*100>= 50:
    print("Great,you are successfully invested 50% or lesser of income in needs")
    print("You are on right path")
else:
    print("You must reduce your unnessary expenses or liabilities")
if w/income*100>=30: 
    print("great you are spending in right amount")
else:
    print("your unnessary expenses must not exceed 30% of your income") 
if (income-total_expense)*100>=20:
    print("Great,you are being good at saving a portion of your income")
else:
    print("you must focus on atleast saving 20% of your income")  

print("Thanks for using Smart budget tracker")
from datetime import datetime
now=datetime.now()
date=now.strftime("%d-%m-%Y")
time=now.strftime("%H-%M")
print(date)
print(time)
with open("budget.txt","a") as file:
    file.write(f"Income: {income}\n")
    file.write(f"total_expense: {total_expense}\n")
    file.write(f"Spent on groceries: {f}\n")
    file.write(f"Spent on home rent: {l}\n")
    file.write(f"Spent on other nessesary expenses: {n}\n")
    file.write(f"Spend on unnessary expenses: {w}\n")
    file.write(f"Savings: {savings}\n")
