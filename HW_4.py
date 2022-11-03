import math
import random as rd

# генеруємо числа по розподілу Гаусса, зручніще тестувати дробні чила, щоб їх відрязняти від індексів
# математичне очікування
mu = 5
# середньо-квадратичне відхилення
sigma = 55
# кількість елементів у списку
num_of_el = 25


def input_num(name):
    # функція здійснює контроль правильності введення даних
    try:
        num = int(input('Введіть натуральне число ' + name + ' '))
        if num <= 0:
            raise Exception("Число мaє бути більше 0")

        return num
    except:
        print('Має бути введено ціле число. Спробуйте ще раз')
        input_num(name)


def get_even_or_not_even(list_loc, even=True):
    # функція повертає новий список, який складається з елементів, які мають парні або непарні індекси
    # even - якщо True повертає елементи, які відповідають парним індексам, False - не парним.
    res = []
    for i, v in enumerate(list_loc):
        if not i % 2 == even:
            res.append(v)
    return res


def task_1():
    print('\n', "*" * 20, "завдання 1", "*" * 20, '\n')

    list_loc = [round(rd.gauss(mu, sigma), 2) for i in range(num_of_el)]
    print("*" * 25 + ' згенерований список ' + "*" * 25)
    print(list_loc, end='\n\n')

    print('парні елементи списку', get_even_or_not_even(list_loc))
    print('непарній елементи списку', get_even_or_not_even(list_loc, False))
    print('сума усіх елементів списку={}'.format(sum(list_loc)))
    print('сума усіх елементів списку, кращій підхід={}'.format(math.fsum(list_loc)))

    print('сума  парних елементів списку={}'.format(math.fsum([v if not i % 2 else 0 for i, v in enumerate(list_loc)])))
    print('сума  непарних елементів списку={}'.format(math.fsum([v if i % 2 else 0 for i, v in enumerate(list_loc)])))
    print('максимальний елемент списку={}'.format(max([v for i, v in enumerate(list_loc)])))

    dict_1 = {i: v for i, v in enumerate(list_loc)}
    print('індекс макс. елемента та елемент ', max(dict_1.items(), key=lambda b: b[1]))

    # дадаємо максимальний елемент до списку для перевірки коректності роботи алгоритму
    list_loc.append(max([v for i, v in enumerate(list_loc)]))
    # створюємо словник з ключем "індекс" та відповідним значенням списку.
    # В умовах задачі не було застережень з цього провиду
    dict_1 = {i: v for i, v in enumerate(list_loc)}
    print('індекс макс. елемента та елемент  (контроль правильності)', max(dict_1.items(), key=lambda b: b[1]))


def print_slice(list_loc):
    # функція здійснює друк списку по 5-елементів у рядку
    # це зроблено для кращого сприйняття вирішення задачі №3
    step = 5
    for i in range(0, len(list_loc), step):
        print(list_loc[i:i + step])


def task_3():
    print('\n', "*" * 20, "завдання 4", "*" * 20, '\n')
    num = input_num('кількість елементів у списку')
    # num кількість елементів у списку
    step = 5  # кількість елементів, який ми сортуємо у зрізі
    # генерація списку, вирішив не писати функцію із одного рядка
    list_loc = [round(rd.gauss(mu, sigma), 2) for i in range(num)]
    print("*" * 25 + ' згенерований список ' + "*" * 25)

    print_slice(list_loc)

    # варіант в одну строку для "рівномірної матірці", кратній step. reshape(size) не спрацьовую, коли
    # кількість елементів не кратно 5, наприклад 24
    # list=np.asarray( [sorted(list[i:i+step], reverse=  i % 2) for i in range (0,size,step)]).reshape(size).tolist()

    # сортуємо зрізи в одну строку, у результаті отримає список списків
    list_loc = [sorted(list_loc[i:i + step], reverse=i % 2) for i in range(0, len(list_loc), step)]

    # розгортаємо список у вихідний розмір, дійсно можно мозок звернути,
    # але що толку від цього синтаксичного цукру, коли є GIL
    list_loc = [item for i in list_loc for item in i]

    print("*" * 25 + ' відсортований список, друк строками ' + "*" * 25)
    print_slice(list_loc)
    print("*" * 25 + ' відсортований список одним рядком ' + "*" * 25)
    print(list_loc)


def multiplicity_2(fizz_loc, bizz_loc, num_loc):
    # функція здійснює перевірку кратності числа num, числам fizz та buzz

    res = (not num_loc % fizz_loc and not num_loc % bizz_loc and 'FB') or \
          (not num_loc % fizz_loc and 'F') or \
          (not num_loc % bizz_loc and 'B') or num_loc

    return res


def task_2():
    print('\n', "*" * 20, "завдання 2", "*" * 20, '\n')
    try:
        with  open('file_1.txt', 'r') as f:
            lines = [line.replace('\n', '').split(' ') for line in f]
            # контроль зчитаних даних
            print(lines)
            print('\n')

            # створюємо двумірний список. Кожна строка буде містити результат роботи функції multiplicity_2
            res = [[multiplicity_2(int(item[0]), int(item[1]), limit) for limit in range(1, int(item[2]) + 1)] for item
                   in lines]

            # примітка "для себе", дла розуменні логіки вкладених циклів в один рядок
            # list_loc = [item (# 1 for i in list_loc)  (# 2 for item in i) ]
            for i, item in enumerate(res):
                print('строка № {}'.format(i))
                print(item)

            f.close()
    except:
        print('щось пішло не так')


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
