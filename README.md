Порівняння жадібного алгоритму та динамічного програмування для задачі розміну монет


Задача розміну монет передбачає знаходження мінімальної кількості монет, необхідних для формування заданої суми з використанням набору номіналів. Два поширені підходи для вирішення цієї задачі:

Жадібний алгоритм

Динамічне програмування (ДП)

Основні відмінності

Жадібний алгоритм

Опис:
Жадібний алгоритм повторно обирає найбільший номінал монети, що не перевищує залишок суми.

Переваги:

Простий у реалізації.

Ефективно працює для наборів монет, де найбільший номінал завжди забезпечує оптимальне рішення (наприклад, ).

Недоліки:

Не гарантує оптимального рішення для довільних наборів монет.

Може помилитися в ситуаціях, коли комбінація менших монет є кращою.

Динамічне програмування

ДП створює масив , де  представляє мінімальну кількість монет, необхідну для формування суми . Ітерації виконуються для всіх можливих номіналів монет для кожної суми до цільової.

Переваги:

Гарантує оптимальне рішення для будь-якого набору монет.

Ефективно працює з довільними комбінаціями номіналів.

Недоліки:

Вища обчислювальна вартість у порівнянні з жадібним алгоритмом для малих сум.

Потребує додаткової пам’яті для збереження таблиці ДП.

Результати експерименту

Експеримент проведено з цільовою сумою  та набором монет .


Час виконання (секунди)

Жадібний - 0.0

Динамічне програмування - 0.019893407821655273 
 

Аналіз

Жадібний алгоритм

Продуктивність:
Показав надзвичайно швидке виконання завдяки лінійній природі реалізації. Однак він може давати хибні результати для наборів монет, які не відповідають канонічній властивості (наприклад, ).

Масштабованість:
Ефективно працює з великими сумами, але лише для наборів монет, де він гарантує правильність.

Динамічне програмування

Продуктивність:
Продемонструвало повільніше виконання в порівнянні з жадібним алгоритмом через вкладені ітерації. Однак воно гарантує оптимальне рішення для будь-якого набору монет.

Масштабованість:
Обчислювальна вартість значно зростає з великими сумами, але алгоритм залишається надійним для довільних вхідних даних.

Висновок

Вибір між жадібним алгоритмом та динамічним програмуванням залежить від умов задачі:

Використовуйте жадібний алгоритм для стандартних наборів монет, де він гарантує правильність. Його простота і швидкість роблять його ідеальним для систем реального часу.

Використовуйте динамічне програмування для довільних наборів монет, де жадібний підхід не працює, або коли важлива точність, незважаючи на вищу обчислювальну вартість.

Для великих сум жадібний алгоритм швидший, але обмежений у застосуванні. Динамічне програмування хоч і повільніше, залишається більш універсальним і надійним вибором.