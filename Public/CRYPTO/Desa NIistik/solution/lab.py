from secp256k1 import PrivateKey, PublicKey
from cffi import FFI
ffi = FFI()
from cryptography.hazmat.primitives import serialization

priv = PrivateKey(bytes.fromhex('ee3aaf37fc333dd1deb32605d5599cbde64207110aba7d697559148b96a29023'))
# print(priv.serialize())
# message = b'asem banget'
# pub = priv.pubkey

# ndata = ffi.new("int *") + 1
# sign = priv.ecdsa_sign(message, custom_nonce=(ffi.NULL, ffi.NULL))
# signature = priv.ecdsa_serialize(sign)
# print(signature)
# hash = PrivateKey().ecdsa_deserialize(signature)
# print(pub.ecdsa_verify(message, hash))
# print(pub.ecdsa_verify(message, sign))

from cryptography.hazmat.primitives.asymmetric import ec
pubkey = (ec.derive_private_key(1, ec.SECP256K1()).public_key().public_bytes(serialization.Encoding.X962,serialization.PublicFormat.CompressedPoint))
pub = PrivateKey().pubkey.serialize()
pb = PublicKey(pubkey, raw=True)
print(pubkey)
print(pub)
# from coincurve import PublicKey, PrivateKey

# mess = b'get_flag'
# secret = b'sembarangansajalahkamuasu'
# priv = PrivateKey(secret)
# pub = PublicKey.from_secret(secret)
# newvoid = ffi.new("int *")
# signature2 = priv.sign(mess,custom_nonce=(ffi.NULL, newvoid))
# print(signature2)
# print(pub.verify(signature2, mess))
