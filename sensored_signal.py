import math

class SensoredSignal():

    def __init__(self, type):
        self.T1 = 1
        self.T2 = 5/7
        self.wn = math.pi/10
        self.A = self.T1/(self.T2 - self.T1)
        self.B = self.T2/(self.T2 - self.T1)
        self.type = type
        self.test_signals = [
            "First-order system",
            "Second-order damped system",
            "Second-order underdamped system",
            "Second-order undamped system"
        ]

    def get_sample(self, t):
        if self.type == self.test_signals[0]:
            return 1 - math.exp(-t)
        elif self.type == self.test_signals[1]:
            return 1 - (1 + t)*math.exp(t)
        elif self.type == self.test_signals[2]:
            return 1 + self.A*math.exp(-t/self.T1) + self.B*math.exp(-t/self.T2)
        elif self.type == self.test_signals[3]:
            return 1 - math.cos(self.wn * t)
