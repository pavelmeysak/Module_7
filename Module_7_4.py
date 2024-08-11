team_1_num = 5
team_2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
task_total = score_1 + score_2
time_avg = (team1_time+team2_time)/task_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Использование %:

print('В команде Мастера кода участников: %s !' % team_1_num)
print('Итого сегодня в командах участников %s и %s !' % (team_1_num, team_2_num))

# Использование format():

print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} c !'.format(team2_time))

# Использование f-строк:

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {task_total} задач, в среднем {time_avg} секунды на задачу!.')
