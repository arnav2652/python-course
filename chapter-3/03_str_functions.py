#HOW TO CHECK THE LENGTH OF STRING
name = "mahadev"

print(len(name))

#HOW TO USE STRING.ENDSWITH
name = "mahadev"
print(name.endswith("nav")) #It is False Statement

name = "mahadev"
print(name.endswith("dev")) #It is True Statement

name = "mahadev"
print(name.endswith("Dev")) #It is also check whether the string is capital or small letter 
# and this function is casesensetive

#HOW TO USE STRING.STARTSWITH
name = "mahadev"
print(name.startswith("nav")) #It is False Statement

name = "mahadev"
print(name.startswith("mah")) #It is True Statement

name = "mahadev"
print(name.startswith("Mah")) #It is also check whether the string is capital or small letter 
# and this function is casesensetive

#HOW TO USE STRING.COUNT
name = "arnnnnav"
count = name.count("n")
print(count)

#HOW TO CAPITALIZED THE STRING
name = "arnav"
capitalised_string = name.capitalize()
print(capitalised_string) # Output: "Arnav"

#HOW TO USE STRING.FIND()
text = "hello world"
index = text.find("world")
print(index)  # Output: 6

#HOW TO USE STRING.REPLACE
name = "arnav"
replaced_name = name.replace("n","a")
print(replaced_name) 



#SOME MOST USED STRING FUNCTION IN PYTHON

# Sample string
text = "  hello World  "

# 1. find() - index of first occurrence
print("1.", text.find("World"))        # → 8

# 2. len() - length of the string
print("2.", len(text))                 # → 15

# 3. lower() and upper()
print("3.", text.lower())              # → '  hello world  '
print("4.", text.upper())              # → '  HELLO WORLD  '

# 4. strip(), lstrip(), rstrip()
print("5.", text.strip())              # → 'hello World'
print("6.", text.lstrip())             # → 'hello World  '
print("7.", text.rstrip())             # → '  hello World'

# 5. replace()
print("8.", text.replace("World", "Python"))  # → '  hello Python  '

# 6. split() and join()
words = text.strip().split()           # ['hello', 'World']
print("9.", words)
print("10.", "-".join(words))          # → 'hello-World'

# 7. startswith() and endswith()
print("11.", text.strip().startswith("hello"))  # → True
print("12.", text.strip().endswith("World"))    # → True

# 8. 'in' keyword
print("13.", "hello" in text)          # → True

# 9. title()
print("14.", text.strip().title())     # → 'Hello World'

# 10. capitalize()
print("15.", text.strip().capitalize())  # → 'Hello world'

# 11. count()
print("16.", text.count("l"))          # → 3

#BELOW THE STRING FUNCTION IS NOT VERY MOST USED FUNCTION IN PYTHON.
# BUT MOST USED FUNCTION IN PYTHON

# 12. zfill()
print("17.", "42".zfill(5))            # → '00042'

# 13. isalpha(), isdigit(), isalnum()
print("18.", "hello".isalpha())        # → True
print("19.", "123".isdigit())          # → True
print("20.", "abc123".isalnum())       # → True

# 14. swapcase()
print("21.", text.swapcase())          # → '  HELLO wORLD  '

# 15. partition()
print("22.", "key=value".partition("="))  # → ('key', '=', 'value')

# 16. rfind()
print("23.", "hello hello".rfind("hello"))  # → 6

# 17. format() and f-strings
name = "Alice"
print("24.", "Hello, {}".format(name))     # → 'Hello, Alice'
print("25.", f"Hi, {name}")                # → 'Hi, Alice'
