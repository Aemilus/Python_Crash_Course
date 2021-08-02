def book_room(name, hotel, checkin, checkout, adults=2, children=0, **facilities):
    """Makes a hotel booking/reservation."""
    booking = {
        "name": name,
        "hotel": hotel,
        "checkin_date": checkin,
        "checkout_date": checkout,
        "adults": adults,
        "children": children
    }
    for facility_k, facility_v in facilities.items():
        booking[facility_k] = facility_v
    print("Your booking order has been processed.")
    return booking


def booking_info(booking):
    """Returns details of a hotel reservation/booking."""
    output = "\nThis reservation is under name: {0}\n".format(booking["name"])
    output += "Booking details:\n"
    line = "\t- {0:15}: {1:>15}\n"
    for booking_k, booking_v in booking.items():
        if booking_k == "name":
            continue
        else:
            # I've used str() because otherwise when using format() the boolean gets converted to int
            output += line.format(booking_k, str(booking_v))

    return output
