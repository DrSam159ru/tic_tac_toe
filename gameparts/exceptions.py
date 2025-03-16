# gameparts/exceptions.py

class FieldIndexError(IndexError):
    """Выбрасывается, если выбрано значение вне поля."""

    def __init__(
        self,
        # Текст по умолчанию.
        message='Введено значение за границами игрового поля!'
    ):
        super().__init__(message)


class FieldIndexError(IndexError):
    """Выбрасывается, если ввели не цифры."""

    def __init__(
        self,
        # Текст по умолчанию.
        message='Буквы вводить нельзя. Только числа!'
    ):
        super().__init__(message)


# Вот оно - новое исключение, унаследованное от базового класса Exception.
class CellOccupiedError(Exception):
    def __init__(
        self,
        message='Попытка изменить занятую ячейку'
    ):

        super().__init__(message)
