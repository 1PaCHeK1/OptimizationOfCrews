import math
import random
from bisect import bisect
from typing import Iterable

from LocalSearchAlgorithms.ga.core import Gen, GA
from models import Brigade, Delivery

class ga(GA):
    brigades:   Brigade
    deliverys:  Delivery

    def __init__(self, brigades, deliverys, maxpopulation, maxage=None, share=-1, maxiter=10, n=None, options=None, callable=None):
        if n is None:       n = len(deliverys)
        if options is None: options = {}
        
        super().__init__(None, maxpopulation, maxage, share, maxiter, n, options, callable)
        
        self.brigades = brigades
        self.deliverys = deliverys

    def crossover(self, leftgen:Gen, rightgen:Gen) -> None:
        # new_gen1_code = leftgen[:len(leftgen)//3] + rightgen[len(leftgen)//3:2*len(leftgen)//3] + leftgen[2*len(leftgen)//3:]
        # new_gen2_code = rightgen[:len(leftgen)//3] + leftgen[len(leftgen)//3:2*len(leftgen)//3] + rightgen[2*len(leftgen)//3:]

        new_gen1_code = leftgen[:len(leftgen)//2] + rightgen[len(leftgen)//2:]
        new_gen2_code = rightgen[:len(leftgen)//2] + leftgen[len(leftgen)//2:]

        new_gen1 = Gen(new_gen1_code, self.func(new_gen1_code))
        new_gen2 = Gen(new_gen2_code, self.func(new_gen2_code))

        if len(self.population) < self.maxpopulation+1:
            tmp = [ i.func for i in self.population]
            index = bisect(tmp, new_gen1.func)
            self.population.insert(index, new_gen1)
        if len(self.population) < self.maxpopulation+1:
            tmp = [ i.func for i in self.population]
            index = bisect(tmp, new_gen2.func)
            self.population.insert(index, new_gen2)

    def mutation(self, gen:Gen) -> None:
        for _ in range(max(self.n//2-gen.age, 0)):
            index = random.randint(0, len(gen)-1)
            gen.chromosomes[index] = random.randint(0, len(self.brigades)-1)
            gen.func = self.func(gen)

    def func(self, solution:Iterable) -> float:
        result = {}
        for index, brigade in enumerate(solution):
            result.setdefault(brigade, []).append(index)
        
        # print(result)
        answer = 0
        for brigade, deliverys in result.items():
            brigade = self.brigades[brigade]
            duration = sum([self.deliverys[d].volume/brigade.performance for d in deliverys])
            if duration > brigade.hours:  return math.inf
            # print('duration', brigade.uid, duration, (1 + duration//brigade.hours))
            answer += brigade.cost #*(1 + duration//brigade.hours)
        # print('answer', answer)
        return answer


    def creategen(self) -> Gen:
        gen_code = [random.randint(0, len(self.brigades)-1) for i in range(self.n)]
        random.shuffle(gen_code)
        return Gen(gen_code, self.func(gen_code))


    def filter(self) -> None:
        # self.population.sort(key=lambda gen: gen.func)
        self.population = self.population[len(self.population)//3:]
        # print(self.population[-1])