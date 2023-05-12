from data_access_layer.data_access import DataAccessLayer


class BusinessLogicLayer:
    def __init__(self):
        self.data_access = DataAccessLayer()

    def square_number(self, number):
        return self.data_access.get_square(number)