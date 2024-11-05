team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


# Использование %:
print('Использование %:')
print('В команде Мастера кода участников: %d ! ' % team1_num)
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))
print('')

# Использование format():
print('Использование format():')
print('Команда Волшебники данных решила задач: {score_2} !'.format(score_2=42))
print('Волшебники данных решили задачи за {team1_time} с !'.format(team1_time=18015.2))
print('')

# Использование f-строк:
print('Использование f-строк:')
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
