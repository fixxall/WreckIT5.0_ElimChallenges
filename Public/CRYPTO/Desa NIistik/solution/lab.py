from cffi import FFI
ffi = FFI()
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec


privkey = ec.derive_private_key(4348293, ec.SECP256K1())
message = b'asem banget'
signature = privkey.sign(
    message,
    ec.ECDSA(hashes.SHA256()),
)
# print("signature:",signature)
pubkey = privkey.public_key()
pb_byte = pubkey.public_bytes(serialization.Encoding.X962,serialization.PublicFormat.CompressedPoint)

from coincurve import PrivateKey, PublicKey, verify_signature
from coincurve.utils import int_to_bytes_padded

pb0 = PublicKey(pb_byte)
x,y = pb0.point()

pbks_byte0 = PublicKey(pb_byte)
cors = int_to_bytes_padded(x)+int_to_bytes_padded(y)
pbks_byte1 = PublicKey(b'\x04'+cors)
pad = b''
if(pb_byte[0]==b'\x02'[0]): pad=b'\x06'
else: pad = b'\x07'
pbks_byte2 = PublicKey(pad+cors)

print(pad)
print(verify_signature(signature, message, pbks_byte0.format()))
print(verify_signature(signature, message, pbks_byte1.format()))
print(verify_signature(signature, message, pbks_byte2.format()))

print(ec.SECP256K1())