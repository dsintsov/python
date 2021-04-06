"""
№ 1. Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7.
Могут ли два билета подряд быть удачными?
"""
BIGGEST_TICKET = 999999

CURRENT_TICKET = 0
LAST_IS_LUCKY = False
while CURRENT_TICKET <= BIGGEST_TICKET:
    FACTOR = 1
    SUM = 0
    for i in range(len(str(BIGGEST_TICKET))):  # Searching the SUM of CURRENT_TICKET
        SUM += (CURRENT_TICKET // FACTOR) % 10  # getting digits from right to left
        FACTOR *= 10
    if SUM % 7 == 0:  # if current ticket is lucky
        if LAST_IS_LUCKY == True:
            print(str(CURRENT_TICKET - 1) + " and " + str(CURRENT_TICKET))
        else:
            LAST_IS_LUCKY = True
    else:
        LAST_IS_LUCKY = False
    CURRENT_TICKET += 1
exit(0)
