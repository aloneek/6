class Lamp:
    def __init__(self,power,energy_consumption,warranty):
        self.power = power # мощность излучения в Вт
        self.energy_consumption = energy_consumption # потребление энергии
        self.warranty = warranty # срок службы
    def analyse(self):
        return self.warranty/8
    def ratio(self):
        return self.power/self.energy_consumption
    

class Daylightlamp(Lamp):
    def __init__(self, color_temperarure, bulb_technology,is_active):
        self.color_temperature = color_temperarure # xxxxK in kelvins 
        self.bulb_technology = bulb_technology # LED/FLUORESCENT/HALOGEN etc
        self.is_active = is_active

    def turnOn(self):
        self.is_active = True
    def turnOff(self):
        self.is_active = False
    
    

class Searchlight(Lamp):
    def __init__(self, application_type, bulb_technology, IP):
        self.application_type = application_type # place where it will be used (outdoor/scene/)
        self.bulb_technology = bulb_technology # LED/XENON/LASER/HALOGEN/FLUORESCENT etc
        self.IP = IP # Ingress Protection
        
    def aceessment(self):
        if self.application_type == 'outdoor': 
            if int(self.IP) in range(65,69+1): print('good choise')
            else: print('bad choise, pick another for this place, it must be more resistant')
        elif self.application_type == 'scene':
            if self.bulb_technology in ['LED','XENON','LASER']: 
                print('good choise')
            else: print('bad choise, pick another for this place, choose another bulb technology')
        else: print('no info, sorry')

lamp1 = Searchlight('outdoor','LED',68)
lamp1.aceessment
print(lamp1.IP)

my_lamp = Daylightlamp(5000,'LED',False)
my_lamp.turnOn()
print(my_lamp.is_active)
my_lamp.warranty = 50000
print(my_lamp.warranty, my_lamp.analyse())