import base64
import pathlib

from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

cipher = AES.new(b"75fd75fd75fd75fd", AES.MODE_ECB)

cipher_txt = base64.b64decode("ybNfmfq0KGctz3UJHIO2zrOZnnwmi+Ksti+z78s/ydgIzCCBX522gkS01qzUMxRHGUDtNTW8BAXv04O9WmtMxM7U6J6g0uCGyACmn1Spt6U=")

result_txt = Padding.unpad(cipher.decrypt(cipher_txt), 16)

r = result_txt.decode()

out = pathlib.Path(__file__).resolve().parent / "plaintext.txt"
with open(out, "w") as f:
    f.write(r)

print(r)
