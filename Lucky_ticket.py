'''На вход даётся строка из шести цифр.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
Выводим "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.'''
ticket_number = str(input())
first_sum = int(ticket_number[0])+int(ticket_number[1])+int(ticket_number[2])
second_sum = int(ticket_number[3])+int(ticket_number[4])+int(ticket_number[5])
if first_sum == second_sum:
  print('Счастливый')
else:
  print('Обычный')