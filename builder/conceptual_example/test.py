from abc import abstractmethod, ABC


class Father(ABC):

    @property
    @abstractmethod
    def name(self) -> None:
        pass


class Child(Father):
    name = 'Luis'

    def __init__(self) -> None:
        self.my_own_variable = 'Hii!'

    @property
    def name(self) -> str:
        name = 'Maite'
        return name


child = Child()
print(Child.name, child.name, '\n')
print(Child.__dict__)
print(child.__dict__)
