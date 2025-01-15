# Timer
def timer(t):
    import time
    import sys
    
    while t > 0:
        time.sleep(1)
        t -= 1
        if t == 10:
            print(f"{t} seconds left!") flush=True)
            sys.stdout.flush()
            
    print("Time's up!")
    
    return True

timer(11)