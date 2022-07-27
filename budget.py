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

# def create_spend_chart(categories):
