marks = {
    "ashamin":20,
    "ushamin":30,
    "hasan":25
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

marks.update({"ashamin":200})
print(marks)

print(marks.get("ashamin"))