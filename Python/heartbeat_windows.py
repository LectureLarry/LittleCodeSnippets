# Heartbeat
# Checking, if SmartMeter is alive.
###################################

from random import randrange

# Set path to value.txt here
# path_to_value = '/home/pi/SMdata/heartbeat/'
path_to_value = 'c:\\Users\\gerweckt\\Desktop\\StrongBox4\\SMdata\\heartbeat\\'

random_number = randrange(1, 100)   # from 1...99
# print(random_number)   # debug

# Write this number into file.
with open(path_to_value + 'value.txt', 'w') as writer:
    writer.write(str(random_number))
