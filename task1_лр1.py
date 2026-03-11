from typing import Union, Optional
import doctest
from datetime import datetime


class Book:
    """Класс, представляющий книгу в библиотеке"""

    def __init__(self, title: str, author: str, page_count: int, publication_year: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги (от 1 до 200 символов)
        :param author: Автор книги (от 2 до 100 символов)
        :param page_count: Количество страниц (от 1 до 5000)
        :param publication_year: Год публикации (от 1000 до текущего года)

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 384, 1966)
        >>> book.title
        'Мастер и Маргарита'
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if len(title) < 1 or len(title) > 200:
            raise ValueError("Название книги должно содержать от 1 до 200 символов")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if len(author) < 2 or len(author) > 100:
            raise ValueError("Имя автора должно содержать от 2 до 100 символов")
        self.author = author

        if not isinstance(page_count, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if page_count < 1 or page_count > 5000:
            raise ValueError("Количество страниц должно быть от 1 до 5000")
        self.page_count = page_count

        current_year = datetime.now().year
        if not isinstance(publication_year, int):
            raise TypeError("Год публикации должен быть целым числом")
        if publication_year < 1000 or publication_year > current_year:
            raise ValueError(f"Год публикации должен быть от 1000 до {current_year}")
        self.publication_year = publication_year

        self.is_borrowed = False  # По умолчанию книга в библиотеке
        self.borrower_name: Optional[str] = None

    def borrow_book(self, borrower: str) -> None:
        """
        Выдача книги читателю

        :param borrower: Имя читателя, который берет книгу
        :raise ValueError: Если книга уже выдана
        :raise TypeError: Если имя читателя не является строкой

        Примеры:
        >>> book = Book("Преступление и наказание", "Федор Достоевский", 608, 1866)
        >>> book.borrow_book("Иван Иванов")
        >>> book.is_borrowed
        True
        """
        if not isinstance(borrower, str):
            raise TypeError("Имя читателя должно быть строкой")
        if self.is_borrowed:
            raise ValueError("Книга уже выдана другому читателю")

        self.is_borrowed = True
        self.borrower_name = borrower

    def return_book(self) -> None:
        """
        Возврат книги в библиотеку

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225, 1869)
        >>> book.borrow_book("Петр Петров")
        >>> book.return_book()
        >>> book.is_borrowed
        False
        """
        self.is_borrowed = False
        self.borrower_name = None

    def get_age(self) -> int:
        """
        Расчет возраста книги в годах

        :return: Возраст книги в годах

        Примеры:
        >>> book = Book("Евгений Онегин", "Александр Пушкин", 224, 1833)
        >>> book.get_age() > 100  # Книге больше 100 лет
        True
        """
        current_year = datetime.now().year
        return current_year - self.publication_year


class Smartphone:
    """Класс, представляющий смартфон"""

    def __init__(self, brand: str, model: str, storage_gb: int, battery_capacity_mah: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона (например: Apple, Samsung, Xiaomi)
        :param model: Модель смартфона
        :param storage_gb: Объем памяти в ГБ (от 1 до 2048)
        :param battery_capacity_mah: Емкость аккумулятора в мАч (от 1000 до 20000)

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 256, 3279)
        >>> phone.brand
        'Apple'
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if len(brand) < 1 or len(brand) > 50:
            raise ValueError("Название бренда должно содержать от 1 до 50 символов")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if len(model) < 1 or len(model) > 50:
            raise ValueError("Название модели должно содержать от 1 до 50 символов")
        self.model = model

        if not isinstance(storage_gb, int):
            raise TypeError("Объем памяти должен быть целым числом")
        if storage_gb < 1 or storage_gb > 2048:
            raise ValueError("Объем памяти должен быть от 1 до 2048 ГБ")
        self.storage_gb = storage_gb

        if not isinstance(battery_capacity_mah, int):
            raise TypeError("Емкость аккумулятора должна быть целым числом")
        if battery_capacity_mah < 1000 or battery_capacity_mah > 20000:
            raise ValueError("Емкость аккумулятора должна быть от 1000 до 20000 мАч")
        self.battery_capacity_mah = battery_capacity_mah

        self.is_on = False
        self.battery_level = 100  # Процент заряда
        self.used_storage = 0  # Использованная память

    def turn_on(self) -> None:
        """
        Включение смартфона

        :raise ValueError: Если смартфон уже включен

        Примеры:
        >>> phone = Smartphone("Samsung", "Galaxy S23", 512, 3900)
        >>> phone.turn_on()
        >>> phone.is_on
        True
        """
        if self.is_on:
            raise ValueError("Смартфон уже включен")
        self.is_on = True

    def charge(self, minutes: int) -> int:
        """
        Зарядка смартфона

        :param minutes: Время зарядки в минутах (от 1 до 1440)
        :return: Новый уровень заряда в процентах
        :raise ValueError: Если время зарядки вне допустимого диапазона

        Примеры:
        >>> phone = Smartphone("Xiaomi", "Redmi Note 12", 128, 5000)
        >>> phone.battery_level = 20
        >>> phone.charge(30) > 20
        True
        """
        if not isinstance(minutes, int):
            raise TypeError("Время зарядки должно быть целым числом")
        if minutes < 1 or minutes > 1440:
            raise ValueError("Время зарядки должно быть от 1 до 1440 минут")

        # Упрощенная модель зарядки: 2% за каждую минуту
        charge_amount = min(minutes * 2, 100 - self.battery_level)
        self.battery_level += charge_amount
        return self.battery_level

    def install_app(self, app_name: str, app_size_gb: Union[int, float]) -> bool:
        """
        Установка приложения на смартфон

        :param app_name: Название приложения
        :param app_size_gb: Размер приложения в ГБ
        :return: True если установка успешна, False если недостаточно памяти
        :raise ValueError: Если размер приложения отрицательный или слишком большой

        Примеры:
        >>> phone = Smartphone("Google", "Pixel 7", 256, 4355)
        >>> phone.install_app("WhatsApp", 0.5)
        True
        """
        if not isinstance(app_name, str):
            raise TypeError("Название приложения должно быть строкой")
        if not isinstance(app_size_gb, (int, float)):
            raise TypeError("Размер приложения должен быть числом")
        if app_size_gb <= 0 or app_size_gb > 100:
            raise ValueError("Размер приложения должен быть от 0 до 100 ГБ")

        if self.used_storage + app_size_gb <= self.storage_gb:
            self.used_storage += app_size_gb
            return True
        return False


class BankAccount:
    """Класс, представляющий банковский счет"""

    def __init__(self, account_number: str, account_holder: str, initial_balance: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param account_number: Номер счета (20 цифр)
        :param account_holder: Владелец счета
        :param initial_balance: Начальный баланс (неотрицательный)

        Примеры:
        >>> account = BankAccount("12345678901234567890", "Иван Иванов", 1000.50)
        >>> account.account_holder
        'Иван Иванов'
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть строкой")
        if not account_number.isdigit() or len(account_number) != 20:
            raise ValueError("Номер счета должен состоять из 20 цифр")
        self.account_number = account_number

        if not isinstance(account_holder, str):
            raise TypeError("Имя владельца должно быть строкой")
        if len(account_holder) < 2 or len(account_holder) > 100:
            raise ValueError("Имя владельца должно содержать от 2 до 100 символов")
        self.account_holder = account_holder

        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Начальный баланс должен быть числом")
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.balance = float(initial_balance)

        self.transaction_history = []

    def deposit(self, amount: Union[int, float]) -> float:
        """
        Внесение средств на счет

        :param amount: Сумма для внесения (положительное число)
        :return: Новый баланс счета
        :raise ValueError: Если сумма внесения отрицательная или нулевая

        Примеры:
        >>> account = BankAccount("11112222333344445555", "Петр Петров", 500)
        >>> account.deposit(250.75)
        750.75
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма внесения должна быть положительной")

        self.balance += amount
        self.transaction_history.append(f"Пополнение: +{amount}")
        return self.balance

    def withdraw(self, amount: Union[int, float]) -> float:
        """
        Снятие средств со счета

        :param amount: Сумма для снятия (положительное число)
        :return: Новый баланс счета
        :raise ValueError: Если сумма снятия превышает баланс

        Примеры:
        >>> account = BankAccount("99998888777766665555", "Мария Сидорова", 1000)
        >>> account.withdraw(300)
        700.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")

        self.balance -= amount
        self.transaction_history.append(f"Снятие: -{amount}")
        return self.balance

    def transfer(self, target_account: 'BankAccount', amount: Union[int, float]) -> None:
        """
        Перевод средств на другой счет

        :param target_account: Счет-получатель
        :param amount: Сумма перевода
        :raise TypeError: Если получатель не является BankAccount
        :raise ValueError: Если сумма перевода превышает баланс

        Примеры:
        >>> account1 = BankAccount("11111111111111111111", "Анна", 2000)
        >>> account2 = BankAccount("22222222222222222222", "Борис", 500)
        >>> account1.transfer(account2, 750)
        >>> account1.balance
        1250.0
        >>> account2.balance
        1250.0
        """
        if not isinstance(target_account, BankAccount):
            raise TypeError("Получатель должен быть объектом BankAccount")
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")

        self.balance -= amount
        target_account.balance += amount
        self.transaction_history.append(f"Перевод на счет {target_account.account_number}: -{amount}")
        target_account.transaction_history.append(f"Перевод со счета {self.account_number}: +{amount}")


if __name__ == "__main__":
    # Запуск тестов из документации
    doctest.testmod(verbose=True)

    # Дополнительное тестирование создания объектов
    print("\n" + "=" * 50)
    print("Дополнительное тестирование:")
    print("=" * 50)

    try:
        # Создание и тестирование книги
        print("\n1. Тестирование класса Book:")
        book = Book("1984", "Джордж Оруэлл", 328, 1949)
        print(f"   Книга создана: '{book.title}' автора {book.author}")
        print(f"   Возраст книги: {book.get_age()} лет")

        # Создание и тестирование смартфона
        print("\n2. Тестирование класса Smartphone:")
        phone = Smartphone("Sony", "Xperia 1 V", 256, 5000)
        print(f"   Смартфон создан: {phone.brand} {phone.model}")
        phone.turn_on()
        print(f"   Смартфон включен: {phone.is_on}")
        print(f"   Установка приложения: {phone.install_app('Telegram', 0.3)}")

        # Создание и тестирование банковского счета
        print("\n3. Тестирование класса BankAccount:")
        account = BankAccount("12345678901234567890", "Алексей", 1500.75)
        print(f"   Счет создан: владелец {account.account_holder}, баланс {account.balance}")

        # Тестирование операций со счетом
        new_balance = account.deposit(500.25)
        print(f"   После пополнения: баланс {new_balance}")

        new_balance = account.withdraw(200)
        print(f"   После снятия: баланс {new_balance}")

        # Создание второго счета для перевода
        account2 = BankAccount("09876543210987654321", "Мария", 3000)
        account.transfer(account2, 800)
        print(f"   После перевода 800 рублей Марии:")
        print(f"   Баланс Алексея: {account.balance}")
        print(f"   Баланс Марии: {account2.balance}")

    except (ValueError, TypeError) as e:
        print(f"Ошибка: {e}")

    print("\nВсе тесты завершены!")
