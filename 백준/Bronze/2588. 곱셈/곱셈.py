A = int(input())
B = list(map(int, input()))
print(A*(B[-1]))
print(A*(B[-2]))
print(A*(B[-3]))
print(A*(B[-1])+A*(B[-2])*10+A*(B[-3])*100)