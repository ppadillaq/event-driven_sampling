import pandas as pd

class SensorNodeIntegral():
    """
    Sensor node for event-driven sampling under integral criterion.
    Inspired by Miskowicz, M (2005) The Event-Triggered Integral Criterion for Sensor
    Sampling
    """
    def __init__(self, monitoring_node, axis, signal, mu, T, Tmax):
        self.monitoring_node = monitoring_node
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
        df.plot(kind='line', legend=True, ax=self.sensor_plot, color='r', marker='o', fontsize=1)


    
    def sample(self, n_samples):
        T_sent = 0
        for k in range(n_samples):
            self.k.append(k)
            self.x.append(self.signal.get_sample(self.T*k))
            T_sent += self.T
            # To do: calculate integral
            if abs(self.x[k] - self.x_sent) >= self.mu:
                self.broadcast(self.x[k])
                self.x_sent = self.x[k]
                T_sent = 0
                
            else:
                if T_sent == self.Tmax:
                    self.broadcast(self.x[k])
                    self.x_sent = self.x[k]
                    T_sent = 0
        self.plot_sample()
        self.reset()
        self.monitoring_node.plot_transmission()



    def reset(self):
        self.k = []
        self.x = []




    def broadcast(self,x):
        print("transmit")
        self.monitoring_node.send(x)



class Monitoring():
    def __init__(self, axis):
        self.x = []
        self.monitoring_plot = axis

    def send(self, x):
        self.x.append(x)

    def plot_transmission(self):
        data = {'value': self.x}  
        df = pd.DataFrame(data)
        df.plot(kind='line', legend=True, ax=self.monitoring_plot, color='r', marker='o', fontsize=1)
