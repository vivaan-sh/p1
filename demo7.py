def main():
    numbers = [3, 5, 3, 2, 5, 1, 2]

    unique = []
    for n in numbers:
        if n not in unique:
            unique.append(n)

    print(unique)

if __name__ == "__main__":
    main()


