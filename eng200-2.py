import machine
import utime
from sample_code import text

rtc=machine.RTC()

file = open("temps.txt", "w")




while True:
    timestamp=rtc.datetime()
    timestring="   %04d-%02d-%02d \n    %02d:%02d:%02d"%(timestamp[0:3] +
                                                timestamp[4:7])
    text(timestring)
    
    
    