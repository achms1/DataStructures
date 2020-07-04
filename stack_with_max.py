#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maximum = 0

    def Push(self, a):
        if len(self.__stack) == 0:
            self.maximum = a
            self.__stack.append(a)
        elif self.maximum < a:
            self.__stack.append(2*a-self.maximum)
            self.maximum = a
        else:
            self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        if self.__stack[-1] <= self.maximum:
            self.__stack.pop()
        else:
            self.maximum = 2*self.maximum - self.__stack[-1]
            self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.maximum


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
