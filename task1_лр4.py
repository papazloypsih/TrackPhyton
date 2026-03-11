if __name__ == "__main__":
    class Vehicle:
        """Базовый класс для транспортных средств."""

        def __init__(self, make: str, model: str, year: int, mileage: float) -> None:
            """
            Инициализация транспортного средства.

            :param make: Производитель (марка)
            :param model: Модель
            :param year: Год выпуска
            :param mileage: Пробег в километрах (инкапсулирован, т.к. изменяется только через методы)
            """
            if not isinstance(make, str):
                raise TypeError("Марка должна быть строкой")
            if not isinstance(model, str):
                raise TypeError("Модель должна быть строкой")
            if not isinstance(year, int):
                raise TypeError("Год должен быть целым числом")
            if year < 1886 or year > 2026:
                raise ValueError("Некорректный год выпуска")
            if not isinstance(mileage, (int, float)):
                raise TypeError("Пробег должен быть числом")
            if mileage < 0:
                raise ValueError("Пробег не может быть отрицательным")

            self.make = make
            self.model = model
            self.year = year
            self._mileage = mileage

        def get_mileage(self) -> float:
            """Вернуть текущий пробег."""
            return self._mileage

        def drive(self, distance: float) -> None:
            """
            Увеличить пробег на указанное расстояние.

            :param distance: Пройденное расстояние (км). Должно быть положительным.
            """
            if not isinstance(distance, (int, float)):
                raise TypeError("Расстояние должно быть числом")
            if distance <= 0:
                raise ValueError("Расстояние должно быть положительным")
            self._mileage += distance

        def __str__(self) -> str:
            """Пользовательское строковое представление."""
            return f"{self.make} {self.model} ({self.year}) — пробег {self._mileage:.1f} км"

        def __repr__(self) -> str:
            """Техническое представление для разработчиков."""
            return (f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, "
                    f"year={self.year!r}, mileage={self._mileage!r})")


    class Car(Vehicle):
        """Дочерний класс для легкового автомобиля."""

        def __init__(self, make: str, model: str, year: int, mileage: float,
                     num_doors: int, fuel_type: str) -> None:
            """
            Инициализация легкового автомобиля.

            :param make: Марка
            :param model: Модель
            :param year: Год выпуска
            :param mileage: Пробег
            :param num_doors: Количество дверей (2, 3, 4 или 5)
            :param fuel_type: Тип топлива
            """
            super().__init__(make, model, year, mileage)
            if not isinstance(num_doors, int):
                raise TypeError("Количество дверей должно быть целым числом")
            if num_doors not in (2, 3, 4, 5):
                raise ValueError("Количество дверей должно быть 2, 3, 4 или 5")
            if not isinstance(fuel_type, str):
                raise TypeError("Тип топлива должен быть строкой")
            self.num_doors = num_doors
            self.fuel_type = fuel_type
            self._features: list = []  # защищённый список дополнительных опций

        def add_feature(self, feature: str) -> None:
            """Добавить дополнительную опцию (например, 'кондиционер')."""
            if not isinstance(feature, str):
                raise TypeError("Опция должна быть строкой")
            self._features.append(feature)

        def get_mileage(self) -> float:
            """Унаследованный метод получения пробега."""
            return super().get_mileage()

        def drive(self, distance: float) -> None:
            """
            Перегруженный метод поездки.
            Причина перегрузки: для легковых автомобилей введено ограничение на максимальное расстояние за одну поездку
            (не более 1000 км) во избежание перегрева и чрезмерного износа.
            """
            if not isinstance(distance, (int, float)):
                raise TypeError("Расстояние должно быть числом")
            if distance <= 0:
                raise ValueError("Расстояние должно быть положительным")
            if distance > 1000:
                raise ValueError("Для легкового автомобиля одна поездка не может превышать 1000 км")
            self._mileage += distance

        def __str__(self) -> str:
            """Перегруженное строковое представление с информацией о легковом авто."""
            base = super().__str__()
            features_str = ', '.join(self._features) if self._features else 'нет'
            return (f"{base}, {self.num_doors}-дверный, топливо: {self.fuel_type}. "
                    f"Опции: {features_str}")

        @property
        def features(self) -> list:
            """Свойство для доступа к списку опций (только чтение)."""
            return self._features.copy()