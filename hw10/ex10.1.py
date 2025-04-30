import re


def main(table_inp: list[list]):
    new_table = remove_null_rows(table_inp)
    new_table = remove_duplicate_rows(new_table)
    new_table = transpose(new_table)
    new_table = remove_null_rows(new_table)
    new_table = remove_duplicate_rows(new_table)
    new_table = replace_elements(new_table)
    split_by_colon(new_table)
    remove_surname(new_table)
    shuffle_date(new_table)
    new_table = transpose(new_table)
    return sorted(new_table, key=lambda row: row[3])


def check_row_null(row):
    for el in row:
        if el is not None:
            return False
    return True


def remove_duplicate_rows(table: list[list]):
    new_table = []
    n = len(table)
    m = len(table[0])
    for i in range(n):
        table[i].append(i)
    table.sort()
    i = 0
    while i < n:
        new_table.append(table[i])
        i += 1
        while i < n and table[i][:m] == table[i - 1][:m]:
            i += 1
    return [row[:m] for row in sorted(new_table, key=lambda row: row[m])]


def remove_null_rows(table: list[list]):
    new_table = []
    for row in table:
        if check_row_null(row):
            continue
        new_table.append(row)
    return new_table


def transpose(table: list[list]):
    new_table = []
    n = len(table)
    m = len(table[0])
    for j in range(m):
        row = []
        for i in range(n):
            row.append(table[i][j])
        new_table.append(row)
    return new_table


def replace_elements(table: list[list]):
    return [[el.replace("[at]", "@")
             .replace("true", "Выполнено")
             .replace("false", "Не выполнено")
             for el in row] for row in table]


def split_by_colon(table: list[list]):
    n = len(table)
    i = 0
    while i < n:
        if ':' in table[i][0]:
            table.insert(i + 1, [])
            for j in range(len(table[i])):
                el1, el2 = table[i][j].split(':')
                table[i][j] = el2
                table[i + 1].append(el1)
            i += 1
            n += 1
        i += 1


def remove_surname(table: list[list]):
    table[3] = [re.sub(R"([^ ]+) .*", R"\1", el)
                for el in table[3]]


def shuffle_date(table: list[list]):
    table[0] = [re.sub(R"(..)\.(..)\.(..)", R"\3.\2.\1", el)
                for el in table[0]]


if __name__ == '__main__':
    inp = [['04.05.23', 'sutevev88[at]yandex.ru:false', None, None, 'Сутевев Влад', 'Сутевев Влад'],
           ['03.05.08', 'ruslan88[at]mail.ru:true', None, None, 'Кошов Руслан', 'Кошов Руслан'],
           ['01.08.16', 'fovko63[at]yandex.ru:true', None, None, 'Фовко Марк', 'Фовко Марк'],
           [None, None, None, None, None, None],
           ['03.02.19', 'fivudak4[at]yahoo.com:true', None, None, 'Фивудяк Рустам', 'Фивудяк Рустам'],
           ['03.02.19', 'fivudak4[at]yahoo.com:true', None, None, 'Фивудяк Рустам', 'Фивудяк Рустам']]
    print(main(inp))
