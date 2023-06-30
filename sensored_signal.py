import math

class SensoredSignal():

    def __init__(self, type):
        self.type = type
        self.test_signals = [
            "First-order system",
            "Second-order underdamped system",
            "Second-order undamped system"
        ]

    def get_sample(self, t):
        if self.type == self.test_signals[0]:
            return 1 - math.exp(-t)
        elif self.type == self.test_signals[1]:
            return 1 - (1 + t)*math.exp(t)
