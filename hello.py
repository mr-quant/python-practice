"""Учебный проект: первый скрипт.

Запуск из папки проекта:
    uv run hello.py
или после активации окружения:
    python hello.py
"""


def greet(name: str) -> str:
    """Возвращает приветствие для имени name."""
    return f"Привет, {name}!"


def ask_name() -> str:
    """Спрашивает имя у пользователя.

    input() вернул бы ошибку (EOFError), если запускать скрипт без консоли,
    например в тесте или когда ввод приходит по конвейеру, поэтому ошибку перехватываем.
    """
    try:
        answer = input("Как тебя зовут? ")
    except EOFError:
        return "Гость"
    # \ufeff — невидимый символ BOM: PowerShell иногда добавляет его к вводу,
    # а strip() его не считает пробелом, поэтому убираем вручную.
    return answer.replace("\ufeff", "").strip() or "Гость"


def sum_from_one_to(n: int) -> int:
    """Сумма чисел от 1 до n включительно.

    range(1, n + 1) — это 1, 2, ... , n (правая граница не входит),
    а sum(...) складывает всё, что внутри.
    Тот же результат через цикл:
        total = 0
        for number in range(1, n + 1):
            total += number
    """
    return sum(range(1, n + 1))


def main() -> None:
    names = ("Сергей", "Python", "Аня")
    for name in names:
        print(greet(name))

    print(greet(ask_name()))

    total = sum_from_one_to(100)
    print(f"Сумма чисел от 1 до 100 = {total}")


if __name__ == "__main__":
    main()