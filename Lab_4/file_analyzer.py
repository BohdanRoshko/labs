def get_file_stats(file_path):

    total_lines = 0
    empty_lines = 0
    lines_with_z = 0
    z_count = 0
    lines_with_and = 0

    with open(file_path, 'r') as file:
        for line in file:
            total_lines += 1

            if line.strip() == '':
                empty_lines += 1

            if 'z' in line:
                lines_with_z += 1
                z_count += line.count('z')

            if 'and' in line:
                lines_with_and += 1

    stats = {
        'total lines': total_lines,
        'empty lines': empty_lines,
        'lines with "z"': lines_with_z,
        '"z" count': z_count,
        'lines with "and"': lines_with_and
    }

    return stats

if __name__ == '__main__':
    while True:
        file_path = input("Введіть шлях до файлу: ")
        stats = get_file_stats(file_path)
        print("Статистика про файл:")
        print("File:", file_path)
        print("total lines:", stats['total lines'])
        print("empty lines:", stats['empty lines'])
        print('lines with "z":', stats['lines with "z"'])
        print('"z" count":', stats['"z" count'])
        print('lines with "and":', stats['lines with "and"'])
        
        another_file = input("Бажаєте проаналізувати ще один файл? (Так/Ні): ")
        if another_file.lower() != 'так':
            break
