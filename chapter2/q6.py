#q6, same as q5

from example_creditcard import CreditCard

class CreditCard_q5(CreditCard):
    
    def charge(self, price):
        if not isinstance(price, (int, float)):
            raise ValueError("price need to be an int or float")

        if price <= 0:
            raise ValueError("price need to be >= 0")
        
        # the original "charge" function has return value, so need to add "return"
        return super().charge(price)
    
    def make_payment(self, amount):

        if not isinstance(amount, (int, float)):
            raise ValueError("payment amount need to be an int or float")

        if amount <= 0:
            raise ValueError("payment amount need to be >= 0")  
        
        # the original function does not have return value, so no need to add "return"
        super().make_payment(amount)

if __name__ == '__main__':
    
    card = CreditCard_q5('John', 'Commonwealth', '5907 8901', 2500)

    print(card.charge(100))
    print(card.charge(300))
    print(card.charge(10000))
    print(card.get_balance())

    card.make_payment(100)
    print(card.get_balance())


    # card.make_payment(-50)
    # print(card.get_balance())