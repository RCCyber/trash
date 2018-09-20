class Planet:

    def __init__(self, name):   #Инициализация экземпляра
        self.name = name        #Создаём атрибут экземпляра

    def __str__(self):          #Чтобы вернуть имя при print'е экземпляра класса
        return self.name


earth = Planet("Earth")       #Создали экземпляр класса
print(earth)
