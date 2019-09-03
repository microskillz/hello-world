import time
import threading


class Philosopher(threading.Thread):

    def __init__(self, pid, sticks, stomachCapacity=3):

        threading.Thread.__init__(self)
        self.pid = pid
        self.sticks = sticks
        self.amount = 0
        self.stomachCapacity = stomachCapacity

    def run(self):

        if self.pid % 2 == 0:
            self.run_even()

        else:
            self.run_odd()

        if self.amount < self.stomachCapacity:

            time.sleep(0.1)
            self.run()

    def run_even(self):

        # Even philosophers are greedy and always wait for the next chopstick and
        # never put down a chopstick until they have eaten.
        i1 = pid
        i2 = (pid + 1) % len(sticks)
        print("Philosopher " + str(self.pid) +
              " is waiting for the first stick")
        self.sticks[i1].acquire()
        print("Philosopher " + str(self.pid) + " gets the left stick")
        print("Philosopher " + str(self.pid) + " waits for the second stick")
        self.sticks[i2].acquire()
        print("Philosopher " + str(self.pid) + " has acquired the right stick")
        self.amount += 1
        print("Philosopher " + str(self.pid) + " eats")
        self.sticks[i2].release()
        print("Philosopher " + str(self.pid) + " has released the right stick")
        self.sticks[i1].release()
        print("Philosopher " + str(self.pid) + " has released the left stick")

    def run_odd(self):

        # Odd numbered philosophes are generous. If they cannot get the second stick
        # they will put down the first and wait to try again.
        i1 = self.pid
        i2 = (self.pid + 1) % len(self.sticks)
        # setting the argument to False makes it so that the thread is not locked and instead
        # the acquire method returns a boolean for whether that thread got the lock or not.
        print("Philosopher " + str(self.pid) +
              " is trying to pick up the left stick.")

        if self.sticks[i1].acquire(False):
            print("Philosopher " + str(self.pid) +
                  " has picked up the left stick.")
        print("Philosopher " + str(self.pid) +
              " is trying to pick up the right stick")

        if self.sticks[i2].acquire(False):
            print("Philosopher " + str(self.pid) +
                  " picked up the right stick")
            self.amount += 1
            print("Philosopher " + str(self.pid) + " has eaten")
            self.sticks[i2].release()
            print("Philosopher " + str(self.pid) +
                  " has released the right stick")
            self.sticks[i1].release()
            print("Philosopher " + str(self.pid) +
                  " has released the left stick")

        elif():
            print("Philosopher " + str(self.pid) +
                  " has failed to get the second stick and released the left stick")
            print("Philosopher " + str(self.pid) + " is waiting to try again.")
            self.sticks[i1].release()
            time.sleep(0.1)
            self.run()

        else:
            print("Philosopher " + str(self.pid) +
                  "has failed to get the first stick and waits to try again.")
            time.sleep(0.1)
            self.run()


numPhilosophers = 5
sticks = []
philosophers = []
amounts = []
for i in range(numPhilosophers):
    sticks.append(threading.Lock())
    amounts.append(0)

for pid in range(numPhilosophers):
    philosophers.append(Philosopher(pid, sticks, 2))

for philosopher in philosophers:
    philosopher.start()

for philosopher in philosophers:
    philosopher.join()

for philosopher in philosophers:
    print(philosopher.amount)

print("Finished!")
