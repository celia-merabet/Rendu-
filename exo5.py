result = []

for x in range(1500, 2701):  # 2701 car 2700 est inclus
    if x % 7 == 0 and x % 5 == 0:
        result.append(x)

print(result)
