class CreditCard:
    """a consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    def get_customer(self): return self._customer

    def get_bank(self): return self._bank

    def get_account(self): return self._account

    def get_limit(self): return self._limit

    def get_balance(self): return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        self._balance -= amount


if __name__ == '__main__':
    
    card = CreditCard('John', 'Commonwealth', '5907 8901', 2500)

    print(card.charge(100))
    print(card.charge(300))
    print(card.get_balance())

    print(card.charge(10000))