array = []
def find_idx(lst,num1,num2):
    # lst = array
    # num1 = index1 (i)
    #num2  = index2 (j)
    try:
        return lst.index(num1,num2)
    except ValueError:
        return -1

size = int(input("Enter the size"))
for i in range(size):
    array.append(int(input()))

target = int(input("Enter the target element"))

for i in range(size):
    for j in range(size - 1):
        if i + j == target:
            index = find_idx(array,i,j)
            print(index)



            
