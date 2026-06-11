people = {
    "Alex": 29,
    "Ben": 35,
    "Ivan": 18
}
print(list(people.keys()))

for name in  people.keys():
    print(name)

for age in people.values():
    print(age)

# for people in people.items():
#     print(people)
# OR
for name, age in people.items():
    print(f"My name is {name},  I am {age} years old")

