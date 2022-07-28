# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main


food = budget.Category("Food")
clothing = budget.Category("Clothing")
auto = budget.Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaursant and more food for dessert")
food.transfer(50, clothing)

clothing.withdraw(25.55)
clothing.withdraw(100)

auto.deposit(1000, "initial deposit")
auto.withdraw(15)

for category in [food, clothing, auto]:
    print(category, end='\n\n')

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)