from enum import Enum
from datetime import datetime
import pandas as pd


class DeliveryStatusEnum(Enum):
    UNLOADING   = 1  # разгрузка
    # STORAGE     = 2  # хранение
    LOADING     = 2  # загрузка
    SENDED      = 3


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
    hours: int

    def __init__(self, uid, cost, performance, hours=12, status=BrigadeStatusEnum.FREE) -> None:
        self.uid = uid
        self.cost = cost
        self.performance = performance
        self.status = status
        self.hours = hours

    def __str__(self) -> str:
        return str(self.uid)


class Point:
    date: datetime
    cost: float
    deliverys: Delivery
    brigades: Brigade
    
    def __init__(self, date, cost, brigades, deliverys, solution) -> None:
        self.date = date
        self.cost = cost
        # self.__solution = solution 
        # self.__brigades = brigades
        # self.__deliverys = deliverys

        self.solution = {deliverys[delivery].uid:brigade  for delivery, brigade in enumerate(solution) }
    
    def __str__(self) -> str:
        return str(self.date)


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