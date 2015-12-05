def merge_sort(x):

    if len(x) < 2:
        return x

    result,mid = [],int(len(x)/2)

    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])

    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z.pop(0))   
        else:
            result.append(y.pop(0))

    result.extend(y+z)
    return result

allNumbers = [1,2,3,4,5,6,9,8,7,6,5]
print(merge_sort(allNumbers))
