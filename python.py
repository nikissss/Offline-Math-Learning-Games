# Variables
num = 42
pi = 3.14
text = "HelloPy"
lst = [1,2,3]
tup = (4,5,6)
dct = {"n":"Ari","a":20}
st = {7,8,9}

print(num, pi, text)
print(lst, tup, dct, st)

# Input/Output
name = input("Name: ")
age = int(input("Age: "))
print(f"Hi {name}, age {age}")

# Conditional
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# Loops
print("For loop:")
for x in range(1,6):
    print(x)

print("While loop:")
c = 1
while c <= 5:
    print(c)
    c += 1

# Iterations
x = [10,20,30]
it = iter(x)
print("Iterations:")
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# Functions
def hi():
    print("Welcome")

hi()

def add(a,b):
    return a+b

print("Sum:", add(5,3))

def fac(n):
    r = 1
    for i in range(1,n+1):
        r *= i
    return r

print("Fac(5):", fac(5))

# Lists and Dicts
fr = ["Mango","Orange","Grape"]
print("Fruits:")
for f in fr:
    print(f)

for i in range(len(fr)):
    print(i+1, fr[i])

person = {"name": "abc", "age": 19, "city": "Kathmandu"}
print(person["name"], person["age"])

for key, value in person.items():
    print(key, ":", value)
