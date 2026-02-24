# CIVE 442 Tool 1.py


name = input("Please enter your name:")
print("Hello,", name, "and welcome to the annual radon inhalation tool. This tool requires three inputs: last radon test reading, hours spent in the basement per week on average, and activity level while in the basement.")

# Unit selection loop with error prevention
while True:
    print("Please choose the unit of your last radon test reading: 1. pCi/L 2. Bq/m3")
    try:
        unit = float(input())
    except ValueError:
        print('Invalid input. Please enter a number (EX: input "one" as 1.)')
        continue
    if unit == 1 or unit == 2:
        break
    else:
        print("Invalid unit selection. Please choose either 1 or 2.")
while True:
    try:
        if unit == 1:
            print("Please enter your last radon test reading in pCi/L:")
        else:
            print("Please enter your last radon test reading in Bq/m3:")
        
        reading = float(input())
        break 
    except ValueError:
        print("Invalid input. Please enter a numerical value (EX: 4.2).")
if unit==1:
    if reading<4:
        print("Your radon level is low.")
    elif reading>=4 and reading<10:
        print("Your radon level is moderate. Consider taking action to reduce your radon levels.")
    else:
        print("Your radon level is high. It is recommended that you take immediate action to reduce your radon levels.")
elif unit==2:
    if reading<148:
        print("Your radon level is low.")
    elif reading>=148 and reading<370:
        print("Your radon level is moderate. Consider taking action to reduce your radon levels.")
    else:
        print("Your radon level is high. It is recommended that you take immediate action to reduce your radon levels.")

# Hours spent in the basement input with error prevention
while True:
    try:
        print("Please enter the average number of hours you spend in the basement per week as a whole number:")
        hours = float(input())
        if hours.is_integer() and 0 <= hours <= 168:
            hours = int(hours)
            break
        else:
            print("Invalid input. Please enter a whole number (EX: 10) or check that the number is between 0 and 168.")
    except ValueError:
        print("Invalid input. Please enter a numerical value (EX: 10).")

# Activity level input with error prevention
while True:
    print("Please select your activity level while in the basement: 1. Low (sitting, light activities) 2. Moderate (standing, walking) 3. High (heavy physical activity)")
    try:
        activity = float(input())
    except ValueError:
        print('Invalid input. Please enter a number (EX: input "one" as 1.)')
        continue
    if activity == 1 or activity == 2 or activity == 3:
        break
    else:
        print("Invalid activity level selection. Please choose either 1, 2, or 3.")

# Normalizing radon concentration, converting activity level to breathing rate in m3/hour, and calculating annual radon inhalation dose
if unit == 1: # pCi/L to Bq/m3
    concentration_bq = reading * 37 
else:
    concentration_bq = reading
if activity == 1:
    breathing_rate = 0.6  
elif activity == 2:
    breathing_rate = 1.2  
else:
    breathing_rate = 2.0  
annual_hours = hours * 52

# Final calculation of annual radon inhalation dose in Bq or piC
annual_inhalation_dose = concentration_bq * breathing_rate * annual_hours
if unit == 1:
    print("Your estimated annual radon inhalation dose is approximately", round(annual_inhalation_dose/27.027, 2), "pCi.")
else:    
    print("Your estimated annual radon inhalation dose is approximately", round(annual_inhalation_dose, 2), "Bq.")
print("Thank you for using the annual radon inhalation tool, ", name, "! Please consider taking action to reduce your radon levels if your estimated dose is high.")