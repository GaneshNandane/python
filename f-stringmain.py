letter="Hey my name  is {1} and I am from {0}"
country="India"
name="Harry"
print(letter.format(country, name))
print(f"Hey my name is {name} and i am from {country}")
print(f"we use f-strings like this: Hey my name is {{name}} and I am from{{country}}")
price=49.999999
txt=f"for only {price: .2f} dollors!"
print(txt)
# print(txt.format())
print(type(f"{2*30}"))