import random
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.-;:_[]{}+*%&/()=?<>"
cipher_txt = base64.b64decode("xDjRYCkTVn8NnFBcDHKP0AFg5LA2qvOb4iCGLYLsXDpcGCyZg26yDKbrzm4ijMq7amYwFhqgdLOjIKQe57dT9g==")
results = []

# random.seed(random.randrange(1000000))

def keygen(seed): 
    random.seed(seed)
    
    key = ""
    for n in range(16):
        index = random.randrange(len(ALPHABET))
        char = ALPHABET[index]
        key += char

    return key

def find_plaintext(key): 
    cipher = AES.new(key, AES.MODE_ECB)

    try: 
        result_txt = Padding.unpad(cipher.decrypt(cipher_txt), 16)
        results.append(result_txt.decode())
        
    except Exception: 
        pass 

for seed in range(1000000): 
    find_plaintext(keygen(seed).encode())

with open("plaintext2.txt", "w") as f: 
    for r in results: 
        f.write(r + "\n")

print(results)