class Timing :

    def __init__(self,hrs,min,sec):
        self.__hrs=hrs
        self.__min=min
        self.__sec=sec
    def add_time(self,t1,t2):
        self.__hrs = t1.__hrs + t2.__hrs
        self.__min = t1.__min + t2.__min
        self.__sec = t1.__sec + t2.__sec
        if self.__min> 60:
            self.__hrs+=1
            self.__min -= 60
        while self.__sec>60:
            self.__min+=1
            self.__sec-=60
        #print(f"Time in Hours : {self.__hrs}hr \nTime in Minutes : {self.__min}min \nTime in Second : {self.__sec}sec")

t1 = Timing(1,31,30)
t2 = Timing(2,30,30)
t3 = Timing(0,0,0)
t3.add_time(t1,t2)
print(f"Time in Hours : {t3._Timing__hrs}hr \nTime in Minutes : {t3._Timing__min}min \nTime in Second : {t3._Timing__sec}sec")
        
        