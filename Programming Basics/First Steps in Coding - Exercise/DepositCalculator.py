deposit = float(input())
months = int(input())
percent = float(input())

# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
sum = deposit + months * ((deposit * percent / 100) /12)
print(sum)
