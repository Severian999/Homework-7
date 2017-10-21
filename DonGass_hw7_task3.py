# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 22:48:03 2017

@author: Don Gass
"""

def decoded(user_tweet, acronym, full_word):
    tokens = user_tweet.split(acronym)
    print(tokens)
    
print(decoded('Gotta go. I will TTYL.','TTYL','talk to you later'))
print('Gotta go. I will TTYL.'.endswith('TTYL'))
print(decoded('abcdcdcd','cd','bc'))
print('abcdcdcd'.endswith('cd'))