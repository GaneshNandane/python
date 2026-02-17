# match case statements in python are similar to the switch case statements in c++ in simple words we can use them in the alternative to if else statements they are simple to write
# also we can use with if conditions and operators such as or 

# match case application program
# fact teller program on the basis of numbers
number = int(input("Enter any number: "))
def matchnumber(number):
  match number:
    case 1:
      print(f"The number {number} fact is. ")
      print(f"nepal is the only {number} country which does not have rectangular flag") 
    case 2:
      print(f"The number {number} fact is. ")
      print(f"Haiti and Paraguay are the only {number} countries whose flags have different designs on the front and back.")
    case 3:
      print(f"The number {number} fact is. ")
      print(f"Russia spans across {number - 1} continents but is the largest country in the world.")
    case 4:
      print(f"The number {number} fact is. ")
      print(f"South Africa has {number - 1} capital cities.")
    case 5:
      print(f"The number {number} fact is. ")
      print(f"The United States has {number} permanently inhabited territories.")
    case 6:
      print(f"The number {number} fact is. ")
      print(f"Spain has {number + 11} autonomous communities.")
    case 7:
      print(f"The number {number} fact is. ")
      print(f"Australia has {number} mainland states and territories.")
    case 8:
      print(f"The number {number} fact is. ")
      print(f"Bhutan measures happiness using Gross National Happiness instead of GDP.")
    case 9:
      print(f"The number {number} fact is. ")
      print(f"Canada has {number + 1} provinces.")
    case 10:
      print(f"The number {number} fact is. ")
      print(f"Antarctica has {number - 10} permanent residents.")
    case _:
      print(f"The number {number} fact is not availabel yet. ")
matchnumber(number)
