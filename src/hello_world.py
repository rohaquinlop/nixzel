import sys


def main():
    file_location: str = sys.argv[0]
    print("File location:", file_location)
    print("Args:", sys.argv[1:])


if __name__ == "__main__":
    main()
