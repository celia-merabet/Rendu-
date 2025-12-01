def test_distinct(liste):

    return len(liste) == len(set(liste))


print(test_distinct([1, 5, 7, 9]))      

print(test_distinct([2, 4, 5, 5, 7, 9]))
