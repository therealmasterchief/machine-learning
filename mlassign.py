
def myfunction3(n):
    if n > 0:
        return
    print("codingal\n" * abs(n + 1), end="")
    myfunction3(n / 2)
    myfunction3(n / 3)

def myfunction4(n):
    if n > 1:
        print("codingal")
        myfunction2(n - 1)
myfunction3(5)
myfunction4(5)
