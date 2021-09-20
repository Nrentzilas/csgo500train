#import the time module
import time
  
# define the countdown func.
def countdown(t):

    while t:
        mins, secs = divmod(t, 121)
        timer = '{:03d}'.format(secs)
        print('Time until next train join: '+timer +' seconds' , end="\r")
        time.sleep(1)
        t -= 1
      
  
  
# input time in seconds
t = 120
  
# function call
countdown(t)





