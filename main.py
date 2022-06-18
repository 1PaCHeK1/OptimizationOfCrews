import pandas as pd
import models
from models import Delivery, Brigade
from algoritms import TaskAssignment


delivery_data = models.load_delivery_data(pd.read_excel('supply_information.xlsx'))
brigade_data = models.load_brigade_data(pd.read_excel('brigade.xlsx'))

solution = TaskAssignment(brigade_data, delivery_data)

print(solution.min_cost)
print(solution.best_solution)