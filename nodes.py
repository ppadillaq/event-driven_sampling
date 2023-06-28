class SensorNodeIntegral():
    """
    Sensor node for event-driven sampling under integral criterion.
    Inspired by Miskowicz, M (2005) The Event-Triggered Integral Criterion for Sensor
    Sampling
    """
    def __init__(self, mu, T, Tmax):
        self.x_sent = 0
        self.mu - mu
        self.T = T
        self.Tmax = Tmax

    
    def sample(self, x):
        self.T_sent += self.T
        # To do: calculate integral
        if abs(x - self.x_sent) >= self.mu:
            self.broadcast(x)
            self.x_sent = x
            self.reset()

        else:
            if self.T_sent == self.Tmax:
                self.broadcast(x)
                self.reset()



    def reset(self):
        self.T_sent = 0




    def broadcast(self):
        print("transmit")