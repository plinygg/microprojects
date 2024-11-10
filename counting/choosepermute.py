def factorial(n):
    n = int(n)
    res = 1
    for i in range(1, n+1):
        res *= i
        
    return res


def main():
    print("""here are your current choices for calculations:
          c: n choose r - n!/r!(n-r)!
          p: n permute r - n!/(n-r)!
          f: n factorial - n!
          """)
    
    choice = input()
    
    if choice == "c":
        n = input('input your n: \n')
        r = input('input your r: \n')
        res = factorial(n) / (factorial(r) * factorial(int(n)-int(r)))
        print("{a} choose {b} is {c}.".format(a=str(n),b=str(r),c=str(res)))
    elif choice == "p":
        n = input('input your n: \n')
        r = input('input your r: \n')
        res = factorial(n) / (factorial(int(n)-int(r)))
        print("{a} permute {b} is {c}.".format(a=str(n),b=str(r),c=str(res)))
    elif choice == "f":
        n = input('what number do you want the factorial of?')
        print('your input factorialed is', factorial(n))
    else:
        main()
        
        
main()