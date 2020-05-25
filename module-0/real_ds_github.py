# -*- coding: utf-8 -*-

import numpy as np


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_v3(number):
    """Ищем медиану диапозона. Если загаданное число больше, медиана ограничивает диапозон снизу.
       Если число меньше, медиана ограничивает диапозон сверху"""
    count = 0
    begin = 1
    end = 100
    while True:
        predict = int(round(np.median([x for x in range(begin, end + 1)])))
        count += 1
        if number < predict:
            end = predict - 1
        elif number > predict:
            begin = predict + 1
        else:
            break
    return count

score_game(game_core_v3)