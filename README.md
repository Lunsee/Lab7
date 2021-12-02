# Lab7
Ответы на контрольные вопросы:
1. Что такое рекурсивная подпрограмма?

Рекурсивная подпрограмма - подпрограмма, которая вызывает сама себя.

2. Что такое итерация?

Итерация - один проход (повторение) цикла.

3. Что такое стек? Каким образом стек используется при реализации рекурсии? Стек - хранилище данных, в который можно заносить данные только "снизу-вверх" и соответственно брать их "сверху-вниз". Можно провести аналогию с коробкой. Вещи мы складываем в нее попорядку снизу-вверх. А когда нам нужно их достать, мы можем только брать самые верхние.

Стек - это так же область оперативной памяти, предназначенная для программ, их функций и переменных. При запуске программы, все необходимые данные записываются в стек, а при выполнении достаются с конца. Поэтому в языках по типу c/c++, мы не можем инициализировать переменные с заранее неизвестным объемом данных. Для таких задач используется "Куча".

Выполнение рекурсивных функций это отличный пример стека. Каждый новый вызов функции становится "поверх" предыдущего. И функции завершают своё выполнение начиная с самой последней до самой первой.

4. Составьте рекурсивный и итерационный алгоритмы нахождения N!

Рекурсивный:
```python
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```
Итерационный:
```python
def factorial(n: int) -> int:
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    return fact
```

5. Объясните термин "косвенная рекурсия"?

Косвенная рекурсия - это способ выполнения функции, при котором функции внутри вызывают друг-друга.

Пример:
```python
def f(n):
    if n > 0:
        g(n - 1)

def g(n):
    print(n)

    if n > 1:
        f(n - 2)

```

6. 6. Если эффективность алгоритмов оценивать по количеству операторов присваивания, то, как вы думаете, какой алгоритм (рекурсивный или итерационный) будет наиболее эффективен? Обоснуйте на примере вычисления значений многочлена Лагранжа:
```python
def rec(x, n):
    print(1)
    if n == 1:
        return x
    elif n == 0:
        return 1
    a = rec(x, n - 1) * x * (2 * n + 1) / (n + 1) - rec(x, n - 2) * n / (n + 1)
    return a


def iter(x, n):
    p1 = 1
    p2 = x
    count = 2
    for i in range(2, n + 1):
        p1 = p2 * x * (2 * i + 1) / (i + 1) - p1 * i / (i + 1)
        b = p1
        p1 = p2
        p2 = b
        count += 4
    print(count)
    return p2


print(rec(5, 7))
print(iter(5, 7))

```
Оценка итерационного алгоритма предельна проста 2 оператора присваивание в самом начале. И на каждую итерацию приходится по 4 оператора.
Количество операторов присваивания (2 + 4n), то есть сложность LVL(N).

С рекурсивным по-сложнее. Каждый вызов функции это 1 оператор присваивания. Но каждая функция в себе вызывает ещё две. Соответветственно сложность данного алгоритма LVL(2^N)
Следовательно, итерационный алгоритм эффективней.

Вывод:
```python
1
... }21891
1
1.3361992451947833e+19
... }78
1.3361992451947833e+19

```
