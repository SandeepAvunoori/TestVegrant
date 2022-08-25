class planetary_data:
    def __init__(self):
        self.mercury= {"atmospheric_gasses":[], "moons" :0 , "rings" : False}
        self.venus = {"atmospheric_gasses":["carbondioxide", "nitrogen"], "moons": 0, "rings": False}
        self.earth = {"atmospheric_gasses":["nitrogen", "oxygen"], "moons": 1, "rings": False}
        self.jupitor = {"atmospheric_gasses":["hydrogen", "helium"], "moons": 79, "rings": True}
        self.saturn = {"atmospheric_gasses":["hydrogen", "helium"], "moons": 83, "rings": True}
        self.uranus = {"atmospheric_gasses":["hydrogen", "helium", "methane"], "moons": 27, "rings": True}
        self.planets= [self.mercury,self.venus,self.earth,self.jupitor,self.saturn ,self.uranus]
        
    def getMoonCount (self):
        moonscount = 0
        for planet in self.planets:
        
            if planet["rings"]:
                moonscount = moonscount + planet["moons"]
        print(moonscount)

planetary_obj = planetary_data()
planetary_obj.getMoonCount()
