import random
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.-;:_[]{}+*%&/()=?<>"
cipher_txt = base64.b64decode("xDjRYCkTVn8NnFBcDHKP0AFg5LA2qvOb4iCGLYLsXDpcGCyZg26yDKbrzm4ijMq7amYwFhqgdLOjIKQe57dT9g==")
results = []

# -- generate key --
def keygen(seed): 
    random.seed(seed)
    
    key = ""
    for n in range(16):
        index = random.randrange(len(ALPHABET))
        char = ALPHABET[index]
        key += char

    return key

# -- find plaintext with key --
def find_plaintext(key): 
    cipher = AES.new(key, AES.MODE_ECB)

    try: 
        result_txt = Padding.unpad(cipher.decrypt(cipher_txt), 16)
        results.append(result_txt.decode())
        print("Possible plaintext found.")
        
    except Exception: 
        pass 

# -- trying 1 million keys --
if __name__ == "__main__": 
    print("Cooking...")
    
    for seed in range(1000000): 
        if seed % 100000 == 0 and seed > 0: 
            print(f"Tried {seed} keys...")
        
        find_plaintext(keygen(seed).encode())

    with open("plaintext2.txt", "w") as f: 
        for r in results: 
            f.write(r + "\n")

    print(results[0])