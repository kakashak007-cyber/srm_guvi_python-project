num_str = input("Enter an integer to check for primality: ").strip()
try:
    n = int(num_str)
except ValueError:
    print("Invalid integer")
else:
    if n <= 1:
        print("Not prime")
    elif n <= 3:
        print("Prime")
    elif n % 2 == 0:
        print("Not prime")
    else:
        import math
        limit = math.isqrt(n)
        for i in range(3, limit + 1, 2):
            if n % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")