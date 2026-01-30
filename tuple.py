def tuple_to_dict(tuples):
    result = {}  
    for key, value in tuples:
        result[key] = value  
    return result

def main():
    input_tuple = (("a", 1), ("b", 2))
    output_dict = tuple_to_dict(input_tuple)
    print("Input Tuple:", input_tuple)
    print("Output Dictionary:", output_dict)

if __name__ == "__main__":
    main()
