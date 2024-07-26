from propietary import *

while True:
	X_hex = input('choose your man (hex): ')
	Y_hex = input('choose your woman (hex): ')
	
	hash_value1 = HORTEX(X_hex)
	hash_value2 = HORTEX(Y_hex)
	
	if hash_value1 == hash_value2:
		print("New couple is matched :). Here your flag WRECKIT50{REDACTED}")
		break
	else:
		print("Try again")
		break