# python-practice

Учебная папка для практики Python. Python 3.13.5 установлен через `uv`.

## Быстрые команды

| Что нужно | Команда (в PowerShell, из папки проекта) |
| --- | --- |
| Запустить скрипт | `uv run hello.py` |
| Активировать окружение | `.\.venv\Scripts\Activate.ps1` |
| Запустить после активации | `python hello.py` |
| Выйти из окружения | `deactivate` |
| Поставить пакет | `uv add requests` (или `uv pip install requests`) |
| Список пакетов окружения | `uv pip list` |
| Создать новое окружение | `uv venv --seed` |

## Как это устроено

- `.venv\` — виртуальное окружение: отдельная «копия» Python со своими пакетами для этого проекта.
- `uv` — менеджер Python и пакетов: сам скачал Python 3.13.5 и создал `.venv`.
- `.vscode\settings.json` — подсказка VS Code, какой интерпретатор использовать.

## Идеи для тренировок

1. Консольный калькулятор (input + if/elif).
2. Угадай число (random, цикл while).
3. Камень-ножницы-бумага со счётом побед.
4. Заметки в файл (чтение/запись, `with open(...)`).
5. Парсер погоды с API (пакет `requests`).

## Git (репозиторий уже инициализирован)

Git 2.56.1 установлен отдельно: `C:\Users\Gamer\Tools\PortableGit`.

| Что нужно | Команда |
| --- | --- |
| Что изменилось | `git status` |
| Посмотреть изменения в тексте | `git diff` |
| Подготовить файл к коммиту | `git add hello.py` (или `git add -A`) |
| Сохранить снимок истории | `git commit -m "понятное описание"` |
| История | `git log --oneline --graph` |
| Откатить изменения файла | `git restore hello.py` |
| Создать ответвление | `git switch -c experiment` |
| Вернуться в main | `git switch main` |

Одноразово указать автора коммита, если конфигурация ещё не задана:

```powershell
git config --global user.name "Твоё имя"
git config --global user.email "ты@example.com"
```