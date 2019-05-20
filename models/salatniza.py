from models.dishes import Dishes

class Salatniza(Dishes):
    def __init__(self, price=0, capacity=0, manufacturerCountry="noCountry", MaterialType=materialType.MaterialType.METALS, numOfCucumbers=0):
        super(KitchenDishes, self).__init__(price, capacity, manufacturerCountry, MaterialType)
        self.numOfCucumbers = numOfCucumbers

    def __str__(self):
        return ('The price is {0}, capacity is {1}, it\'s from {2},'
                + 'material is {3}, ' + 'cucumbers = {4} \n').format(self.price,
                                                                     self.capacity,
                                                                     self.manufacturerCountry,
                                                                     self.materialType,
                                                                     self.numOfCucumbers,)

    def __repr__(self):
        return self.__str__()