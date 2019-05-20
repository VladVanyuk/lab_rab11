from models import *
from models import cookingType
from models import materialType
from models import storageType
from models import workingType
from models.dishes import Dishes
from models.kitchenDishes import KitchenDishes
from models.dinnerware import Dinnerware
from models.dishesForStorage import DishesForStorage
from models.salatniza import Salatniza


class ShopManager:
    def __init__(self, dishesList):
        self.dishesList = dishesList

    def find_by_capacity(self, capacity):
        return list(filter(lambda dishes: dishes.capacity == capacity, self.dishesList))

    def find_by_material(self, materialType):
        return list(filter(lambda dishes: dishes.materialType == materialType, self.dishesList))

    def sort_by_price(self, reverse):
        return sorted(self.dishesList, key=lambda dishes: dishes.price, reverse=reverse)

    def sort_by_capacity(self, reverse):
        return sorted(self.dishesList, key=lambda dishes: dishes.width, reverse=reverse)


fryingPan = KitchenDishes(2.3, 10, "Poland", materialType.MaterialType.METAL, cookingType.CookingType.FORCOOKING, workingType.WorkingType.GAS)

plate = Dinnerware(44, 4, "Germany", materialType.MaterialType.CERAMIC, 25)

pitcher = DishesForStorage(23, 100, "Ukraine", materialType.MaterialType.WOOD, 30, storageType.StorageType.WATER)

salatnizaOne = Salatniza(44, 4, "Germany", materialType.MaterialType.CERAMIC, 675)


goods = [fryingPan, plate, pitcher]
manager = ShopManager(goods)
print(manager.sort_by_price(False))
print("\n")
print(manager.sort_by_capacity(True))
print("\n")
print(manager.search_by_type(materialType.MaterialType.CERAMIC))