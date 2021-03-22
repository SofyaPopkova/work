# Задание №1

from pprint import pprint
import os


def cookbook():
    cook_book = {

    }

    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            dish = f.readline().strip()
            if not dish:
                break
            number = int(f.readline())
            ingredient_list = list()
            for n in range(number):
                ingredient = f.readline().strip()
                separated = ingredient.split('|')
                cook_dict = {
                    'ingredient_name': separated[0],
                    'quantity': int(separated[1]),
                    'measure': separated[2]
                }
                ingredient_list.append(cook_dict)
            f.readline().strip()
            cook_book[dish] = ingredient_list
    return cook_book


pprint(cookbook())

# Задание №2


def get_shop_list_by_dishes(dishes, person_count):
    cookbook_main = cookbook()
    ingred_list = dict()

    for meal in dishes:
        if meal in cookbook_main:
            for ingr in cookbook_main[meal]:
                other_list = dict()
                if ingr['ingredient_name'] not in ingred_list:
                    other_list['measure'] = ingr['measure']
                    other_list['quantity'] = ingr['quantity'] * person_count
                    ingred_list[ingr['ingredient_name']] = other_list
        else:
            print('Данное блюдо отсутствует в кулинарной книге')
    return ingred_list


pprint(f'Нужное количество ингредиентов: {get_shop_list_by_dishes(["Запеченный картофель", "Фахитос"], 3)}')
print()

# Задание №3


def combine_files(path_1, path_2, path_3):
    file_path_1 = os.path.join(os.getcwd(), path_1)
    with open(file_path_1, 'r', encoding='utf-8') as f:
        data_1 = f.readlines()

    file_path_2 = os.path.join(os.getcwd(), path_2)
    with open(file_path_2, 'r', encoding='utf-8') as f:
        data_2 = f.readlines()

    file_path_3 = os.path.join(os.getcwd(), path_3)
    with open(file_path_3, 'r', encoding='utf-8') as f:
        data_3 = f.readlines()

    united_lst = [data_1, data_2, data_3]
    sorted_lst = sorted(united_lst, key=len)
    # pprint(sorted_lst)
    tuple_1 = tuple(sorted_lst[0])
    tuple_2 = tuple(sorted_lst[1])
    tuple_3 = tuple(sorted_lst[2])
    name_1 = str(sorted_lst[0][:])
    name_base_1 = os.path.basename(name_1)
    name_2 = str(sorted_lst[1][:])
    name_base_2 = os.path.basename(name_2)
    name_3 = str(sorted_lst[2][:])
    name_base_3 = os.path.basename(name_3)

    file_path_final = os.path.join(os.getcwd(), 'final.txt')
    with open(file_path_final, 'w', encoding='utf-8') as f_final:
        f_final.write(f'{name_base_1}/n')
        f_final.write(f'{len(tuple_1)}/n')
        f_final.writelines(tuple_1)
        f_final.write('\n')
        f_final.write(f'{name_base_2}/n')
        f_final.write(f'{len(tuple_2)}/n')
        f_final.writelines(tuple_2)
        f_final.write('\n')
        f_final.write(f'{name_base_3}/n')
        f_final.write(f'{len(tuple_3)}/n')
        f_final.writelines(tuple_3)

    return


combine_files('1.txt', '2.txt', '3.txt')