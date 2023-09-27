list_1 = []
list_2 = []
num_1 = int(input('input first number'))
num_2  = int(input('input second number'))

n = None
m = None
i = 0
j = 0
dict = {}
while i < num_1:
    n = int(input())
    list_1.append(n)
    i+=1
while j < num_2:
    m = int(input())
    list_2.append(m)
    j+=1
com = list_1 + list_2
print(sorted(com))