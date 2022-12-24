from abc import abstractmethod, ABC


class Father(ABC):

    @property
    @abstractmethod
    def name(self) -> None:
        pass


class Child(Father):
    name = 'Luis'
    apellido = 'Perugachi'

    def __init__(self) -> None:
        self.my_own_variable = 'Hii!'
        self.__another_variable = 'another!'

    @property
    def name(self) -> str:
        name = 'Maite'
        return name


child = Child()
print(Child.name, Child.apellido, child.apellido, child.name, '\n')
print(child.my_own_variable, child._Child__another_variable)
print(Child.__dict__)
print(child.__dict__)
