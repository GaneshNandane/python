# Generators
# Generators in Python are used to generate values one at a time as needed,
# instead of generating and storing all values in memory at once.
# This helps reduce memory usage and can improve performance when working
# with large amounts of data.

# Here is an example of a dialogue system in a game.
# The dialogue lines are generated one by one whenever they are needed,
# so the program does not need to load all dialogue into memory at once.

def dialogue_seqence():
    yield "Hero: where am i?"
    yield "Guid: welcome to the ancient ruins"
    yield "Hero: who are you?"
    yield "Guid: i am your guid i am here to help you escape the game virtual world."
    yield "Hero: how may i escape this virtual game world?"
    yield "Guid: you need to find all boss crowns and burn it into the campfire be carefull there are lots of enemy's and tricksters around here."
    yield "Hero: ok how may i suposed to find all bosses?"
    yield "Guid: just go the the southern part of the map you see the large gate you can start from there, there are easy bosses"
    yield "Hero: ok thanks for help guid."

dialogue = dialogue_seqence()

while True:
    try:
        print(next(dialogue))
        input("Press Enter to continue...")
    except StopIteration:
        print("Dialogue ended.")
        break
