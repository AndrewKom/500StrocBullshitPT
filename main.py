# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#Работа с двумя целыми числами:
def numbers2():
    print('Введите первое число для работы:')
    a=int(input())
    print('Введите второе число для работы:')
    b=int(input())

    print(a,'+',b,'= ',
          a+b)
    print(a, '-', b, '= ',
          a - b)
    print(a, '*', b, '= ',
          a * b)
    print(a, '/', b, '= ',
          int(a / b))
    print(b, '/', a, '= ',
          int(b / a))

    print('Квадрат первого числа = ',
          a*a)
    print('Квадрат второго числа = ',
          b * b)


    if (a > b):
        print('Число ', a, 'больше числа ', b)
    elif (a == b):
        print('Число ', a, 'равняется числу ', b)
    else:
        print('Число ', b, 'больше числа ', a)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


#Начало сортировки слиянием, создание массива:
def sort():
    random_list_of_nums = [120, 45, 68, 250, 176, 100, 20, 30, 11000, 234, 567, 34, 12, 11, 1, 2, 3, 56]
    print('Изначальный массив для сортировки слиянием: ',
          random_list_of_nums)
    random_list_of_nums = merge_sort(random_list_of_nums)
    print('Отсортированный массив: ',
          random_list_of_nums)


def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:

            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


#Быстрая сортировка
def sort1():
    random_list_of_nums = [22, 5, 1, 18, 99,250, 176, 100, 20, 30, 11000,34,12,22,44,55,66,77,88,99,0,1,2,3,22,3,12,13,14,15]
    print('Изначальный массив для сортировки быстрой сортировкой: \n',
          random_list_of_nums)
    quick_sort(random_list_of_nums)
    print('Осортированный массив: \n',
          random_list_of_nums)




#Сумма чисел числа
def sumshisla():
    var_1 = int(input("Введите число: "))
    total = 0
    while var_1 > 0:
        rest = var_1 % 10
        total = total + rest
        var_1 = var_1 // 10
    print("Сумма цифр равна:", total)




#Количество цифр в числе
def kolchisla():
    var_1 = int(input("Введите число: "))
    count = 0
    while var_1 > 0:
        count = count + 1
        var_1 = var_1 // 10
    print("Количество цифр равно:", count)




#Факториалы
def fact():
    print('Введите число, по которому хотите получить факториал')
    number=int(input())

    result = 1
    while number >= 1:
        result *= number
        number -= 1
    print(result)




#:Жизненные советы и цитаты
def auf():
    print('Выберите номер жизненного совета который хотите получить 1-11')
    vibor = int(input())
    if vibor==1:
        print('Запоминайте что-то новое каждый день')

    elif vibor==2:
        print('Фокусируйтесь на настоящем')

    elif vibor==3:
        print('Кем бы ты ни был, кем бы ты не стал, помни, где ты был и кем ты стал.')

    elif vibor==4:
        print('Главное не иметь образ льва, а обладать силой волка.')

    elif vibor==5:
        print('В мире точно есть люди, которым мы нужны такие какие есть')

    elif vibor==7:
        print('Если волк молчит то лучше его — Не перебивать')

    elif vibor==8:
        print('Иногда жизнь — это жизнь, а ты в ней иногда')

    elif vibor==9:
        print('Лучше один раз упасть, чем сто раз упасть')

    elif vibor==10:
        print('Там, где есть овцы, волки всегда рядом')

    elif vibor==11:
        print('Лучше ужасный конец, чем ужас без конца')


    else:
        print('Не тот силен, кто не ошибается, а тот кто не боится ошибиться')



def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считаем корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — допустимый индекс, а элемент больше,
    # чем текущий наибольший, обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент больше не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    # Создаём Max Heap из списка
    # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)



def piramid():
    random_list_of_nums = [35, 12, 43, 8, 51,3,5,7,8,98,65,43,23,56,75,34,23,12,11]
    print('Массив до сортировки: ',
          random_list_of_nums)

    heap_sort(random_list_of_nums)
    print('Массив после сортировки',
          random_list_of_nums)



def test():
    print("Вас привествует тест по знанию общей информации, прошу, введите своё имя:")
    name=input()
    count=0
    print('Привествую, ',name, ', сегодня мы проверим твои знания и выведем оценку, начинаем!\n'
          'Первый вопрос: Когда началась Великая Отечественная война?\n'
          '1) 9 мая 1945 г.\n'
          '2) 22 июня 1941 г.\n'
          '3) 1 сентября 1939 г. \n' 
          '4) 3 сентября 1945 г.')
    otvet=int(input())



    if otvet==1:
        print('Вы ошиблись! Это дата окончания!')

    elif otvet==2:
        print('Конечно! Вы дали правильный ответ')
        count += 1

    elif otvet==3:
        print('Вы ошиблись! Это дата начала Второй мировой войны!')

    elif otvet==4:
        print('Вы ошиблись! Это дата окончания Второй Мировой войны!')

    else:
        print('Вы ошиблись с введенным числом, попробуете ответить на этот вопрос в следующий раз')

    print('Продолжим, ', name, ', следующий вопрос проверит твое знание Императоров\n'
                                'Второй вопрос: Кто был первым Императором России?\n'
                                '1) Иван Грозный\n'
                                '2) Пётр 1\n'
                                '3) Юрий Владимирович Долгорукий \n'
                                '4) Борис Николаевич Ельцин')
    otvet=int(input())

    if otvet == 1:
        print('Вы ошиблись! Это конечно не Иван Грозный!')

    elif otvet == 2:
        print('Конечно! Вы дали правильный ответ')
        count += 1

    elif otvet == 3:
        print('Вы ошиблись! Это конечно не Юрий Владимирович Долгорукий')

    elif otvet == 4:
        print('Вы ошиблись! Он был первым всенародно избранным Президентом Российской Федерации')

    else:
        print('Вы ошиблись с введенным числом, попробуете ответить на этот вопрос в следующий раз')

    print('Перейдем к следующему вопросу, ', name, ', надеюсь ты с легкостью на него ответишь\n'
                               'Третий вопрос: Какого животного боялся Уолт Дисней, который до 1947 года лично озвучивал Микки Мауса??\n'
                               '1) Мышей\n'
                               '2) Собак\n'
                               '3) Кошек \n'
                               '4) Утконосов')
    otvet=int(input())

    if otvet == 1:
        print('Вы правы! Как бы это странно не было, но именно мышей и боялся Уолт Дисней')
        count += 1

    elif otvet == 2:
        print('Ошибка! Собаки хоть и опасные существа, но Дисней их не боялся')

    elif otvet == 3:
        print('Вы ошиблись! Кошки очень милые существа, не надо о них так думать')

    elif otvet == 4:
        print('Вы ошиблись! Конечно же он не боялся утконосов! Как вы могли так подумать')

    else:
        print('Вы ошиблись с введенным числом, попробуете ответить на этот вопрос в следующий раз')

    print('Настало время 4 вопроса, ', name, ', тут мы обойдемся без мышей\n'
                                                   'Четвертый вопрос: Каким животным разрешён вход в мусульманскую мечеть?\n'
                                                   '1) Кошки\n'
                                                   '2) Собаки\n'
                                                   '3) Ястребы \n'
                                                   '4) Утконосы')
    otvet=int(input())

    if otvet == 1:
        print('Вы правы! Только кошка разрешен вход в мечеть. Это сделано в память о кошке Пророка')
        count += 1

    elif otvet == 2:
        print('Ошибка! Собаки опасны, куда их пускать в мечеть')

    elif otvet == 3:
        print('Вы ошиблись! Ястребы? Вряд ли такое могло произойти')

    elif otvet == 4:
        print('Вы ошиблись! Конечно же не  утконосы! Как вы могли так подумать!')

    else:
        print('Вы ошиблись с введенным числом, попробуете ответить на этот вопрос в следующий раз')

    print('Финал! ', name, ' , перейдем к Америке\n'
                                             'Пятый вопрос: В качестве чего задумывали использовать шпиль знаменитого нью-йоркского небоскрёба Эмпайр-стейт-билдинг его создатели??\n'
                                             '1) В качестве причальной мачты для дирижаблей\n'
                                             '2) В качестве телевизионной башни \n'
                                             '3) В качестве огромного громоотвода  \n'
                                             '4) В качестве смотровой вышки')
    otvet=int(input())

    if otvet == 1:
        print('Вы правы! 102-й этаж был причальной платформой со сходнями для подъёма на дирижабль')
        count += 1

    elif otvet == 2:
        print('Ошибка! Телевизор при помощи неё не посмотреть')

    elif otvet == 3:
        print('Вы ошиблись! Это был не громоотвод')

    elif otvet == 4:
        print('Вы ошиблись! Посмотреть красоты Америки без дирижабля от туда нельзя было')

    else:
        print('Вы ошиблись с введенным числом, попробуете ответить на этот вопрос в следующий раз')

    if count <=2:
        print('Ваша оценка 2. Подтяните знания и попробуйте пройти снова')
        count += 1

    elif count == 3:
        print('Ваша оценка 3. Неплохо, но и не хорошо, подтяните знания и возвращайтесь')

    elif count == 4:
        print('Ваша оценка 4. Хорошо! Но еще не отлично, сделайте вывод, где вы сделали ошибку и повторите')

    elif count == 5:
        print('Ваша оценка 5. Отлично! Вашим знаниям все завидуют, вы отлично справились!')


    print('-' * 100)




def vib():
    print('Введите номер функции,которую хотите запустить:'
          '\n0-Закончить работу'
          '\n1-Работа с двумя целыми числами'
          '\n2-Сортировка массива слиянием'
          '\n3-Сортировка массива быстрой сортировкой'
          '\n4-Сумма чисел числа'
          '\n5-Количество цифр в числе'
          '\n6-Факториал числа'
          '\n7-Если хотите получить жизненный совет'
          '\n8-Пирамидальная сортировка'
          '\n9-Тест'
          )

    vibor= int(input())

    if (vibor==1):
        numbers2()
        vib()

    elif(vibor==0):
        print('Спасибо за работу! Заканчиваем')

    elif (vibor==2):
        sort()
        vib()

    elif (vibor==3):
        sort1()
        vib()

    elif (vibor==4):
        sumshisla()
        vib()

    elif (vibor==5):
        kolchisla()
        vib()

    elif (vibor==6):
        fact()
        vib()

    elif (vibor==7):
        auf()
        vib()

    elif (vibor==8):
        piramid()
        vib()

    elif (vibor==9):
        test()
        vib()

    else:
        print('Вы ввели неправильно число, попробуйте заново')
        vib()

vib()