ticket = input('Введите номер билета: ')
lucky_sum_1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
lucky_sum_2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if lucky_sum_1 == lucky_sum_2:
    print('Поздравляем! У вас счастливый билет!')
else:
    print('К сожалению, ваш билет не счаcтливый :(')
