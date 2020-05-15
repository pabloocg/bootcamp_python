import time
from random import randint
import getpass

def log(func):
    
    def inner1(*args, **kwargs):
        begin = time.time()
        value = func(*args, **kwargs)
        func_name = str(func.__name__)
        func_name = func_name.replace("_", " ").title()
        f = open ('machine.log','a')
        exec_time = time.time() - begin
        print(f"\033[;35m({getpass.getuser()})Running\033[0;m: {func_name}    \t[ exec-time = {exec_time:.3f} ms ]", file=f)
        f.close()
        return value

    return inner1

class CoffeeMachine():
    
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
