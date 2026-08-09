# Before filling the name and Date in the letter
letter = """Dear <|Name|>,
\tyou are selected!
<|Date|>\n"""
print(letter)

# After filling the name of the person in place of the <|Name|>
print(letter.replace("<|Name|>", "Ganesh"))

# After filling the name and date in place of the <|Name|> and <|Date|>
print(letter.replace("<|Name|>", "Ganesh").replace("<|Date|>", "09 August 2026"))
