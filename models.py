from enum import Enum
from datetime import datetime
import pandas as pd


class DeliveryStatusEnum(Enum):
    UNLOADING   = 1  # разгрузка
    SORTING     = 2  # сортировка
    STORAGE     = 3  # хранение
    PRELOADING  = 4  # подготовка к отправке
    LOADING     = 5  # загрузка


class Delivery:
    uid: int 
    arrival: datetime
    departure: datetime
    volume: int
    status: DeliveryStatusEnum

    def __init__(self, uid, arrival, departure, volume, status=DeliveryStatusEnum.UNLOADING) -> None:
        self.uid = uid
        self.arrival = arrival
        self.departure = departure
        self.volume = volume
        self.status = status

    @property
    def processing_time(self) -> int:
        return (self.departure - self.arrival).days

    def __str__(self) -> str:
        return str(self.uid)

class BrigadeStatusEnum(Enum):
    INWORK = 1   # в работе
    SIMPLE = 2   # простой
    FREE   = 3   # свободны


class Brigade:
    uid: int
    performance: int
    cost: int
    status: BrigadeStatusEnum

    def __init__(self, uid, cost, performance, status=BrigadeStatusEnum.FREE) -> None:
        self.uid = uid
        self.cost = cost
        self.performance = performance
        self.status = status

    def __str__(self) -> str:
        return str(self.uid)


def load_delivery_data(data:pd.DataFrame) -> list[Delivery]:
    result = []
    for index, row in data.iterrows():
        result.append(Delivery(row['ID'], row['date of import'], 
                                row['departure date'], row['cargo volume']))
    return result


def load_brigade_data(data) -> list[Brigade]:
    result = []
    for index, row in data.iterrows():
        result.append(Brigade(row['uid'], row['cost'], row['performance']))
    return result