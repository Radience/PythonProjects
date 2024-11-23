import CircularQueueModule
import random

if __name__ == "__main__":
    circQue = CircularQueueModule.CircularQueue(5)
    for x in range(circQue.sizeque):
        rand = random.randint(1, 10)
        circQue.enqueue(rand)
    print("Queue is: ")
    circQue.printQueue()
