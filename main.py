################################
# Hunter Tysdal
# CompSci_101_Lab
# Week 13

import time


class Clock:
    def __init__(self, second=00, minute=00, hour=00, day=''):
        self.second = second
        self.minute = minute
        self.hour = hour
        self.day = day

    def __str__(self):
        return ('Time : {:02d}:{:02d}:{:02d} {}'.format(self.hour, self.minute, self.second, self.day))

    def tick(self):
        seconds = second
        minutes = minute
        hours = hour
        days = day
        while True:
            print('{:02d}:{:02d}:{:02d} {}'.format(hours, minutes, seconds, days))
            seconds += 1
            time.sleep(1)
            if seconds == 60:
                minutes += 1
                seconds = 00
            if minutes == 60:
                hours += 1
                minutes = 00
            if hours == 13:
                hours = 1

            if hours == 12 and minutes == 0 and seconds == 0:
                if days == 'am':
                    days = 'pm'
                elif days == 'pm':
                    days = 'am'


# measure = Clock()
print('Welcome to the digital clock!')
print()
choice = ''
while choice != 'q':

    hour = int(input('What is the current hour ---> '))
    if hour >= 13 or hour < 0:
        print('That is not a valid hour interval, must be from 0-12')
        print()
        continue
    print()
    minute = int(input('What is the current minute ---> '))
    if minute >= 60 or minute < 0:
        print('That is not a valid minute interval, must be from 0 to 59')
        print()
        continue
    print()
    second = int(input('What is the current second ---> '))
    if second >= 60 or second < 0:
        print('That is not a valid second interval, must be from 0 to 59')
        print()
        continue
    print()
    day = input('Is it am or pm ---> ')
    if day != 'am' and day != 'pm':
        print('Must enter either am or pm')
        print()
        continue

    print()
    measure = Clock(second, minute, hour)
    print(measure)
    while True:
        print(measure.tick())
