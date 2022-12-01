import pandas as pd
import matplotlib.pyplot as plt

class Python_data():

    #for calculate the years of experience
    exp_years = 0
    #counter to get the average of the years
    counter = 0
    #list of unique tecnologies
    unique_tecnologies = []
    #number of times in which the unique technologies appear
    statistics = []

    def __init__(self) -> None:
        #open file adn save the data temporaly in tec

        with open("data.txt","r") as file:
            tec = []
            for line in file:
                self.tec = line.split(",")


    @staticmethod
    def upper_tecnologies(tec) -> list:
        
        for index, element in enumerate(tec):
            tec[index] = element.upper().strip(" ")
        return tec

    def build_data(self):
        #get years of experience needed, get unique_tecnologies and get numeric statistics of this tecnologies
        
        self.tec = Python_data.upper_tecnologies(self.tec)

        for index, element in enumerate(self.tec):
            

            if element.isnumeric():

                
                self.exp_years += int(self.tec.pop(index))
                self.counter += 1
                
            
            else:

                if element not in self.unique_tecnologies:

                    self.unique_tecnologies.append(element)



            if element in self.unique_tecnologies:
                
                
                self.statistics.append(self.tec.count(element))

    def __str__(self) -> str:

        full_data = dict(zip(self.unique_tecnologies,self.statistics))
        
        for key, value in full_data.items():
            print(f"{key = } - {value = }")

        return ""

    #como ocultar un metodo desde fuera
    @staticmethod
    def show(unique_tecnologies: list, statistics: list):

        #df = pd.DataFrame(statistics, index=unique_tecnologies)
        plt.barh(statistics, unique_tecnologies)
        plt.show()

    def show_data(self):

        Python_data.show(self.unique_tecnologies, self.statistics)

    def show_data_relevant(self,value):

        unique_tecnologies_relevant = []
        statistics_relevant = []

        for index, element in enumerate(self.unique_tecnologies):
            if self.statistics[index] > value:
                statistics_relevant.append(self.statistics[index])
                unique_tecnologies_relevant.append(element)

        Python_data.show(unique_tecnologies_relevant, statistics_relevant)
        
#print(statistics)
#print(len(unique_tecnologies))
#print(len(statistics))

#df = pd.DataFrame(statistics, index=unique_tecnologies)

info = Python_data()

info.build_data()
print(info)
info.show_data_relevant(10)

