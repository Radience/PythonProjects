import random

class Itiss:
    def __init__(self, front, rear):
        self.arr = [x for x in range(front, rear)]
        self.arrLen = len(self.arr)

    def deleteNumberFromArray(self, randNumb):
        self.arr.pop(randNumb)

    def solutionTask(self):
        j = 1
        self.arr.sort()
        print("Array: ", self.arr)
        for x in self.arr:
            if self.arrLen > max(self.arr):
                print("Its number: " , self.arrLen)
                break
            if x-j == 1:
                print("Its number: " , j)
                break
            else:
                j += 1


if __name__ == "__main__":
    rear = int(input("Enter rear more than 1: "))
    sequence = Itiss(1, rear+1)
    sequence.deleteNumberFromArray(random.randint(0, rear-1))
    sequence.solutionTask()
