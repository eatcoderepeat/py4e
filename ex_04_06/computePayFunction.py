def computepay():
    h = input("Enter Hours: ")
    r = input("Enter Rate: ")
    h = float(h)
    r = float(r)
    if h > 40:
        ot = (h - 40) * (r * 1.5)
        return (40 * r) + ot
    else:
        return h * r

print("Pay", computepay())
