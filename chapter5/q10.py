"""
re-write the initialization part in the CaesarCipher
"""

from example_cipher import CaesarCipher

class CaesarCipher2(CaesarCipher):
    def __init__(self, shift):
        """this part replaces the original initialization"""
        self._forward_key = "".join( chr( (k+shift)%26 + ord('A') ) for k in range(26) )    # don't need the "list" symbol in: join([xxxx])
        self._backward_key = "".join( chr( (k-shift)%26 + ord("A") ) for k in range(26) )
        # print("ok")


if __name__ == '__main__':
    msg = "THE EAGLE IS IN PLAY; MEET AT JOE'S"

    cipher = CaesarCipher2(3)
    coded = cipher.encrypt(msg)
    decoded = cipher.decrypt(coded)

    print(coded)
    print(decoded)