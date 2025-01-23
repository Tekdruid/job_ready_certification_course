sentence = "This is a sentence"
sentence = sentence.upper()

print(sentence)

sentence = "this IS a 1995 sentence"
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())

print(sentence.isdigit())
sentence = "1995"
print(sentence.isdigit())
sentence = "1995 "
print(sentence.isdigit())

sentence = "1995"
print(sentence.isalnum())
sentence = "1995 A"
print(sentence.isalnum())
sentence = "1995A"
print(sentence.isalnum())
sentence = "1995%A"
print(sentence.isalnum())
print(sentence.startswith("19"))
print(sentence.startswith("A"))
print(sentence.endswith("A"))
print(sentence.startswith("99",1))
print(sentence.startswith("A", -1))



