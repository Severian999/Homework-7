# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 22:48:03 2017

@author: Don Gass
"""
import re

###############################################################################
############## The easy way ###################################################

def re_decoded(user_tweet, acronym, full_word):
    """ Use the regular expression module sub method to replace the strings
    """
    return re.sub(acronym, full_word, user_tweet)

def rep_decoded(user_tweet, acronym, full_word):
    """ Use the str.replace() method to replace the strings
    """
    return user_tweet.replace(acronym, full_word)

############## End of the easy way ############################################    
###############################################################################
    
def decode(user_tweet, acronym, full_word, start=0):
    """Use recursive function and string slicing to replace the strings
    """
    if acronym not in user_tweet or user_tweet.find(acronym, start) == -1:
        return user_tweet
    pos = user_tweet.find(acronym, start)
    decoded_tweet = user_tweet[:pos] + full_word + user_tweet[pos + len(acronym):]
    return decode(decoded_tweet, acronym, full_word, pos + len(full_word))

print('These were processed with the regular expression module.')    
print(re_decoded('Gotta go. I will TTYL.','TTYL','talk to you later'))
print(re_decoded('abcdd','cd','bc'))
print(re_decoded('abcdcd','cd','bc'))
print('\n')

print('These were processed with the str.replace() method')
print(rep_decoded('Gotta go. I will TTYL.','TTYL','talk to you later'))
print(rep_decoded('abcdd','cd','bc'))
print(rep_decoded('abcdcd','cd','bc'))
print('\n')

print('These were processed with my homegrown recursive function')
print(decode('Gotta go. I will TTYL.','TTYL','talk to you later'))
print(decode('abcdd','cd','bc', 0))
print(decode('abcdcd','cd','bc', 0))

