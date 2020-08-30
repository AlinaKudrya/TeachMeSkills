def decorator(func):
    def check(list):
        new_list = [i for i in list if i % 2 != 0]
        return func(new_list)
    return check

@decorator
def i_need_list(list):
    print(list)

numbers = [1,2,3,4,5,6]
i_need_list(numbers)