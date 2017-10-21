# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:00:43 2017

@author: Don Gass
"""

alphabet = "abcdefghijklmnopqrstuvwxyz "
key      = "sxzaijhbwpekfcqrgdtluv noym"

def substitutionEncrypt(plainText, key):
    encrypted_string = ""
    for letter in plainText:
        pos = alphabet.find(letter)
        encrypted_string += key[pos]
    return encrypted_string

def substitutionDecrypt(cipherText, key):
    decrypted_string = ""
    for letter in cipherText:
        pos = key.find(letter)
        decrypted_string += alphabet[pos]
    return decrypted_string        
            
mytext = 'today is tuesday'

print('The text to be enrypted:  ', end="")
print(mytext, '\n')

encrypted_text = substitutionEncrypt(mytext, key)
print('Encrypted: ', encrypted_text)

decrypted_text = substitutionDecrypt(encrypted_text, key)
print('Decrypted: ', decrypted_text)
