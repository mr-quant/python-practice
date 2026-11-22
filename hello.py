"""Учебный проект: первый скрипт.

Запуск из папки проекта:
    uv run hello.py
или после активации окружения:
    python hello.py
"""


def greet(name: str) -> str:
    """Возвращает приветствие для имени name."""
    return f"Привет, {name}!"


def main() -> None:
    for name in ("Сергей", "Python"):
        print(greet(name))

    # TODO 1: добавь ещё одно имя в кортеж выше.
    # TODO 2: попроси имя у пользователя через input() и поздоровайся с ним.
    # TODO 3: вычисли и выведи сумму чисел от 1 до 100 (подсказка: цикл for или sum(range(...))).


if __name__ == "__main__":
    main()