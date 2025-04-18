import csv
import datetime
import matplotlib.pyplot as plt


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=';'))


def main():
    # Сообщения, присланные в ЦАП.
    # id, task, variant, group, time
    messages = load_csv('messages.csv')

    # Результаты проверок сообщений, присланных в ЦАП.
    # id, message, time, status
    checks = load_csv('checks.csv')

    # Состояния задач ЦАП.
    # task, variant, group, time, status, achievements
    statuses = load_csv('statuses.csv')

    # Таблица соответствия номеров групп и их названий.
    # id, title
    groups = load_csv('groups.csv')



    fig = plt.figure(figsize=(16, 10))
    plt.bar(groups_successes.keys(), groups_successes.values())
    plt.xticks(rotation=90)
    plt.show()


if __name__ == '__main__':
    main()
