import numpy as np



class RandomWalk():
    def __init__(self, maxSteps = 100, fromCoinToss = False):
        self.maxSteps = maxSteps
        self.possibleSteps = [-1, 1]
        

        if fromCoinToss == True:
            self.CT= CoinToss(self.maxSteps)
            self.steps = C.PlusMinusHT()

        else:
            self.CT= None
            self.steps = []
            for i in range(maxSteps):
                self.steps.append(np.random.choice(self.possibleSteps))

        self.States = []
        Sum = 0
        for i in range(maxSteps):
            Sum += self.steps[i]
            self.States.append(Sum)

    def movingAvgState(self):
        self.movingAvg = []
        temp = 0
        for i in range(self.maxSteps):
            temp+=self.States[i]/(i+1)
            self.movingAvg.append(temp)
        return self.movingAvg
        

    def simulate(self):
        from matplotlib.animation import FuncAnimation
        import matplotlib.pyplot as plt

        again = True
        while again == True:
        
            showAvg = str(input('Show Moving Average? [Y/N]: ')).lower()
            nPlotted = 0
            
            plt.style.use('dark_background')

            xdata = []
            ydata = []
            avg = []
            

            fig, ax = plt.subplots(figsize=(12,10))
            l, =ax.plot([],[], color='salmon', lw = 0.5, label = 'State')
            ax.plot([0*i + np.mean(self.States) for i in range(self.maxSteps)], linestyle='-', lw = 0.3, color = 'white',
                    label = 'Mean')

            avgs = self.movingAvgState()
            l1, = ax.plot([],[],color = 'yellow', lw = 0.5,  linestyle = '--', label = 'Moving Average')
            
            time_txt = ax.text(0.05, 0.95,'',
                            horizontalalignment='left',
                            verticalalignment='top',
                            transform=ax.transAxes)
            
            avgvalue = ax.text(0.05, 0.90,'',
                            horizontalalignment='left',
                            verticalalignment='top',
                            transform=ax.transAxes)
            
            value = ax.text(0.05, 0.85,'',
                            horizontalalignment='left',
                            verticalalignment='top',
                            transform=ax.transAxes)
            
            
            
            def init():
                ax.set_ylim(min(np.min(avgs),np.min(self.States)-1), max(np.max(avgs),np.max(self.States)+1))
                ax.title.set_text('Random Walk Simulation')
                l.set_data([],[])
                if showAvg == 'y':
                    l1.set_data([],[])
                time_txt.set_text("time-step: 0")
                value.set_text("Current State: %d" %self.States[0])
                avgvalue.set_text("Current Average: %.2f" %avgs[0])
                return l, time_txt, value, avgvalue, l1, 
        
            def animate(i):
                xdata.append(i)
                ydata.append(self.States[i])
                ax.set_xlim(0,i+1)
                if showAvg == 'y':
                    avg.append(avgs[i])
                    l1.set_data(xdata,avg)
                l.set_data(xdata, ydata)
                time_txt.set_text("Current Time-Step: %d"%i)
                avgvalue.set_text("Current Average: %.2f" %avgs[i])
                value.set_text("Current State: %d" %self.States[i])
                return l, time_txt,value, avgvalue, l1, 

            anim = FuncAnimation(fig, animate,
                                       init_func=init,
                               frames=self.maxSteps, interval=1, blit=True, repeat = False)
            
            plt.xlabel('Time-step (n)')
            plt.ylabel('State S')
            plt.legend()
            plt.show()
            print("\n\n")
            response = str(input("Plot a new Random Walk? [Y/N]:  ")).lower()
            
            print("\n\n")
            if response == 'n':
                again = False
                return
            else:
                newN = int(input("Enter the max number of steps to take: "))
                self.maxSteps = newN
                self.States = []
                Sum = 0
                for i in range(newN):
                    self.steps.append(np.random.choice(self.possibleSteps))
                    Sum += self.steps[i]
                    self.States.append(Sum)
                
            
            
            
