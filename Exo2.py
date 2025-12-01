a = float(input("le premier nombre : "))
b = float(input("deuxieme : "))
c = float(input("troisieme:"))


median = a + b + c - max(a, b, c) - min(a, b, c)

print("le mediane est ")
print(median)
