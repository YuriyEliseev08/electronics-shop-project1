from src.item import Item


class Phone(Item):
    def __init__(self, name: str, prise: float, quantity: int, number_of_sim: int):
        super().__init__(name, prise, quantity)
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM- карт должно быть целым числом и больше 0.")

    @property
    def namber_of_sim(self):
        return self.__number_of_sim

    @namber_of_sim.setter
    def namber_of_sim(self, sim_input):
        if sim_input > 0:
            self.__number_of_sim = sim_input
        else:
            raise ValueError("Количество физических SIM- карт должно быть целым числом и больше 0.")

    def __add__(self, other) -> int:
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Только предметы класса Item или Phone")
