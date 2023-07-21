def num_rec(num):
    if num == 0:
        return 0
    num_rec(num - 1)
    print(num)
    return 1

print("Enter the number")
num = int(input())
num_rec(num)
