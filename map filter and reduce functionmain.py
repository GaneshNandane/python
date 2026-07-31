# # Map
def cube (x):
    return x*x*x

print(cube(2))
1=[1, 2, 4, 6, 4, 3]
newl=[]
for item in l:
    newl.append(cube(item))

newl=list(map(lambda x: x*x*x, l))

print(newl)

# # FILTER
def filter_function(a):
      return a>2

newnewl=list(filter(filter_function, l))

print(newnewl)

from functools import reduce
#list of numbers
numbers=[1,2,3,4,5]

#calculate the sum of the numbers using the reduce function

def mysum(x, y):
    return x+y

sum=reduce(mysum, numbers)

#print the sum
print(sum)