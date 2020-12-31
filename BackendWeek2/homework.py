import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = float(amount)
        self.comment = comment
        if date != None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.datetime.now().date()

class Calculator:
    def __init__(self, limit):
        self.limit = float(limit)
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_amount = 0
        current_day = dt.datetime.now().date()
        for record in self.records:
            if current_day == record.date:
                today_amount += record.amount
        return today_amount

    def get_week_stats(self):
        week_amount = 0
        period = dt.timedelta(days=7)
        current_day = dt.datetime.now().date()
        for record in self.records:
            if current_day - record.date <= period:
                week_amount += record.amount
        return week_amount


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0

    def get_today_cash_remained(self, currency):
        ost = self.limit - self.get_today_stats()
        if currency == 'rub':
            if ost > 0:
                return 'На сегодня осталось ' + str(round(ost, 2)) + ' руб'
            if ost == 0:
                return 'Денег нет, держись'
            if ost < 0:
                return 'Денег нет, держись: твой долг - ' + str(round(-ost, 2)) + ' руб'
        if currency == 'usd':
            if ost > 0:
                return 'На сегодня осталось ' + str(round(ost / self.USD_RATE, 2)) + ' USD'
            if ost == 0:
                return 'Денег нет, держись'
            if ost < 0:
                return 'Денег нет, держись: твой долг - ' + str(round(-ost / self.USD_RATE, 2)) + ' USD'
        if currency == 'eur':
            if ost > 0:
                return 'На сегодня осталось ' + str(round(ost / self.EURO_RATE, 2)) + ' Euro'
            if ost == 0:
                return 'Денег нет, держись'
            if ost < 0:
                return 'Денег нет, держись: твой долг - ' + str(round(-ost / self.EURO_RATE, 2)) + ' Euro'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.limit - self.get_today_stats() > 0:
            return 'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более ' + str(int(self.limit - self.get_today_stats())) + ' кКал'
        if self.limit - self.get_today_stats() <= 0:
            return 'Хватит есть!'

# для CashCalculator
r1 = Record(amount=1145, comment="Безудержный шопинг", date="31.12.2020")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины")
r3 = Record(amount=4691, comment="Катание на такси")


Cash = CashCalculator(limit=3000)
Cash.add_record(r1)
Cash.add_record(r2)
Cash.add_record(r3)

for record in Cash.records:
    print(f'amount={record.amount}, comment="{record.comment}", date="{record.date}"')

print(Cash.get_today_stats())
print(Cash.get_week_stats())
print(Cash.get_today_cash_remained('rub'))

# для CaloriesCalculator
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.")
r5 = Record(amount=84, comment="Йогурт.")
r6 = Record(amount=1140, comment="Баночка чипсов.")

Cashc = CaloriesCalculator(limit=3000)
Cashc.add_record(r4)
Cashc.add_record(r5)
Cashc.add_record(r6)

for record in Cashc.records:
    print(f'amount={record.amount}, comment="{record.comment}", date="{record.date}"')

print(Cashc.get_today_stats())
print(Cashc.get_week_stats())
print(Cashc.get_calories_remained())