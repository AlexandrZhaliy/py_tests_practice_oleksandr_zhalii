#dictionaries - mutable
#pare key = value

# keys - unique and hashable

my_dict = {"name": "Alex",
           "age": "27",
           "has_job": True
           }
print(my_dict)

my_dict["new_key"] = "new value"
print(my_dict)

my_dict["age"] = "28"
print(my_dict)

new_dict_update = {"key1":"value1"}
my_dict.update(new_dict_update)
print(my_dict)

my_dict["new_dict_key"] = new_dict_update
print(my_dict)

#get

print(my_dict["age"])
# print(my_dict["age1"]) #there will be an error if non-existing key is requested

print(my_dict.get("key1"))
print(my_dict.get("key0")) # it's non-existing key also but "None" will be returned

