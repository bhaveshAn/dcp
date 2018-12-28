'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''


from threading import Thread
import time

def delayed_execution(f, ms):
    time.sleep(ms)
    return f()

def hello(name):
    print 'Hello {}'.format(name)
job = Thread(target=delayed_execution, args=(lambda: hello('from thread'), 0.01))
job.start()

print 'Before'
time.sleep(0.02)
print 'After'