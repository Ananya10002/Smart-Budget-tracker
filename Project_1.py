#Smart Budget tracker
def clean_amount(text):
    text.replace("," , " ")
    text.replace( "$" , " ")
    return text
income=clean_amount(input("Enter your monthly income:"))
l=clean_amount(input("What is your home rent:"))
f=clean_amount(input("How much do you spend on grocieries?:"))
n=clean_amount(input("Enter any other necessary expense,excluding rent and grocieries:"))
w=clean_amount(input("What is your unnessary expense[wants]:"))
print("For this Month-")
total_expense= l+n+f+w
needs=l+n+f
print("For this month you spent:", total_expense)
savings=income-total_expense

#Function to check if budget follows 50/30/20 rule
def Budget_check(savings,income,needs,w):
    If needs/income*100=<50:
    print("Great, You are able to spend 50 or less of your income in your needs")
else:
    print("You should focus on saving 50% of your income for basic needs.")
     if w/income*100<=30: 
      print("great you are spending in right amount")
     else:
      print("WARNING!!! your unnessary expenses must not exceed 30% of your income") 
    if savings/income*100>=20:
     print("Great,you are being good at saving a portion of your income")
    else:
     print("you must focus on atleast saving 20% of your income")  

Budget_check(savings,income,needs,w) #calling function

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

