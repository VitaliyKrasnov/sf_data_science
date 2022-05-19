import numpy as np

def random_predict(number:int=1) -> int:
    """_summary_

    Args:
        number (int, optional): Число которое нужно угадать. Значение по умолчанию 1.

    Returns:
        int: Количество попыток за которое было угадано число
    """
    
    """ 
    УСЛОВИЯ ЗАДАНИЯ

    - Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать
    - Алгоритм учитывает информацию о том, больше или меньше случайное число нужного нам числа.
    """
    top_boundary = 100
    down_boundary = 1
    count = 0
    # выбираем начальную точку поиска загаданного числа
    predict_number = 50

    while True:
        count += 1 
        if number == predict_number:
            # выход из цикла, если угадали
            break
        else:
            if number > predict_number:
                down_boundary = predict_number
                step = int((top_boundary - predict_number)/2)
                predict_number += step if step > 0 else 1  
            else:
                top_boundary = predict_number
                step = int((predict_number - down_boundary)/2)
                predict_number -= step if step > 0 else 1
                
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """

    # список для сохранения количества попыток
    count_ls = []
    # загадали список чисел
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    # находим среднее количество попыток
    score = int(np.mean(count_ls))

    return score

# RUN
if __name__=='__main__':
    print(f'Ваш алгоритм угадывает число в среднем за: {score_game(random_predict)} попыток')