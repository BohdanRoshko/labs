def task_estimation():
    tasks = []
    while True:
        a = float(input("Введіть найнижчу оцінку задачі (a): "))
        m = float(input("Введіть найбільш імовірну оцінку задачі (m): "))
        b = float(input("Введіть найвищу оцінку задачі (b): "))
        tasks.append((a, m, b))
        another = input("Бажаєте ввести ще одну задачу? (так/ні): ")
        if another.lower() != "так":
            break

    E_project = 0  # expected value of the project
    SE_project_square = 0  # sum of squares of standard deviations

    for a, m, b in tasks:
        E_task = (a + 4*m + b) / 6
        SD_task = (b - a) / 6
        E_project += E_task
        SE_project_square += SD_task ** 2

    SE_project = SE_project_square ** 0.5
    CI_min = E_project - 2*SE_project
    CI_max = E_project + 2*SE_project

    print("Project's 95% confidence interval: {:.2f} ... {:.2f} points".format(CI_min, CI_max))

if __name__ == "__main__":
    task_estimation()
