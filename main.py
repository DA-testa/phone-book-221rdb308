# python3

n = int(input())
phone_book = {}

for i in range(n):
    query = input().split()
    command = query[0]
    number = query[1]
    
    if command == "add"
        name = query[2]
        phone_book[number] = name
    elif command == "del"
        if number in phone_book:
            del phone_book[number]
    elif command == "find":
        if number in phone_book:
            print(phone_book[number])
        else:
            print("not found")

