def BinarySearch(number):
    max = 100 # Задаем максимальное значение...
    min = 1 # ...и минимальное
    
    for i in range(min, max+1): # Цикл в диапазоне от начала до конца (+1 для должной работы цикла)
        guess = (max + min) // 2 # Угаданное число, деление ведется с округлением, иначе код не будет работать
        if guess == number: # Если угаданное число равно загадываемоему, тогда...
            return f"Attempt: {i} , The number {guess} is correct!" # ... выведется что число угадано, и работа цикла завершится (ключевое слово return останавливает цикл)
        elif guess < number: # Если угаданное число меньше загадываемого...
            print(f"Attempt: {i}, The number {guess} is smaller than guess!")
            min = guess + 1 # ...начало диапазона станет равным угадываемому числу (+ 1, т.к. данное число уже использовалось)
        elif guess > number: # Если угадываемое число больше загаданного...
            print(f"Attempt: {i}, The number {guess} is bigger than guess!")
            max = guess - 1 # ...конец диапазона равняется угадываемому числу (- 1, т.к. данное число уже использовалось)
        else:
            return "Something went wrong…" # Случай, если что то пойдет по одному месту
                
               
               
print(BinarySearch(55)) # Пример работы кода

# Output:
# Attempt: 1, The number 50 is smaller than guess!
# Attempt: 2, The number 75 is bigger than guess!
# Attempt: 3, The number 62 is bigger than guess!
# Attempt: 4, The number 56 is bigger than guess!
# Attempt: 5, The number 53 is smaller than guess!
# Attempt: 6, The number 54 is smaller than guess!
# Attempt: 7 , The number 55 is correct!
