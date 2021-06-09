# Laufschrift
# ###########
import time

text = "Das ist noch ein anderer Laufschrifttext! "

# TODO: Nothing to do here. Just testing ToDo :-)
while True:
    i = 0
    while i < len(text):
        print('\r' + text[i:] + text[0:i], end='')
        i += 1
        time.sleep(0.3)
