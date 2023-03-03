def sum(x,y):
    x = x + y
    x = x - y
    y = x + y
    y = x + y
    y = y - x
    y = y - x
    return [y,x]
print(list(sum(10,20)))