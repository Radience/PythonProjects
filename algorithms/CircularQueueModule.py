class CircularQueue:
    def __init__(self, size):
        self.sizeque = size
        self.queue = [0] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if self.isEmpty():
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.sizeque
            if self.rear == self.front:
                print("Queue is full. Cannot enqueue.")
                self.rear = (self.rear - 1 + self.sizeque) % self.sizeque
            else:
                self.queue[self.rear] = item

    def dequeue(self):
        item = -1
        if not self.isEmpty():
            item = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.sizeque
        else:
            print("Queue is empty. Cannot dequeue.")

        return item #optional return for check of dequeue element

    def peek(self):
        if not self.isEmpty():
            return self.queue[self.front]
        else:
            print("Queue is empty. No peek value.")

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def printQueue(self):
        if(self.front == -1):
            print("Is empty. Cannot print.")
        elif(self.rear >= self.front):
            for x in range(self.front, self.rear + 1):
                print(self.queue[x], end = " ")
            print()
        else:
            for x in range(self.front, self.sizeque):
                print(self.queue[x], end = " ")
            for x in range(0, self.rear + 1):
                print(self.queue[x], end = " ")
            print()
