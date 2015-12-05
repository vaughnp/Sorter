counter = 0

def merge_sort(x):
    global counter

    if len(x) < 2:
        return x

    result,mid = [],int(len(x)/2)

    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])

    while (len(y) > 0) and (len(z) > 0):
        userChoice = raw_input(str(y[0]) + " or " + str(z[0]) + "?")
        if (userChoice == "2"):
            result.append(z.pop(0))   
        else:
            result.append(y.pop(0))
        counter += 1
        
    result.extend(y+z)
    return result

allNumbers = ["Chocolate", "Vanilla", "Cherry", "Cookie Dough", "Mint Chocolate Chip", "Neapolitan"]
print(merge_sort(allNumbers))
print("Wow! That was fast! That only took " + str(counter) + " comparisons!")
