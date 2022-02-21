# Strings in Python
# Concatenation (adding two strings i.e print("My name " + "is Ali."))
# Functions/Methods (is an action python performs on a piece of data) e.g .title() or .upper() or .lower() etc

message = "Dream big work hard"  # or 'Dream big work hard'
print("Bro: " + message)  # concatenation

# Using some basic functions
print(message.upper())    # upper case
print(message.lower())    # lower case
print(message.title())    # First letter of each word is Capital
print(message.isupper())  # check whether message is in upper case or not ... True or False
print(message.islower())  # check whether message is in lower case or not ... True or False
print(message.istitle())  # check whether message is in title case or not ... True or False
print(len(message))        # length function finds out no,of characters (also counts spaces)
print(message[0])          # index you want to find out
print(message.index("work"))  # returns index of that specific word
print(message.replace("big", "small"))   # replace a word

# Using variables in strings
first_name = "Ali"
last_name = 'Daud'
full_name = f"Hello,{first_name} {last_name}!"   # f-strings ("f" means format)
print(full_name)
