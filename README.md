# fitness_tracker

Программный модуль fitness_tracker - рассчитывает и отображает результаты тренировки. В модуле заложенны три вида тренирки: бег, спортивная ходьба и плавание.

Этот модуль выполняет следующие функции:
- принимает информацию о прошедшей тренировке,
- определяет вид тренировки,
- рассчитывает результаты тренировки,
- выводит информационное сообщение о результатах тренировки.

Информационное сообщение включает такие данные:
- тип тренировки (бег, ходьба или плавание);
- длительность тренировки;
- дистанция, которую преодолел пользователь, в километрах;
- среднюю скорость на дистанции, в км/ч;
- расход энергии, в килокалориях.

### Технологии
[![Python](https://img.shields.io/badge/-Python3.9-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)


### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Tatiana314/fitness_tracker.git && cd fitness_tracker 
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
Linux/macOS: source env/bin/activate
windows: source env/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Запуск модуля:
```
python homework.py
```

## Автор
[Мусатова Татьяна](https://github.com/Tatiana314)