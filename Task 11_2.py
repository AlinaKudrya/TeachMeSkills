class Car:
    def __init__(self, brand, year, speed):
        self.brand = brand
        self.year = year
        self.speed = speed

    def get_brand(self):
        return self.brand

    def set_brand(self,brand):
        self.brand = brand

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_diameter(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def add_speed(self):
        print('Speed increased by 5 km/h')
        self.speed += 5

    def reduce_speed(self):
        if self.speed != 0:
            print('The speed decreased by 5 km/h')
            self.speed -= 5

    def stop(self):
        print('The car stopped')
        self.speed = 0

    def speed_display(self):
        print(f'The current speed of the car: {self.speed} km\h')

    def turn(self): ### ??изменение знака скорости??
        if self.speed != 0:
            print('The car is turning. The speed is decreasing by 5 km/h')
            self.speed -= 5
            if self.speed == 0:
                print('The car stopped')
        else:
            print('You should speed up')