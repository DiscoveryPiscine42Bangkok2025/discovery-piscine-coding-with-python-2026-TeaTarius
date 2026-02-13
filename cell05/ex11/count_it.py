from sys import argv

def main():
    if not len(argv) > 1:
        print("none")
        return
    print(f"parameters: {len(argv) - 1}")
    for i in argv[1:]:
        print(f"{i}: {len(i)}")

main()