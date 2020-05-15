class Flower:
    """class of Flower"""

    def __init__(self, name="Flower", amount=5, price=10.0):
        
        if not isinstance(name, str):       raise ValueError("Name should be str")
        if not isinstance(amount, int):     raise ValueError("Amount must be int")
        if not isinstance(price, float):    raise ValueError("Price must be float")

        if not amount >= 0: raise ValueError("Amount need >= 0")
        if not price > 0: raise ValueError("Price need > 0")

        self._name, self._amount, self._price = name, amount, price

    def get_name(self):     return self._name

    def get_amount(self):   return self._amount

    def get_price(self):    return self._price

    def set_name(self, name):
        if not isinstance(name, str):   raise ValueError("Name should be str")
        self._name = name
    
    def set_amount(self, amount):
        if not isinstance(amount, int): raise ValueError("Amount must be int")
        if not amount >= 0: raise ValueError("Amount need >= 0")
        self._amount = amount
    
    def set_price(self, price):
        if not isinstance(price, float):    raise ValueError("Price must be float")
        if not price > 0: raise ValueError("Price need > 0")
        self._price = price


if __name__ == '__main__':
    f = Flower("love", 10, 3.0)
    print(f.get_name())
    
    f.set_name("joy")
    print(f.get_name())