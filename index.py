
a_string = "like this"
a_number = 3
a_boolean = False
a_float = 3.12
a_none = None

print(type(a_none))
print(type(a_float))


days = ["Mon" , "Tue", "Wed", "Thur", "Fri"]
print(days)
print(type(days))

print("Mon" in days)
print("Man" in days)
print(days[3])
print(len(days[3]))

print(days)
days.append("Sat")
days.reverse()
print(days)


days_1 = ("Mon" , "Tue", "Wed", "Thur", "Fri")
print(type(days_1))



nico = {
"name" : "Nico",
"age" : 29,
"korean" : True,
"fav_food": ["Kinchi", "Sashimi"]
}

print(nico["fav_food"])
nico["handsome"] = True
print(nico) 


print(len("ddfasdfsdafsdafdfaf"))

age = "18"
print(age)
print(type(age))
print("-------------------------")
n_age = int(age)
print(n_age)
print(type(n_age))

print("------------------Day 2 of 14--------------------")
def say_hello():
  print("hello")
  print("by")

say_hello()


def say_bye(who):
  print("bye!", who)

say_bye("Nicolas")


def plus(a, b):
  print(a + b)

# default value. 함수 호출시 b인자가 없으면 defalut값을 사용
def minus(a, b = 0):
  print(a - b)

plus(2, 5)
minus(2)


def say_hi(name="anonymous"):
  print("hi!", name)

say_hi()
say_hi("nico")

print("<---------------------->")

def p_plus(a, b):
  print(a + b)

def r_plus(a, b):
  return a + b

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)
#     None      5

print("<---------------------->")

def done(a, b):
  return a + b
  print("rprddkkdkdkdkkdd", True)

r_done = done(2, 4)
print(r_done)

result = done(b=30, a =1)
print(result)


def say_good(name, age):
  return f"Hello {name} you are {age} years old"

def say_bad(name, age):
  return "Hello " + name + " you are " + age + " years old" 

good = say_good(age="12", name="nico")
bad = say_bad("ddod", "12")
print(good)
print(bad)