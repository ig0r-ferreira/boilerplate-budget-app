from itertools import zip_longest

class Category:
    def __init__(self, name:str):
        self.name = name
        self.ledger = list()
        self.balance = 0

    def deposit(self, amount:float, description:str='') -> None:
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self) -> float:
        return self.balance

    def check_funds(self, amount:float) -> bool:
        return  amount <= self.get_balance()

    def withdraw(self, amount:float, description:str='') -> bool:
        if not self.check_funds(amount): return False 
        
        self.balance -= amount
        self.ledger.append({'amount': -amount, 'description': description})        
        return True

    def transfer(self, amount:float, category:'Category') -> bool:
        if not self.check_funds(amount): return False
        
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True
    
    def __str__(self) -> str:
        item_display = '{description:<23.23s}{amount:>7.2f}' 
        transactions = [item_display.format(**transaction) for transaction in self.ledger]
        return f'{self.name:*^30}\n' + '\n'.join(transactions) + f'\nTotal: {self.get_balance():.2f}'


def create_spend_chart(categories:list):    
    title = 'Percentage spent by category'
    row = '\n{:3}{sep}' + ('{:^3}' * len(categories)) + ' '
    dashed_sep = f'{"":4}{"":->{(3 * len(categories) + 1)}}'

    x_labels, y_labels, expenses = [], range(100, -1, -10), []

    for category in categories:
        x_labels.append(getattr(category, 'name'))
        expenses.append(get_total_spend_by_category(category))
    
    percentages = calc_percent_of_expenses(expenses)
    bars = generate_bars(percentages)
    
    chart = title
    for data in zip_longest(y_labels, *bars): chart += row.format(*data, sep='|')
    chart += f'\n{dashed_sep}'
    for letters in zip_longest(*x_labels, fillvalue=' '): chart += row.format('', *letters, sep=' ')

    return chart


def get_total_spend_by_category(category:Category):
    return sum(transaction['amount'] for transaction in getattr(category, 'ledger') if transaction['amount'] < 0)


def calc_percent_of_expenses(expenses:list):
    total_spend = sum(expenses)
    return tuple([int(expense / total_spend * 10) for expense in expenses])


def generate_bars(percents:list):  
    return tuple((10 - percent) * ' ' + 'o' * (percent + 1) for percent in percents)
