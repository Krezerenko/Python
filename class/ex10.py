import csv
import datetime
import matplotlib.pyplot as plt


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


def convert_groups(groups):
    return dict(groups)


WEEKDAY_NAMES = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")
MY_GROUP_ID = "14"


def get_activity_by_weekday(messages, group_id=None):
    result = {}
    for _, _, _, group, time in messages:
        if group_id is not None and group != group_id:
            continue
        # print(time)
        weekday = WEEKDAY_NAMES[parse_time(time).weekday()]
        if weekday not in result:
            result[weekday] = 0
        result[weekday] += 1
    return result


def get_successes_by_group(statuses, groups):
    result = {}
    for _, _, group, _, status, _ in statuses:
        if status != "6":
            continue
        if groups[group] not in result:
            result[groups[group]] = 0
        result[groups[group]] += 1
    return result


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

    id_to_group = convert_groups(groups)
    print(id_to_group)
    weekdays_activity = get_activity_by_weekday(messages, MY_GROUP_ID)
    groups_successes = get_successes_by_group(statuses, id_to_group)
    groups_successes = dict(sorted(groups_successes.items(), key=lambda x: x[1], reverse=True))
    print(groups_successes)
    fig = plt.figure(figsize=(16, 10))
    plt.bar(groups_successes.keys(), groups_successes.values())
    plt.xticks(rotation=90)
    plt.show()


if __name__ == '__main__':
    main()
