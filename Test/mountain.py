# Main method

class Mountains:

    def lookLeft(self, arr, curr, middle, count, highest):
        # print("Curr before: ", curr)
        if curr==-1:
            return count
        else:
            if highest < arr[curr]:
                hightest = arr[curr]
                count = count + 1

            return self.lookLeft(arr, curr-1, middle, count, highest)


        # print("Curr after: ", curr)


    def lookRight(self, arr, curr, middle, count, highest):
        # print("Curr before: ", curr)

        if curr==(len(arr)):
            return count
        else:
            if highest < arr[curr]:
                hightest = arr[curr]
                count = count + 1
            return self.lookRight(arr, curr+1, middle, count, highest)


        # print("Curr after: ", curr)





# number of mountains
n = int(input())
m = Mountains()

# # height of each mountain
# a = list(map(int,input().strip().split()))[:n]
numArr = []
count = []

# Get height for each mountain
for i in range(n):
    numArr.append(input('Input mountain height '))

hold = 1
for i in range(n):
    # Look for each mountain
    hold = hold + m.lookLeft(numArr, i-1, i, 0, numArr[i])
    # print('Left :', hold)
    hold = hold + m.lookRight(numArr, i+1, i, 0, numArr[i])
    # print('Right :', hold)
    count.append(hold)

print(count)





