Будь ласка, напишіть програму, яка розраховує оцінку проекту за допомогою https://en.wikipedia.org/wiki/Three-point_estimation.
Програма просить користувача надати доступні завдання (принаймні одне) з 3 необхідними оцінками (a, m, b).
Після цього обчислює оцінку (E) і стандартне відхилення (SD) для кожного завдання за такими формулами:
```
E(task) = (a + 4m + b) / 6
SD(task) = (b − a) / 6
```
Нарешті, обчислює 95% довірчий інтервал (confidence interval (CI)) для проекту на основі https://en.wikipedia.org/wiki/Three-point_estimation#Project_management.
Це означає, що E(project) і SE (project) (SE(task) дорівнює SD(task) вище) повинні бути обчислені перед остаточною оцінкою

CI(project) = E(project) ± 2 × SE(project).

Остаточні значення мають бути надруковані так:
```
Project's 95% confidence interval: 100 ... 120 points
```
де 100 і 120 – значення мінімального та максимального CI(project).

**Приклад виконання**

![image](https://github.com/BohdanRoshko/labs/assets/107959377/c2e33cdc-d4b2-4d75-b088-1200dc793473)
