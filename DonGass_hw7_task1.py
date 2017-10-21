# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 18:22:36 2017

@author: Don Gass
"""
##### Match the following output #####
#2012 quarterback statistics:
#  Passes completed:
#    Greg McElroy   :  19
#    Aaron Rodgers  : 371
#    Peyton Manning : 400
#    Matt Leinart   :  16
#  Passing yards:
#    ...
#  Touchdowns / Interception ratio:
#    Greg McElroy   : 1.00
#    Aaron Rodgers  : 4.88
#    Peyton Manning : 3.36
#    Matt Leinart   : 0.00


quarterback_stats = {
    'Aaron Rodgers': {'COMP': 371, 'YDS': 4925, 'TD': 39, 'INT': 8},
    'Peyton Manning': {'COMP': 400, 'YDS': 4659, 'TD': 37, 'INT': 11},
    'Greg McElroy': {'COMP': 19, 'YDS': 214, 'TD': 1, 'INT': 1},
    'Matt Leinart': {'COMP': 16, 'YDS': 115, 'TD': 0, 'INT': 1}
}

print('2012 quarterback statistics:')

print('  Passes completed:')
for qb in quarterback_stats:
    comp = quarterback_stats[qb]['COMP']
    print('    %-15s: %4d' % (qb, comp))  # Replace conversion specifiers
    # Hint: Use the conversion flag '-' to left-justify names

print('  Passing yards:')
for qb in quarterback_stats:
    yards = quarterback_stats[qb]['YDS']
    print('    %-15s: %4d' % (qb, yards))

print('  Touchdown / interception ratio:')
# ...
# Hint: Convert TD/INTs to float before calculating ratio 
for qb in quarterback_stats:
    numTDs = float(quarterback_stats[qb]['TD'])
    numINTs = float(quarterback_stats[qb]['INT'])
    print('    %-15s: %1.2f' % (qb, numTDs / numINTs))