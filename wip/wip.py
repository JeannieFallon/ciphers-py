"""
WIP one-liner versions of rot13 and caesar
"""

# TODO do not change spaces in strings
plain = "abc 123 XYZ"
key = 27

rot13 = "".join(list(map(lambda x: chr(ord(x) + 13), plain)))
# check str.isalpha()
caesar = "".join(list(map(lambda x: chr((ord(x) + key % 26) if x else " "), plain)))
