def binary_search(arr, x):
    """
    Реализация алгоритма двоичного поиска.
    Возвращает индекс элемента, который меньше x, а следующий за ним больше или равен x.
    Если такого элемента нет, возвращает None.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] >= x:
            right = mid - 1
    return left

def main():
    # Ввод последовательности чисел
    input_sequence = input("Введите последовательность чисел через пробел: ")
    sequence = list(map(int, input_sequence.split()))

    # Ввод числа для поиска
    target_number = int(input("Введите число для поиска: "))

    # Сортировка списка по возрастанию
    sequence.sort()

    # Проверка, что введенное число находится в диапазоне введенной последовательности
    if not sequence or target_number < sequence[0] or target_number > sequence[-1]:
        print("Введенное число не соответствует заданной последовательности.")
        return

    # Поиск и вывод результата
    index = binary_search(sequence, target_number)
    print("Индекс элемента, который меньше введенного числа, а следующий за ним больше или равен: ", index)


if __name__ == "__main__":
    main()
