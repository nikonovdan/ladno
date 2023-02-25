'''''class Robot:

    model = 'robot'

    def __init__(self, walk):
        self.walk = walk

    def get_name(self):
        return self.model

class JumpRobot(Robot):

    task = 'jump'

    def __init__(self, jump):
        #super().__init__(model)
        self.jump = jump

    def get_name(self):
        return super().get_name() + ' ' + self.task

    borya = JumpRobot(10)
    print(borya.get_name()) '''''


class Line:
    def __int__(self, a = 0):
        self.__a = a

    def get_length(self):
        return self.__a

class Rectangle(Line):
    def __int__(self, a = 0, b = 0):
        super().__init__(a)
        self.__b = b

    def get_perimeter(self):
        return (super().get_length() + self.__b) * 2

    recOne = Rectangle(2, 2)
    print(recOne.get_petimeter())
