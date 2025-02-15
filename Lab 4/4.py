from datetime import datetime 
time1 = input("Enter the 1st date (YYYY-MM-DD HH:MM:SS): ") 
time2 = input("Enter the 2nd date (YYYY-MM-DD HH:MM:SS): ") 
date1 = datetime.strptime(time1, "%Y-%m-%d %H:%M:%S") 
date2 = datetime.strptime(time2, "%Y-%m-%d %H:%M:%S") 
diff = abs(date1 - date2) 
seconds_diff = diff.total_seconds() 
print(seconds_diff)