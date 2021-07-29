def vowel_filter(function):
    def wrapper():
        letters = function()
        vowels = [v for v in letters if v.lower() in "aoueiy"]
        return vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
