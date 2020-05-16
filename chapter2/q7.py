#q7: one add choice: non-zero initialization of the account
from example_creditcard import CreditCard

class CreditCard_q7(CreditCard):
    """non-zero initialization of the account"""

    def __init__(self, customer, bank, acnt, limit, start=0):
        
        super().__init__(customer, bank, acnt, limit)
        if start != 0:
            self._balance = -start  # here i set to negative value


if __name__ == '__main__':
    
    card = CreditCard_q7('John', 'Commonwealth', '5907 8901', 2500)

    print(card.charge(100))
    print(card.charge(300))
    print(card.get_balance())

    print(card.charge(10000))

    card2 = CreditCard_q7('John', 'Commonwealth', '5907 8901', 2500, 2500)

    print(card2.get_balance())
    print(card2.charge(100))
    print(card2.charge(300))
    print(card2.get_balance())

    print(card2.charge(10000))