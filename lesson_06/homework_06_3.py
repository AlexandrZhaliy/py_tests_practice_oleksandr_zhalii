# =================== HOMEWORK 6.3 =======================
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for entity in lst1:
    if isinstance(entity, str):
        lst2.append(entity)

print(lst2)



