hours = input("Enter Hours:")
h = float(hours)
rate = input("Enter Rate:")
overtimeRate = float(rate) * 1.5

if h > 40 :
    overtimeHours = h - 40
    h = 40

pay = (overtimeHours * overtimeRate) + (h * float(rate))
print(pay)
