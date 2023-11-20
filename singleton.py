import threading
class SingletonMetaclass(type):
    instances = {}
    lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls.lock:
            print(type(cls))
            if cls not in cls.instances:
                cls.instances[cls] = super().__call__(*args, **kwargs)
            return cls.instances[cls]

class FirstSingleton(metaclass=SingletonMetaclass):
    def __init__(self, **kwargs):
        print("Creating the first singleton instance...")
        self.private_name = kwargs.get('name', None)
        self.family_name = kwargs.get('family', None)
    
    def printData(self):
        print(f"name: {self.private_name} family: {self.family_name}")


class SecondSingleton(metaclass=SingletonMetaclass):
    def __init__(self):
        print("Creating the second singleton instance...")

if __name__ == "__main__":
    # Create two instances of the first singleton class
    instance1 = FirstSingleton(name='matan', family='Elitzur')
    instance1.printData()
    #instance2 = FirstSingleton() // This is also working
    instance2 = FirstSingleton(name='XXX', family='YYYY')
    instance2.printData()

    # Check if the two instances are the same
    print("Are the two first singleton instances the same?", instance1 is instance2)

    # Create two instances of the second singleton class
    instance3 = SecondSingleton()
    instance4 = SecondSingleton()

    # Check if the two instances are the same
    print("Are the two second singleton instances the same?", instance3 is instance4)

    # Check if the two singleton classes share the same instance
    print("Do the two singleton classes share the same instance?", instance1 is instance3)