import pandas as pd
from ga import ga
import models
from models import Delivery, Brigade
from algoritms import ScheduleBuilder


delivery_data = models.load_delivery_data(pd.read_excel('supply_information.xlsx'))
brigade_data = models.load_brigade_data(pd.read_excel('brigade.xlsx'))



solution = ScheduleBuilder(brigade_data, delivery_data).solve()

print()
print("Дата события |  Стоимость  | Распределение {Погрузка:Бригада}")
[print(f"{str(point.date)[:-9]:^12} | {point.cost:^11} | {point.solution}") for point in solution]
print()
