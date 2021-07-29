def type_check(expected_type):
    def decorator(function):
        def wrapper(param):
            result = function(param)
            if type(param) == expected_type:
                return result
            return "Bad Type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))

