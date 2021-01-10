from collections import deque
from enum import Enum
from itertools import combinations

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from mesa import Model, Agent



#cnt = Counter()
#for agents in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
 #   cnt[agents] += 1


class Car():
    vehicle_type = "BMW"
    price = 40000
    def __init__(self,name, colour="red"):
        self.name = name
        self.colour = colour
        self.engine = 'off'
        self.engine_heat = "cold"

    def turn_on(self):
        self.engine = 'on'
        self.engine_heat = "hot"

    def turn_off(self):
        self.engine = "off"
        self.engine_heat = "warm"

    def __repr__(self):
        return self.name + " " + self.colour
    


c1 = Car('BMW')
c2 = Car('Nissan')
print(c1,c2)


