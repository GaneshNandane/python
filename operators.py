# ==========================================================
#                    OPERATORS IN PYTHON
# ==========================================================

# Operators are special symbols in Python that are recognized
# by the Python interpreter.
#
# Each operator has a specific meaning and is used to perform
# operations on variables, values, and different data types.
#
# Mainly there are several types of operators in Python:
#
# 1. Arithmetic Operators    → +, -, *, /, %, **, //
# 2. Relational Operators    → <, <=, >, >=, ==, !=
# 3. Logical Operators       → and, or, not
# 4. Bitwise Operators       → &, |, ^, ~, <<, >>
# 5. Assignment Operators    → =, +=, -=, *=, %=, /=, //=, **=, &=, |=, ^=, <<=, >>=, :=
# 6. Identity Operators      → is, is not
# 7. Membership Operators    → in, not in


# ==========================================================
# 1. ARITHMETIC OPERATORS
# ==========================================================
# These operators are used to perform mathematical operations.

value1 = 5
value2 = 7

print(f"Addition of two values is:          {value1 + value2}")   # Adds two numbers
print(f"Subtraction of two values is:       {value1 - value2}")   # Subtracts second from first
print(f"Multiplication of two values is:    {value1 * value2}")   # Multiplies two numbers
print(f"Division of two values is:          {value1 / value2}")   # Returns float result
print(f"Modulus of two values is:           {value1 % value2}")   # Returns remainder
print(f"Exponent of two values is:          {value1 ** value2}")  # Power operation
print(f"Floor division of two values is:    {value1 // value2}")  # Removes decimal part


# ==========================================================
# 2. RELATIONAL (COMPARISON) OPERATORS
# ==========================================================
# These operators compare two values and return True or False.

value3 = 9
value4 = 10

print(f"value3 is less than value4:                 {value3 < value4}")
print(f"value3 is less than or equal to value4:     {value3 <= value4}")
print(f"value3 is greater than value4:              {value3 > value4}")
print(f"value3 is greater than or equal to value4:  {value3 >= value4}")
print(f"value3 is equal to value4:                  {value3 == value4}")
print(f"value3 is not equal to value4:              {value3 != value4}")


# ==========================================================
# 3. LOGICAL OPERATORS
# ==========================================================
# Logical operators combine conditional statements.
# They always work with Boolean values (True / False).

value5 = True
value6 = False 

print(f"value5 AND value6:                          {value5 and value6}")  # True only if both are True
print(f"value5 OR value6:                           {value5 or value6}")   # True if at least one is True
print(f"NOT value5 (opposite of value5):            {not value5}")         # Reverses Boolean value


# ==========================================================
# 4. BITWISE OPERATORS
# ==========================================================
# Bitwise operators work on binary (bit-level) representation of integers.

value7 = 4   # Binary: 0100
value8 = 3   # Binary: 0011

print(f"Bitwise AND of value7 and value8:           {value7 & value8}")
print(f"Bitwise OR of value7 and value8:            {value7 | value8}")
print(f"Bitwise XOR of value7 and value8:           {value7 ^ value8}")
print(f"Bitwise NOT of value7:                      {~value7}")
print(f"Left shift value7 by 1:                     {value7 << 1}")
print(f"Right shift value7 by 1:                    {value7 >> 1}")


# ==========================================================
# 5. ASSIGNMENT OPERATORS
# ==========================================================
# Assignment operators assign values and update values.

value9 = 10

value9 += 5
print(f"After += 5:                                 {value9}")

value9 -= 3
print(f"After -= 3:                                 {value9}")

value9 *= 2
print(f"After *= 2:                                 {value9}")

value9 /= 4
print(f"After /= 4:                                 {value9}")

value9 //= 2
print(f"After //= 2:                                {value9}")

value9 **= 2
print(f"After **= 2:                                {value9}")


# Walrus operator (:=)
# It assigns a value to a variable inside an expression.

print(f"Using walrus operator:                      {(temp := 20)}")
print(f"Value stored in temp:                       {temp}")


# ==========================================================
# 6. IDENTITY OPERATORS
# ==========================================================
# These operators check whether two variables refer to the same object in memory.

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(f"list1 is list2:                             {list1 is list2}")
print(f"list1 is list3:                             {list1 is list3}")
print(f"list1 is not list3:                         {list1 is not list3}")


# ==========================================================
# 7. MEMBERSHIP OPERATORS
# ==========================================================
# These operators check whether a value exists in a sequence.

numbers = [10, 20, 30, 40]

print(f"20 in numbers:                              {20 in numbers}")
print(f"50 not in numbers:                          {50 not in numbers}")

text = "Python Programming"

print(f"'Python' in text:                           {'Python' in text}")
print(f"'Java' in text:                             {'Java' in text}")
