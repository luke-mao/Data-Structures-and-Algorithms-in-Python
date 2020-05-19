class CaesarCipher:

    def __init__(self, shift):

        encoder = [None] * 26
        decoder = [None] * 26

        for k in range(26):
            encoder[k] = chr( (k+shift)%26 + ord('A') )
            decoder[k] = chr( (k-shift)%26 + ord('A') )
        
        self._forward_key = "".join(encoder)
        self._backward_key = "".join(decoder)
    
    def encrypt(self, msg):
        return self._transform(msg, self._forward_key)
    
    def decrypt(self, msg):
        return self._transform(msg, self._backward_key)
    
    def _transform(self, msg, key):

        result = list(msg)

        for i in range(len(result)):
            letter = result[i]

            if letter.isupper():
                result[i] = key[ord(letter) - ord("A")]
            
            # for other character: keep it
        
        return "".join(result)


if __name__ == '__main__':
    msg = "THE EAGLE IS IN PLAY; MEET AT JOE'S"

    cipher = CaesarCipher(3)
    coded = cipher.encrypt(msg)
    decoded = cipher.decrypt(coded)

    print(coded)
    print(decoded)