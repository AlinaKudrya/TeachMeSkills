def decorator_change_arguments(function_to_decorate):
    def changer(name, lastname, age):
        function_to_decorate(age, lastname, name)
    return changer


@decorator_change_arguments
def original_func(name, lastname, age):
    print(name, lastname, age)


original_func('Robert', 'Robertovich', '45')
