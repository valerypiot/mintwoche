from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding 
import base64
import rng_randu 

rand = rng_randu.Randu()
cipher_txt = base64.b64decode("ybNfmfq0KGctz3UJHIO2zrOZnnwmi+Ksti+z78s/ydgIzCCBX522gkS01qzUMxRHGUDtNTW8BAXv04O9WmtMxM7U6J6g0uCGyACmn1Spt6U=")

# --- Find key --- 
seeds = []
for i in range(100): 
    if i % 2 == 0: 
        continue

    rand.seed(i)
    n = rand.random_hex()
    
    if n == "7": 
        seeds.append(i)

print(f"Possible seeds: {seeds}")

rand.seed(seeds[0])
key = ""
for i in range(16): 
    key += rand.random_hex()

print(f"Key: {key}")

# --- Find plaintext ---
cipher = AES.new(key.encode(), AES.MODE_ECB)

result_txt = Padding.unpad(cipher.decrypt(cipher_txt), 16).decode()

with open("plaintext1.txt", "w") as f: 
    f.write(result_txt)

print("Plaintext: " + result_txt)