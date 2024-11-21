values = [1, 2, "bransen", 4, 5]
print(values[2])

print(values[-1])

print(values[1:3])

values.insert(3, "shetty")  # insert
values.append("End")  # Appending
values[2] = "BRANSEN"  # Updating
del values[0]

print(values)

# Tuple - Same as LIST Data Type but immutable

val = (1, 2,)

# Dictionary

dic = {"a": 2, 4: "first name", "c": "Hello World"}
print(dic[4])
print(dic["c"])

dict = {}

dict["firstname"] = "Bransen"
dict["lastname"] = "Daniels"

print(dict)
print(dict["lastname"])
