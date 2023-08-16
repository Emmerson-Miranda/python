import time
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta

# Current date
today = date.today()
print("Today's date:", today)

# Formating datet dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Current date time
before = datetime.now()
print("Before now =", before)

# Adding seconds to an existing datetime
after = before + timedelta(seconds=124)
print("After now =", after)

# Difference between two datetimes
duration = after - before

# Delta in seconds
duration_in_s = duration.total_seconds() 
print("duration in seconds =", duration_in_s)

# Delta in minutes using divmod
duration_in_m = divmod(duration_in_s, 60)[0]  
print("duration in minutes =", duration_in_m)

# Delta in minutes using timedelta
time_difference = after - before
time_difference_in_minutes = time_difference / timedelta(minutes=1)
print("duration in minutes 2=", time_difference_in_minutes)
