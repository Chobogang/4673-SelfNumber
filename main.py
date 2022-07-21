arr = [i for i in range(1, 10001)]

for i in range(1, 10001) :
    a = str(i)
    for k in range(len(a)) :
        i += int(a[k])
    if i in arr :
        del arr[arr.index(i)]
    else : continue

for i in range(len(arr)) :
    print(arr[i])