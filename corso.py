name = " test"
print(test)


my_list = [10,5,8,3,11,2]

type (my_list)
len(my_list)
my_list[0]

my_list[1]


len(my_list[1:])

animals = [ "cane","gatto","topo"]
"uomo" in animals
"gatto" in animals
 animals.remove("gatto")
animals

animals.append("bestia")
print(animals)

animals.insert(1,"sorcio")
print(animals)

my_tuple = (10,5,8,3,9)

type(my_tuple)
my_tuple[3]
my_tuple[:3]
my_tuple[0]=4

my_tuple.index(5)
my_tuple.count(5)

hello = "hello python"
len(hello)

names = {"Giuseppe", " Federico", " Antonino","MAtteo","Federico"}
print (names)
names.add("Lorenzo")
print (names)
names.remove("Antonino")

items = {"latte":3, 'riso':2, 'tofu':5}
type(items)
print (items)

items["cereali"] = 1
items

items ["yogurt"] = {"fragola":2, "bianco":3}

items["yogurt"]["fragola"]



n = int(input("Fino a che numero stampare ? "))

for i in range(0,n):
    print(i)


n = int(input("quanti numeri fibonacci ? "))
fib_num= 0
next_fib_num = 1

for i in range(n):
    #tmp=next_fib_num
    #next_fib_num += fib_num
    fib_num, next_fib_num = next_fib_num, next_fib_num +fib_num

    print(f"{i+1} numero di fib = {fib_num}")



a = "cane"
b= "gatto"
a,b=b,a

print (a , b)

shopping = ["tofu","latte", "riso", "yogurt"]
for i,entry in enumerate(shopping):
    print(f"{i}) {entry}")
