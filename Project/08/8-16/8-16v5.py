"""
8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""

from hotel_bookings import *

booking_0 = book_room("emil", "Conac Bavaria", "06-Aug-2021", "09-Aug-2021", breakfast=True)
booking_1 = book_room("laura", "Hotel Alpin", "21-Sep-2021", "26-Sep-2021", children=1, breakfast=True, parking=True)
booking_2 = book_room("john", "Hotel Royal", "04-Jan-2022", "09-Jan-2022", 3, breakfast=False, pool=False)
booking_3 = book_room("diana", "Casa Dante", "10-Jul-2021", "11-Jul-2021", 4, 2, breakfast=False)

bookings = [booking_0, booking_1, booking_2, booking_3]

for booking in bookings:
    print(booking_info(booking))
