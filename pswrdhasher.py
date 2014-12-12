!/bin/python3
import os
import hashlib

password = input('Password Here > ')

# Divide password into chunk of 6 char
# eg. 12345678901230
# then 
# 123456
# 789012
# 30

# Initial Password
# 'def' 
# Pop out last char to hash
# 'de' hash('f') -> f
# print(f) -> 64CharHash of 'f'
# 'd' hash('e',f) -> e
# '' hash('d',e) -> FinalHash
# print(FinalHash)

# Save FinalHash to localfile
# Read hash localfile
# Input to confirmer
# if confirmer true
# then print(Access Granted)
# elif confirmer false
# then exit/quit/ctrl+c

password = input('Password Here > ')

hashInt = 0
for char in password:
	hashInt += hash(char)
print(hashInt,len(_))


-1531827972080291699






