from functools import reduce

# We can use the eval() function only in safe environments.
def operate(operator, *args):
    return reduce(lambda x, y: eval(f"{x}{operator}{y}"), args)
