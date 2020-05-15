import time
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
