from .models import MenuItem


class menu_category:
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.dic = {}

class menu_main:
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.list_sub = []

def create_menu_item():
    dic = {}  # 전체 메뉴 정리

    list_menu = MenuItem.objects.all()

    if list_menu is not None:
        for item in list_menu:
            if item.category_index not in dic:
                dic[item.category_index] = menu_category(item.category_index, item.category)

            if item.main_num not in dic[item.category_index].dic:
                dic[item.category_index].dic[item.main_num] = menu_main(item.main_num, item.main_name)

            if 0 < item.sub_num:
                dic[item.category_index].dic[item.main_num].list_sub.append((item.sub_num, item.sub_name))
    else:
        raise 'MenuItem is null.'

    return dic
'''
    for key, value in dic.items():
        print(key, ":", value.name)

        for key2, value2 in value.dic.items():
            print(key2, ":", value2.name)

            for item in value2.list_sub:
                print(item)
'''

