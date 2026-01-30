
def check_key(dictionary, key):
    if key in dictionary:
        return "Found"
    else:
        return "Not Found"


data = {"a": 1, "b": 2}
key = "b"


result = check_key(data, key)
print(result)
