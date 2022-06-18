import pandas as pd
import numpy as np


STAGE_AMOUNT = 5

excel_data = pd.read_excel('supply_information.xlsx')

data_sum_cargo = pd.DataFrame(excel_data, columns=['quantity of cargo'])
sum_cargo = list(data_sum_cargo.iloc[0])

print('количество грузов ',sum_cargo[0])
print('*******')

id_cargo= list(excel_data['ID'] )
print('ID грузов', id_cargo) 

import_date = list(excel_data['date of import'])
print('время привоза', import_date)

departure_date = list(excel_data['departure date'])
print('время отгрузки', departure_date) 

cargo_volume = list(excel_data['cargo volume'])
print('объём груза',cargo_volume)

#COL_VOLUME = 'cargo volume'
#excel_data.loc[i, COL_VOLUME]

def div_date(import_date, departure_date):
    import_date = np.array(import_date)
    departure_date = np.array(departure_date)
    return (departure_date - import_date)//STAGE_AMOUNT


print(div_date(import_date, departure_date))
