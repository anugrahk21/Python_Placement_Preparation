#String
#String is a immutable sequence of characters, i.e once created, its elements cannot be changed or modified.

S="Hello, World!"
print(S)

# Indexing
print(S[7])  # W

# Slicing
print(S[0:5])  # Hello

# Reversing a string
print(S[::-1]) # !dlroW ,olleH

# Length of string
print(len(S))   #13

# String Manipulation : Insertion, Deletion, Update

# Since strings are immutable, we cannot change them directly. However, we can create new strings based on existing ones.

# Insertion
S1 = S[:7] + "Beautiful " + S[7:]
print(S1)  # Hello, Beautiful World!

# Deletion
S2 = S.replace("Hello, ","")
print(S2)  # World!

# Update
S3 = S.replace("World", "Universe")
print(S3)  # Hello, Universe!

# String Methods
print(S.lower())  # hello, world!
print(S.upper())  # HELLO, WORLD!
print(S.split(", "))  # ['Hello', 'World!']
print(S.find("World"))  # 7
print(S.replace("World", "Everyone"))  # Hello, Everyone!
print(S.strip("!"))  # Hello, World
print(S.startswith("Hello"))  # True
print(S.endswith("!"))  # True
print(S.count("o"))  # 2
print(S.isalpha())  # False (because of space and punctuation)
print(S.isdigit())  # False
print(S.join(["Hi", "There"]))  # HiHello, World!There
print(S.capitalize())  # Hello, world!
print(S.title())  # Hello, World!
print(S.center(30, '-'))  # ---------Hello, World!---------
print(S.zfill(20))  # 0000000Hello, World!
print(S.encode())  # b'Hello, World!'
print(S.expandtabs(tabsize=4))  # Hello, World! (no tabs to expand here)
print(S.swapcase())  # hELLO, wORLD!
print(S.partition(", "))  # ('Hello', ', ', 'World!')
print(S.rpartition(", "))  # ('Hello', ', ', 'World!')
print(S.splitlines())  # ['Hello, World!']
print(S.translate(str.maketrans("Helo", "Jxyz")))  # Jxyyz, Wxrzd!
print(S.removeprefix("Hello, "))  # World!
print(S.removesuffix("!"))  # Hello, World
print(S.casefold())  # hello, world!
print(S.isprintable())  # True
print(S.islower())  # False
print(S.isupper())  # False
print(S.istitle())  # True
print(S.rfind("o"))  # 8
print(S.rindex("o"))  # 8
print(S.zfill(25))  # 0000000000000Hello, World!
print(S.count("l", 0, 5))  # 2
print(S.encode('utf-8'))  # b'Hello, World!'
print(S.format())  # Hello, World!
print(S.format_map({'greet': 'Hello', 'place': 'World'}))  # Hello, World!
print(S.isidentifier())  # False
print(S.isascii())  # True
print(S.removeprefix("H"))  # ello, World!
print(S.removesuffix("d!"))  # Hello, Worl
print(S.partition("o"))  # ('Hell', 'o', ', World!')
print(S.rpartition("o"))  # ('Hello, W', 'o', 'rld!')
print(S.split(",", 1))  # ['Hello', ' World!']
print(S.rsplit(" ", 1))  # ['Hello,', 'World!']
print(S.zfill(15))  # 000Hello, World!
print(S.isnumeric())  # False
print(S.isdecimal())  # False
print(S.isalnum())  # False
print(S.encode('utf-16'))  # b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00W\x00o\x00r\x00l\x00d\x00!\x00'
print(S.expandtabs())  # Hello, World! (no tabs to expand here)
print(S.swapcase())  # hELLO, wORLD!
print(S.translate(str.maketrans("Helo", "Jxyz")))  # Jxyyz, Wxrzd!
print(S.isprintable())  # True
print(S.islower())  # False
print(S.isupper())  # False