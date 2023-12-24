long_string = """Hello this is a multi-line
string that i am showing. Multiverse!"""
print(long_string)

print(len(long_string))
print("showing" in long_string)
print("fish" not in long_string)

print(long_string[0:5])

uppercase = long_string.upper()
print(uppercase)

lowercase = long_string.lower()
print(lowercase)

weird_string = "    face   "
print(weird_string.strip())

hello = "Hello"
print(hello.replace("H", "J"))

basic = "Hello, World!"
print(basic.split(","))

concat = "cheese" + " " + "burger"
print(concat)

apple_amount = 3
print("Hello, I have {} apples.".format(apple_amount))
