
class Polynomial:


    def calculateF(self, index, num, currNum):
        # print('Round: ', index)
        if index < num:
            coeff = int(input('Enter cooef :'))
            calc = coeff**index + currNum
            # print('Calc: ', calc)
            index = index+1
            self.calculateF(index, num, calc)
        else:
            return currNum


    def calculateG(self, input):
        hold = input % 32000011
        return hold



#  Main method
p = Polynomial()
num = int(input('Please input the number of coeffiecient: '))
numArr = []

for i in range(num):
    if 0 < num < 10 ** 6:
        numArr.append(p.calculateF(0, num, 0))
        print('F(x): ', numArr[i])
    else:
        print("Number input is not in range 10**6")

