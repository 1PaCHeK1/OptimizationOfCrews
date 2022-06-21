import math
from models import Brigade, Delivery, DeliveryStatusEnum, Point
from ga import ga
# solution = ga(brigade_data, delivery_data, 120, maxage=3, maxiter=25).fitness()
# print(DeliveryStatusEnum(DeliveryStatusEnum.LOADING.value+1))

class ScheduleBuilder:
    brigades: list[Brigade]
    deliverys: list[Delivery]
    
    def __init__(self, brigades, deliverys) -> None:
        self.brigades = brigades
        self.deliverys = deliverys

    def solve(self):
        solution = []
        while any(delivery.status != DeliveryStatusEnum.SENDED  for delivery in self.deliverys):
            ti = min([delivery for delivery in self.deliverys 
                        if delivery.status != DeliveryStatusEnum.SENDED], 
                    key=self.min_key)

            if ti.status == DeliveryStatusEnum.UNLOADING:   ti = ti.arrival
            elif ti.status == DeliveryStatusEnum.LOADING:   ti = ti.departure

            deliverys_i = [delivery 
                            for delivery in self.deliverys 
                            if (delivery.status == DeliveryStatusEnum.UNLOADING and delivery.arrival == ti) or \
                                (delivery.status == DeliveryStatusEnum.LOADING and delivery.departure == ti)
                        ]

            sol = ga(self.brigades, deliverys_i, 120, maxage=3, maxiter=25).fitness()

            for d in deliverys_i:
                d.status = DeliveryStatusEnum(d.status.value +1)

            solution.append(Point(ti, sol.func, self.brigades, deliverys_i, sol))
        return solution


    def min_key(self, value:Delivery):
        if value.status == DeliveryStatusEnum.UNLOADING:
            return value.arrival
        elif value.status == DeliveryStatusEnum.LOADING:
            return value.departure
        else:
            return math.inf