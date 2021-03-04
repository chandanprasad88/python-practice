# this program is to add elements of array
def array_sum(arr):
    sum = 0
    for item in arr:
        sum += item
    return sum

# running main program
arr = [1, 2, 3, 4, 5]
sum = array_sum(arr)
print(sum)
