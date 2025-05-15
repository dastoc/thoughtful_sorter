from sorter import sort

def main():
    print("Package 1:", sort(100, 100, 100, 10))  # Output: STANDARD
    print("Package 2:", sort(200, 50, 50, 25))    # Output: REJECTED
    print("Package 3:", sort(150, 10, 10, 10))    # Output: SPECIAL

if __name__ == "__main__":
    main()