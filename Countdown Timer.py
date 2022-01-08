import time
def set_countdown():
    seconds = int(input("Enter amount of seconds: "))
    print('Countdown starts now...')
    temp = seconds
    while temp != 0:
        if temp != seconds:
            print('\b'*len(str(temp)), end='')
        time.sleep(1)
        temp -=1
        print(temp, end='')
    print("\nCountdown ended...\n")
print("this countdown timer")
while 1:
    Selection = input("Do you want to set a Countdown (y/n): ")
    if 'y' in Selection.lower():
        set_countdown()
    elif 'n' in Selection.lower():
        print("Existing...")
        break
    else:
        print('invalid input... please try again')