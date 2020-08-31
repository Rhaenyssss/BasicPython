#Asking for data
while True:
    hours = input('Q: How many hours have you worked this week? ')
    try:
        hours = float(hours)
        break #Mission complete, now ask for rate
    except:
        print('Please enter a valid number')
        continue #Try again until valid
while True:
    rate = input('Q: What is your hourly pay rate? ')
    try:
        rate = float(rate)
        break
    except:
        print('Please enter a valid number')
        continue
#Checking for overtime
overtimeornot = input('Q: Does your company offer overtime rates? (y/n) ')
if overtimeornot[0] == 'y' or overtimeornot[0] == 'Y':
    while True:
        otrates = input('Q: How many more times is your overtime pay? (e.g. 1.5,2.0) ')
        try:
            otrates = float(otrates)
            break
        except:
            print('Please enter a valid number')
            continue
    while True:
        ottime = input('Q: After which hours does it counts as overtime? ')
        try:
            ottime = float(ottime)
            break
        except:
            print('Please enter a valid number')
            continue
    pay = ottime*rate + (hours-ottime)*(otrates*rate)
    print('Pay(OT+):', pay)
if overtimeornot[0] == 'n' or overtimeornot[0] == 'N':
    pay = hours*rate
    print('Pay(OT-):', pay)
