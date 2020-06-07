# To use threads you need import Thread using the following code:
from threading import Thread

# Use the sleep function to make the thread "sleep"
from time import sleep


# To create a thread in Python you'll want to make your class work as a thread.
# For this, you should subclass your class from the Thread class
class TraditonalStat(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.name = "Traditional Stat Class\n"

    def print_statclass(self):
        print(self.name)

# The run method prints ten times the message
    def run(self):
        print("Thread Starting\n")
        x = 0
        while (x < 10):
            self.print_statclass()
            sleep(2)
            x += 1
        print("Thread Ended\n")


# start the main process
print("Process Started")

# create an instance of the HelloWorld class
hello_Python = TraditonalStat()

# print the message...starting the thread
hello_Python.start()

# end the main process
print("Process Ended")
