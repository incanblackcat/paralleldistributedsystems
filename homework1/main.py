import time
import threading


class thread(threading.Thread):
    __kill = False
    __count = 0

    def __init__(self, threadNumber):
        threading.Thread.__init__(self)
        self.__threadNumber = threadNumber

    def kill(self):
        self.__kill = True

    def calculate(self):
        while not self.__kill:
            time.sleep(self.__threadNumber % 1 + 2)
            self.__count += 1
        print("count: " + str(self.__count))

    def get_Count(self):
        return self.__count

    def run(self):
        self.calculate()


def newThread(num):
    allThreads = []
    for i in range(num):
        t = thread(i)
        t.start()
        allThreads.append(t)

    for i in allThreads:
        i.kill()

    for i in allThreads:
        i.join()

       return None


operations = 0

for t in allThreads:
    operations += t.get_Count()

print('Operations: ' + str(operations))


def main():
    print('Currently running 1 thread')
    newThread(1)
    print('Currently running 2 threads')
    newThread(2)
    print('Currently running 4 threads')
    newThread(4)
    print('Currently running 8 threads')
    newThread(8)


print()

main()
