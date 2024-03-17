def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r') as file:
            for line in file:
                name, salary_str = line.strip().split(',')
                salary = int(salary_str)
                total_salary += salary
                num_developers += 1

        average_salary = total_salary / num_developers if num_developers > 0 else 0
        return total_salary, average_salary

    except FileNotFoundError:
        print("Файл не знайдено")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

total, average = total_salary("workers.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
