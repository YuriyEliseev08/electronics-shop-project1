import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @classmethod
    def instantiate_from_csv(cls, file_name):
        with open(file_name, encoding='UTF-8', newline="") as file:
            file_info = csv.DictReader(file)
            print(file_info)
            for info in file_info:
                cls(info["name"], float(info["price"]), int(info['quantity']))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_input):
        if len(name_input) <= 10:
            self.__name = name_input
        else:
            #    raise Exception("Наименование товара превышает 10 символов")
            name_input_list = list(name_input)
            name_input_list_10 = name_input_list[0:9]
            self.__name = "".join(name_input_list_10)
