from builders import LadaBuilder, VolkswagenBuilder, AudiBuilder, FerrariBuilder
from factory import Factory

BUILDERS = {
    '1': LadaBuilder,
    '2': VolkswagenBuilder,
    '3': AudiBuilder,
    '4': FerrariBuilder
}


def main():
    print('''
    Введите номер варианта автомобиля:
    1 - Lada,
    2 - Volkswagen,
    3 - Audi,
    4 - Ferrari
    ''')
    model_choice = input('>>> ')
    while model_choice not in BUILDERS.keys():
        print('Некорректный ввод, попробуйте снова')
        model_choice = input('>>> ')

    print('''
    Как поступить с результатом:
    1 - открыть,
    2 - сохранить в файл
    ''')
    save_choice = input('>>> ')
    while save_choice not in ['1', '2']:
        print('Некорректный ввод, попробуйте снова')
        save_choice = input('>>> ')

    if save_choice == '2':
        print('Введите название файла для сохранения без расширения')
        filename = input('>>> ')
        filename = "".join(x for x in filename if x.isalnum()) + '.png'
    else:
        filename = None

    factory = Factory()
    factory.builder = BUILDERS[model_choice]
    factory.construct()
    factory.get_result(save_choice, filename)


if __name__ == '__main__':
    main()
