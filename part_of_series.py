# This function genarate a series element
def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x>1:
        return (6*f(x-1)-2*f(x-2))

# Checking the element of a list
def is_part_of_series(lst):
    max_ele = max(lst)
    series = []
    i = 0
    value = f(0)
    while max_ele >= value:
        series.append(value)
        i += 1
        value = f(i)
    result = set(lst).intersection(series)
    if len(result)is len(lst):
        return True
    else:
        return False


lst = [0,1,6,34]
# Return True is the element of the list in series
print(is_part_of_series(lst))
#is_part_of_series([0,1,6,34])


