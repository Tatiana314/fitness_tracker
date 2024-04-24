from __future__ import annotations

from dataclasses import asdict, dataclass, fields


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    MESSAGE = (
        'Тип тренировки: {training_type}; '
        'Длительность: {duration:.3f} ч.; '
        'Дистанция: {distance:.3f} км; '
        'Ср. скорость: {speed:.3f} км/ч; '
        'Потрачено ккал: {calories:.3f}.'
    )

    def get_message(self) -> str:
        return self.MESSAGE.format(**asdict(self))


@dataclass
class Training:
    """Базовый класс тренировки."""

    LEN_STEP = 0.65
    M_IN_KM = 1000
    HR_IN_MIN = 60
    action: int
    duration: float
    weight: float

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения в км/ч."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError(
            f'Определите get_spent_calories в {type(self).__name__}.'
        )

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories()
        )


@dataclass
class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return (
            (
                self.CALORIES_MEAN_SPEED_MULTIPLIER
                * self.get_mean_speed()
                + self.CALORIES_MEAN_SPEED_SHIFT
            )
            * self.weight / self.M_IN_KM
            * self.duration * self.HR_IN_MIN
        )


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    height: float
    COEFFICIENT_WEIGHT_SHIFT = 0.035
    COEFFICIENT_WEIGHT_MULTIPLIER = 0.029
    CM_IN_M = 100
    KM_H_IN_M_SEC = round(Training.M_IN_KM / Training.HR_IN_MIN ** 2, 3)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return (
            (
                self.COEFFICIENT_WEIGHT_SHIFT * self.weight
                + (self.get_mean_speed() * self.KM_H_IN_M_SEC)**2
                / (self.height / self.CM_IN_M)
                * self.COEFFICIENT_WEIGHT_MULTIPLIER * self.weight
            ) * self.duration * Training.HR_IN_MIN
        )


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38
    CALORIES_MEAN_SPEED_SHIFT = 1.1
    CALORIES_MEAN_SPEED_MULTIPLIER = 2
    length_pool: float
    count_pool: int

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения в км/ч."""
        return (
            self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        )

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return (
            (self.get_mean_speed() + self.CALORIES_MEAN_SPEED_SHIFT)
            * self.CALORIES_MEAN_SPEED_MULTIPLIER * self.weight * self.duration
        )


TYPES_TRAINING: dict[str, list(type[Training], int)] = {
    'SWM': (Swimming, 5),
    'RUN': (Running, 3),
    'WLK': (SportsWalking, 4)
}
DATA_ERROR = (
    'Ошибка передачи данных о тренировке. '
    'Передано {index} показателя. '
    'Для {training} необходимо передать {number} показателя.'
)
TRAINING_ERROR = (
    '{data} - несуществующий вид тренировки. '
    'Доступные виды тренировок: {workout}.'
)


def read_package(workout_type: str, data: list[float]) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type not in TYPES_TRAINING:
        raise ValueError(
            TRAINING_ERROR.format(
                data=workout_type,
                workout=list(TYPES_TRAINING.keys())
            )
        )
    if len(fields(TYPES_TRAINING[workout_type][0])) != len(data):
        raise ValueError(
            DATA_ERROR.format(
                index=len(data),
                training=workout_type,
                number=TYPES_TRAINING[workout_type][1]
            )
        )
    return TYPES_TRAINING[workout_type][0](*data)


def main(training: Training) -> None:
    """Главная функция."""
    print(training.show_training_info().get_message())


if __name__ == '__main__':
    packages: list[str, list[float]] = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        main(read_package(workout_type, data))
