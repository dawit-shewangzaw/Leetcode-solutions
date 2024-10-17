import threading

class Foo:
    def __init__(self):
        # Two locks: one to ensure second() waits for first(), and one for third() to wait for second()
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        
        # Lock both initially to prevent second() and third() from executing prematurely
        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # Print first
        printFirst()
        # Release the lock so second() can now execute
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for first() to release the lock
        self.lock1.acquire()
        # Print second
        printSecond()
        # Release the second lock so third() can now execute
        self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # Wait for second() to release the lock
        self.lock2.acquire()
        # Print third
        printThird()
