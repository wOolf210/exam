import time

class Pizza:
    """Базовый класс для пицц."""
    def __init__(self, name, dough, sauce, topping, price):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.topping = topping
        self.price = price

    def prepare(self):
        """Подготовить пиццу: замесить тесто, собрать начинку."""
        try:
            print(f"Подготавливаем пиццу {self.name}: замешиваем {self.dough} тесто, добавляем соус {self.sauce} и начинку {self.topping}.")
            time.sleep(3)
        except Exception as e:
            print(f"Ошибка при подготовке пиццы {self.name}: {e}")

    def bake(self):
        """Испечь пиццу."""
        try:
            print(f"Пицца {self.name} готовится в духовке...")
            time.sleep(5)
        except Exception as e:
            print(f"Ошибка при выпекании пиццы {self.name}: {e}")

    def cut(self):
        """Порезать пиццу на кусочки."""
        try:
            print(f"Пицца {self.name} порезана на кусочки.")
            time.sleep(2)
        except Exception as e:
            print(f"Ошибка при нарезке пиццы {self.name}: {e}")

    def package(self):
        """Упаковать пиццу для доставки."""
        try:
            print(f"Пицца {self.name} упакована.")
            time.sleep(1)
        except Exception as e:
            print(f"Ошибка при упаковке пиццы {self.name}: {e}")


class PepperoniPizza(Pizza):
    """Пицца Пепперони."""
    def __init__(self):
        super().__init__("Пепперони", "тонкое", "томатный", "пепперони", 5000)


class BBQPizza(Pizza):
    """Пицца Барбекю."""
    def __init__(self):
        super().__init__("Барбекю", "толстое", "барбекю", "курица, бекон, лук", 6000)


class SeafoodPizza(Pizza):
    """Пицца с дарами моря."""
    def __init__(self):
        super().__init__("Дары Моря", "тонкое", "песто", "креветки, мидии, кальмары", 7000)


class Order:
    """Класс для хранения заказа."""
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        """Добавить пиццу в заказ."""
        try:
            self.pizzas.append(pizza)
            print(f"Пицца {pizza.name} добавлена в заказ.")
        except Exception as e:
            print(f"Ошибка при добавлении пиццы в заказ: {e}")

    def remove_pizza(self, pizza_name):
        """Удалить пиццу из заказа."""
        try:
            pizza_to_remove = None
            for pizza in self.pizzas:
                if pizza.name.lower() == pizza_name.lower():
                    pizza_to_remove = pizza
                    break
            if pizza_to_remove:
                self.pizzas.remove(pizza_to_remove)
                print(f"Пицца {pizza_name} удалена из заказа.")
            else:
                print(f"Пицца с названием {pizza_name} не найдена в заказе.")
        except Exception as e:
            print(f"Ошибка при удалении пиццы из заказа: {e}")

    def total_price(self):
        """Посчитать общую стоимость заказа."""
        try:
            total = sum(pizza.price for pizza in self.pizzas)
            print(f"Общая стоимость заказа: {total} тг.")
            return total
        except Exception as e:
            print(f"Ошибка при расчете стоимости заказа: {e}")
            return 0

    def show_order(self):
        """Показать список пицц в заказе."""
        if self.pizzas:
            print("Ваш заказ:")
            for pizza in self.pizzas:
                print(f"{pizza.name} - {pizza.price} тг.")
        else:
            print("Ваш заказ пуст.")


class Terminal:
    """Терминал для взаимодействия с пользователем."""
    def __init__(self):
        self.order = Order()
        self.menu = {
            1: PepperoniPizza(),
            2: BBQPizza(),
            3: SeafoodPizza(),
        }

    def show_menu(self):
        """Показать меню пицц."""
        print("Меню пицц:")
        try:
            for key, pizza in self.menu.items():
                print(f"{key}. {pizza.name} - {pizza.price} тг.")
        except Exception as e:
            print(f"Ошибка при отображении меню: {e}")

    def take_order(self):
        """Принять заказ от клиента."""
        try:
            while True:
                self.show_menu()
                choice = input("Выберите пиццу по номеру (или введите '0' для завершения): ")
                if choice == '0':
                    break
                try:
                    pizza_choice = int(choice)
                    if pizza_choice not in self.menu:
                        print("Неверный выбор, попробуйте снова.")
                        continue
                    pizza = self.menu[pizza_choice]
                    self.order.add_pizza(pizza)
                except ValueError:
                    print("Ошибка: введите номер пиццы.")
        except Exception as e:
            print(f"Ошибка при принятии заказа: {e}")

    def confirm_order(self):
        """Подтвердить заказ."""
        try:
            total = self.order.total_price()
            if total > 0:
                while True:
                    # Показать текущий список заказа
                    self.order.show_order()

                    # Предложить удалить пиццу
                    remove_choice = input("Хотите удалить пиццу из заказа? (д/н): ").lower()
                    if remove_choice == 'д':
                        pizza_name = input("Введите название пиццы, которую хотите удалить: ")
                        self.order.remove_pizza(pizza_name)
                    elif remove_choice == 'н':
                        break
                    else:
                        print("Неверный ввод, попробуйте снова.")

                # Подтверждение заказа
                while True:
                    confirmation = input("Подтвердить заказ (д/н): ").lower()
                    if confirmation == 'д':
                        print("Заказ подтвержден!")
                        self.process_payment()
                        break
                    elif confirmation == 'н':
                        print("Заказ отменен.")
                        break
                    else:
                        print("Неверный ввод. Пожалуйста, введите 'д' для подтверждения или 'н' для отмены.")
            else:
                print("Заказ пуст.")
        except Exception as e:
            print(f"Ошибка при подтверждении заказа: {e}")

    def process_payment(self):
        """Обработка оплаты заказа."""
        try:
            amount = self.order.total_price()
            if amount > 0:
                while True:
                    try:
                        payment = float(input(f"Оплатите {amount} тг.: "))
                        if payment == amount:
                            print("Оплата прошла успешно.")
                            self.prepare_order()
                            break
                        else:
                            print("Неверная сумма оплаты, попробуйте снова.")
                    except ValueError:
                        print("Ошибка: введите корректную сумму.")
            else:
                print("Ошибка: заказ пуст.")
        except Exception as e:
            print(f"Ошибка при оплате: {e}")

    def prepare_order(self):
        """Приготовить заказ."""
        try:
            print("Приступаем к приготовлению пицц...")
            for pizza in self.order.pizzas:
                pizza.prepare()
                pizza.bake()
                pizza.cut()
                pizza.package()
            print("Заказ готов!")
        except Exception as e:
            print(f"Ошибка при приготовлении заказа: {e}")


if __name__ == "__main__":
    try:
        terminal = Terminal()
        terminal.take_order()
        terminal.confirm_order()
    except Exception as e:
        print(f"Ошибка в процессе работы терминала: {e}")
