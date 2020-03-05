import time
import sys # ignore
sys.path.insert(0,'.') # ignore
#from Root.pswd import real_password

def check_password(password): # Don't change it
    if len(password) != len('1987'):
        return False
    for x, y in zip(password, "1987"):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    i = 0
    crack_pass_list = [9,9,9,9]
    while i < len(crack_pass_list):
        for number in range(0,10):
            crack_pass_list[i] = number
            print(crack_pass_list)
            crack_pass = ''.join(map(str, crack_pass_list))
            start_time = time.time()
            if check_password(crack_pass):
                return crack_pass
            exec_time = round( ((time.time() - start_time)),2)
            if exec_time > (0.1)*(i+1):
                break
        i = i + 1

print(crack_password())
