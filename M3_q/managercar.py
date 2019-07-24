from car import Car
car1 = Car("KA20MA3307",5)
car2 = Car("KA20MA3308",4)
car3 = Car("KA20MA3309",5)
car4 = Car("KA20MA3303",6)
car5 = Car("KA20MA3302",4)
car1.start()
car2.start()
car3.start()
car1.change_gear()
car2.change_gear()
car1.change_gear()
lst = [car1,car2,car3,car4,car5]
for car in lst:
    car.showInfo()
c = len(list(filter(lambda x : x.is_started and x.c_gear==0,lst)))
print(c)