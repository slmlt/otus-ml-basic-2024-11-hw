days = int(input())

whole_weeks = days // 7
leftover = days % 7
holidays_in_leftover = (leftover // 5) * (leftover % 5)
print(whole_weeks * 2 + holidays_in_leftover)
