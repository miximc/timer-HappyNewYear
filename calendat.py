mounth = {'dec':31,
          'nov':30,
          'oct':31}
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
        self.till_ny = self.day_year - mounth['dec'] + today['day'] + self.new_year
        print(f"Новый год в {today['year']} год наступит в {ost_day[self.till_ny % 7]}")

# 2. Есть ли годы, начинающиеся с пн? со вт?
# Привести ближайший пример.
    def chek_new_year(self):
        self.till_ny = self.day_year - mounth['dec'] + today['day'] + self.new_year

        if today['year'] < self.new_god:
            if self.new_god - today['year'] > (self.diff + 2) // 4:
                self.diff = self.new_god - today['year']
                self.new_diff = (self.diff + 2) // 4
                self.till_ny += self.new_diff
                self.diff += self.new_god - today['year']
            self.till_ny += self.new_god - today['year']
            self.diff += self.new_god - today['year']
        else:
            if today['year'] - self.new_god > (self.diff + 2) // 4:
                self.diff = self.new_god - today['year']
                self.new_diff = (self.diff + 2) // 4
                self.till_ny += self.new_diff
                self.diff += self.new_god - today['year']
            self.till_ny += self.new_god - today['year']
            self.diff = self.new_god - today['year']

        if (self.new_god % 4 == 0 and self.new_god % 100 != 0) or (self.new_god % 400 == 0):
            self.diff = 0
            self.new_diff = (self.diff + 2) // 4
            self.till_ny += self.new_diff
            print(f"Новый год в {self.new_god} год наступит в {ost_day[self.till_ny % 7]}")
        else:
            print(f"Новый год в {self.new_god} год наступит в {ost_day[self.till_ny % 7]}")


run = calendar(ost_day)
run.next_new_year()
run_2 = calendar(1995)
run_2.chek_new_year()