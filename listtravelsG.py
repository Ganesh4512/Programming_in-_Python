print("Demonstrate the Python programming")

def main():
    Arr = list()

    print("enter how many element ypu want to store ?")
    size=int(input())

    print("enter the values")

    for i in range(0,size):
        no = int(input())
        Arr.append(no)

    print(Arr)

if __name__ == "__main__":
    main()