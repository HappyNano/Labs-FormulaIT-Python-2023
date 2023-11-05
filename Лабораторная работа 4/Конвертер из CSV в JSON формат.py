# TODO импортировать необходимые молули
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    columns_names = []  # TODO считать содержимое csv файла
    data = []
    with open(INPUT_FILENAME, "r") as fin:
        is_first = True
        for line in fin.readlines():
            if is_first:
                columns_names = list(map(lambda x: x.replace('\n', ''), line.split(',')))
                is_first = False
            else:
                i = 0
                json_data = {}
                for col in line.split(','):
                    json_data.update({ columns_names[i]: col.replace('\n', '') })
                    i += 1
                data.append(json_data)

    with open(OUTPUT_FILENAME, "w") as fout:
        json.dump(data, fout, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
