def cube(number):
    return number*number*number
def by__three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(by__three(9))
print(by__three(4))