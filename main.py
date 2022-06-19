import pandas as pd
from ga import ga
import models
from models import Delivery, Brigade
from algoritms import TaskAssignment


delivery_data = models.load_delivery_data(pd.read_excel('supply_information.xlsx'))
brigade_data = models.load_brigade_data(pd.read_excel('brigade.xlsx'))

solution = ga(brigade_data, delivery_data, 120, maxage=3, maxiter=25).fitness()

print()
print(solution)