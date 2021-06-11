# Hello World Advanced
# ####################

text = "Hello World! "

i = 1
while i < 100:
    print(text, end='')
    if i % 9 == 0:
        print("\r")
    i += 1
