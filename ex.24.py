bush = list()
N = int(input('input number of bushes:'))
max_n = list()
for i in range(N):
    num = int(input())
    bush.append(num)
for i in range (len(bush)-1):
    max_n.append(bush[i] + bush[i+1] + bush[i-1])
max_n.append(bush[-2] + bush[-1] + bush[0])
print(max(max_n))