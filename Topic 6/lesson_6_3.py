class Nikola:

    def __init__(self, name, age):
        if name != "Николай":
            self.name = f'Я не {name}, я Николай'
        else:
            self.name = name
        self.age = age


nikola = Nikola(name='Николай', age=25)
print(nikola.name)

maxim = Nikola(name='Максим', age=30)
print(maxim.name)
