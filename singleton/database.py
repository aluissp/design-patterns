class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def query(self, sql):
        print(f'Executing: {sql}')


if __name__ == "__main__":
    # The client code.

    s1 = Database()
    s2 = Database()

    s1.query('select * form users where name=^A')

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
