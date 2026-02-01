import os
def encrypt_file(filename,key):
	if not os.path.exists(filename):
		print("kojja na kodaka sarigga rayi ra")
		return
	with open(filename,"rb") as f:
		data = f.read()	
	key_bytes = key.encode()
	scrambled = []
	for i in range(len(data)):
        	scrambled_byte = data[i] ^ key_bytes[i % len(key_bytes)]
        	scrambled.append(hex(scrambled_byte))
	print("\n[+] Encryption Complete! Copy the list below:\n")
	print("scrambled_hex = [")
	print(", ".join(scrambled))
	print("]")
encrypt_file("payload.bin", "SECRET")
