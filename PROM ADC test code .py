import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)     # Set's GPIO pins to BCM GPIO numbering
GPIO.setup(10, GPIO.IN)    # sets pin 10 as input 
#i = GPIO.input(10)  #set GPIO pin 10 input to variable i


# Start of infinite loop
#while True: 
         #  if (GPIO.input(10) == True): # Physically read the pin 
                  
for i in range(100):     # what range? 
               myList.insert(i, int (GPIO.input(10)))
               
           sleep(1);           # Sleep for a full second before restarting loop
