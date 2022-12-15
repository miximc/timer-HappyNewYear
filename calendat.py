# #Считается, что Вы знаете, что такое високосный год
# (делится на 4 и не делится на 100 или делится на 400)
# Считается, что Вы знаете, сколько дней в каждом месяце
# Считается известным, что в неделе 7 дней
#
#
# 1. Сегодня вторник, 13-е декабря 2022 года
# Используя только эту информацию вычислить день недели нового года.
# Подсказка: правильный ответ: воскресенье
today = {'day': 13,
             'month': 12,
             'year': 2022}
ost_day = {0: 'Вторник',
           1:'Среду',
           2:'Четверг',
           3:'Пятницу',
           4:'Субботу',
           5:'Воскресенье',
           6:'Понедельник',
           }
class calendar:

    def __init__(self, new_go):
        self.new_year = 1
        self.diff = 0
        self.day_year = 365
        self.new_god = new_go
        self.till_ny = 0

    def next_new_year(self):
        self.till_ny = self.day_year - 31 + today['day'] + self.new_year
        print(f"Новый год в {today['year']} год наступит в {ost_day[self.till_ny % 7]}")

# 2. Есть ли годы, начинающиеся с пн? со вт?
# Привести ближайший пример.
    def chek_new_year(self):
        self.till_ny = self.day_year - 31 + today['day'] + self.new_year
        if today['year'] < self.new_god:
            self.till_ny += self.new_god - today['year']
            self.diff += self.new_god - today['year']
        else:
            self.till_ny += self.new_god - today['year']
            self.diff = self.new_god - today['year']
        if (self.new_god % 4 == 0 and self.new_god % 100 != 0) or (self.new_god % 400 == 0):
            self.new_diff = (self.diff + 2) // 4
            self.till_ny += self.new_diff
            print(f"Новый год в {self.new_god} год наступит в {ost_day[self.till_ny % 7]}")
        else:
            print(f"Новый год в {self.new_god} год наступит в {ost_day[self.till_ny % 7]}")

# run = calendar(ost_day)
# run.next_new_year()
run_2 = calendar(2021)
run_2.chek_new_year()



#
# 2. Есть ли годы, начинающиеся с пн? со вт?
# Привести ближайший пример.
# new_god = 2048


#
# 3. В какой день недели Вы родились? Перечислить все свои ДР,
# пришедшиеся на тот же день недели.