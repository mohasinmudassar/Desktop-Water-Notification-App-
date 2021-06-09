#Simple Push Notification:

"""
from win10toast import ToastNotifier
import time

while True:
    current_time=time.strftime("%H:%M:%S")
    if current_time =="04:00:00":
        print(current_time)
        break
    else :
        pass

hr = ToastNotifier()

hr.show_toast("alarm" , "this is the message") """



#Water Notification 30 mins :

"""
from win10toast import ToastNotifier
import time

while True:
    hr = ToastNotifier()

    hr.show_toast("alarm", "Drink Water", duration=5)

    time.sleep(60  * 30)"""

 
#Water Notification App Using Kivy :


from win10toast import ToastNotifier
import time
print(" Enter your Remainder time = ")
a = input(int())
while True:
    hr = ToastNotifier()

    hr.show_toast("alarm", "Drink Water", duration=5)

    time.sleep(int(a))
