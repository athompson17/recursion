def get_fibonacci(n):

    
    if n < 0:
        print("Incorrect input")

    
    elif n == 0:
        return 0

    
    elif n == 1 or n == 2:
        return 1

    else:
        return get_fibonacci(n-1) + get_fibonacci(n-2)






def main():

    number = int(input("Enter a number"))

    print(get_fibonacci(number))




if __name__ == '__main__':
    main()