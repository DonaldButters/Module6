
def weekly_pay():
    hours_worked = int(input('Please enter your work hours. :'))
    hourly_pay_rate = int(input('Please re-enter your hourly pay rate :'))
    weekly_pay=(hours_worked * hourly_pay_rate)
    return weekly_pay
print('Your pay this week is', weekly_pay())

