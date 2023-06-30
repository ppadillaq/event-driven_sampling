import pandas as pd

class SensorNodeIntegral():
    """
    Sensor node for event-driven sampling under integral criterion.
    Inspired by Miskowicz, M (2005) The Event-Triggered Integral Criterion for Sensor
    Sampling
    """
    def __init__(self, axis, signal, mu, T, Tmax):
        self.sensor_plot = axis
        self.signal = signal
        self.x_sent = 0
        self.mu = mu
        self.T = T
        self.Tmax = Tmax
        self.k = []
        self.x = []


    def plot_sample(self):
        # data = {'k': self.k,
        #  'value': self.x
        #  }  
        data = {'value': self.x
         }  
        df = pd.DataFrame(data)
        df.plot(kind='line', legend=True, ax=self.sensor_plot, color='r', marker='o', fontsize=10)


    
    def sample(self, n_samples):
        T_sent = 0
        for k in range(n_samples):
            self.k.append(k)
            self.x.append(self.signal.get_sample(self.T*k))
            self.plot_sample()
            T_sent += self.T
            # To do: calculate integral
            # if abs(self.x[k] - self.x_sent) >= self.mu:
            #     self.broadcast(self.x[k])
            #     self.x_sent = self.x[k]
            #     self.reset()
            # else:
            #     if T_sent == self.Tmax:
            #         self.broadcast(self.x[k])
            #         self.reset()



    def reset(self):
        self.T_sent = 0




    def broadcast(self):
        print("transmit")