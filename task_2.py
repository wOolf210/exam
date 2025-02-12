import random


def welcome_player():
    """Приветствие игрока и запрос имени."""
    try:
        name = input("Добро пожаловать в игру 'Камень, ножницы, бумага'! Как вас зовут? ")
        if not name.strip():
            raise ValueError("Имя не может быть пустым.")
        print(f"Привет, {name}!")
        return name
    except Exception as e:
        print(f"Ошибка: {e}")
        return welcome_player()


def get_computer_choice():
    """Получить случайный выбор компьютера."""
    try:
        choices = ['камень', 'ножницы', 'бумага']
        return random.choice(choices)
    except Exception as e:
        print(f"Ошибка при выборе компьютера: {e}")
        return get_computer_choice()


def get_player_choice():
    """Получить выбор игрока."""
    try:
        player_choice = input("Выберите: камень, ножницы или бумага: ").lower().strip()
        if player_choice not in ['камень', 'ножницы', 'бумага']:
            raise ValueError("Неверный выбор! Пожалуйста, выберите камень, ножницы или бумагу.")
        return player_choice
    except ValueError as e:
        print(f"Ошибка: {e}")
        return get_player_choice()
    except Exception as e:
        print(f"Ошибка: {e}")
        return get_player_choice()


def determine_winner(player_choice, computer_choice):
    """Определить победителя."""
    try:
        if player_choice == computer_choice:
            return "Ничья"
        elif (player_choice == 'камень' and computer_choice == 'ножницы') or \
                (player_choice == 'ножницы' and computer_choice == 'бумага') or \
                (player_choice == 'бумага' and computer_choice == 'камень'):
            return "Вы выиграли!"
        else:
            return "Компьютер выиграл!"
    except Exception as e:
        print(f"Ошибка при определении победителя: {e}")
        return "Ошибка в определении победителя."


def play_again():
    """Спросить, хочет ли игрок сыграть снова."""
    try:
        again = input("Хотите сыграть снова? (д/н): ").lower().strip()
        if again == 'д':
            return True
        elif again == 'н':
            return False
        else:
            raise ValueError("Неверный ввод. Пожалуйста, введите 'д' для продолжения или 'н' для выхода.")
    except ValueError as e:
        print(f"Ошибка: {e}")
        return play_again()
    except Exception as e:
        print(f"Ошибка: {e}")
        return play_again()


def main():
    """Основная функция игры."""
    try:
        welcome_player()
        while True:
            player_choice = get_player_choice()
            computer_choice = get_computer_choice()
            print(f"Компьютер выбрал: {computer_choice}")
            result = determine_winner(player_choice, computer_choice)
            print(result)

            if not play_again():
                print("Спасибо за игру! До свидания!")
                break
    except Exception as e:
        print(f"Ошибка в процессе игры: {e}")


if __name__ == "__main__":
    main()
