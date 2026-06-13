import calendar  #import Calendar
import re

"""
In this project i create calendar to mark the important  events such as my family's Birthday and other events.
"""

year = 2026 # make variable for current year


# in operation statement , iterate the months
for month in range (1, 13):
    cal = calendar.month(year, month)
    
    if month == 1:
        cal = re.sub( r" \b1\b", "①", cal)
        cal = re.sub(r"\b2\b","②", cal)
        
    if month == 11:
        cal = re.sub( "14","⑭", cal)
        cal = re.sub("12", "⑫", cal)
    
    if month == 7:
        
        cal = re.sub("15","⑮", cal)
        
    if month == 12:
        
        cal = re.sub("25", "㉕", cal)
   
   

    print(cal) 
    
    
    
    
   


   
    