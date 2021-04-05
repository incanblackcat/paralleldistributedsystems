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
            #time.sleep(self.__threadNumber % 1 + 2)
            self.__count += 1

    def get_Count(self):
        return self.__count

    def run(self):
        self.calculate()


def newThread(num, sleepDur):
    allThreads = []
    threadValues = []

    operations = 0
    for i in range(num):
        t = thread(i)
        t.start()
        allThreads.append(t)

    print ('\nrunning')

    time.sleep(sleepDur)


    for i in allThreads:
        i.kill()

    print('joining all threads')

    for i in allThreads:
        i.join()


    for i in allThreads:
        operations += i.get_Count()

    print('Flops = ' + str(operations/sleepDur))


def main():
    time = int(input("How long would you like to run each thread execution? "))
    print('\nCurrently running 1 thread')
    newThread(1, time)
    print('\nCurrently running 2 threads')
    newThread(2,time)
    print('\nCurrently running 4 threads')
    newThread(4, time)
    print('\nCurrently running 8 threads')
    newThread(8, time)


print()

main()
