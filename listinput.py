def main():
    Arr = list()
    print("Enter how many element you want to store ?")
    size = int(input())

    print("Plz enter the values")
    for i in range(0,size):
        no = int(input())
        Arr.append(no)

    print(Arr)
if __name__ == "__main__":
    main()
