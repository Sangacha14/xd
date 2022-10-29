import os
import json
f= open("newmail.txt")  
u=(f.read())
z = u[:-1]
with open ("accounts.json","w") as file:
	file.write('['+z+']')
	file.close()
print("\n\n\33[48;5;5m\33[38;5;234m ❮ accounts.json ❯ \33[0m\33[48;5;235m\33[38;5;5m file created successfully \33[0m")	