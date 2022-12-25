<h1 align="center">
<img src="https://github.com/PersifoX/lidar/blob/main/READMEstatic/logo.png" title="Lego lidar" alt="logo">
<br><br>
Lidar (Модифицировано до колесной базы)
</h1><br>

#### Вид сбоку

![lidar](https://github.com/PersifoX/lidar/blob/main/READMEstatic/accb443b-1708-4169-b9df-2b96852cc43a.jfif)

#### Вид спереди

![lidar](https://github.com/PersifoX/lidar/blob/main/READMEstatic/3f2cf4cd-7b6c-4ba6-892d-91ff9aa191b8.jfif)

### Если вы собрали все правильно, лидар будет возвращать массив с 30-ю элементами типа <code>int</code>
### от 0 (лидар не видит препятствия) до 2249 (~225 см) <br>

Классы
======

## Lidar
### имеет 2 функции:
> <code>scan</code> - возвращает массив с 30-ю элементами типа <code>int</code> от 0 (лидар не видит препятствия) до 2249 (~225 см) <br>
> <code>printmap</code> - чертит карту на экране ev3 (БЕТА тест)

## Tools
### имеет 1 функцию:
> <code>find_longest_zeros</code> - возвращает индекс элемента с возмоным пространством

Параметры классов
-----------------

<code>class Lidar</code> имеет 3 необязательных параметра:<br>
    <code>-DualMode</code>:<br>
        Следует ли лидару инициализировать сразу 2 датчика (Инфакрасный и Ультразвуковой)<br>
        (По умолчанию лидар использует только Ультразвуковой)<br>
    <code>-Debug</code>:<br>
        Выводить ли элементы массива на экран ev3 (поочередно)<br>
    <code>-Speed</code>:<br>
        Скорость вращения лидара, чем меньше - тем лучше стабилизация. По умолчанию 30.<br>
<code>class Tools</code> имеет 1 необязательный параметр:<br>
    <code>-OptionalMap</code>:<br>
        Задает карту по умолчанию сразу для всех дочерних функций<br>
     
     
Полезные линки
==============
Все статик и презентация [тык](https://drive.google.com/drive/folders/1POTgSskfk5JdrRK0sexyEhDVIWgNqfNM?usp=sharing)

### Все кто принимал в этом участие:
[Valed](#)(Логистика)<br>
[Secondfox](https://persifox.space/)(Это я)<br>
[Sergey Ippolitov](https://github.com/i-sergh)(Наставник?)
