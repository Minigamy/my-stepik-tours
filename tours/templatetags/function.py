import random
from django import template
from tours.data import tours

register = template.Library()


def random_six_tours():
    count = 1
    six_random_tours_dict = {}
    while count <= 6:
        random_num = random.randint(1, 16)
        if random_num not in six_random_tours_dict:
            six_random_tours_dict[random_num] = tours[random_num]
            count += 1
    return six_random_tours_dict


def depart_filter(departure):
    depart_name_dict = {}
    for dep_id, dep_value in tours.items():
        if dep_value['departure'] == departure:
            depart_name_dict[dep_id] = dep_value
    return depart_name_dict


@register.filter()
def tours_info(departure):
    search_tours_info = {'tours_count': 0, 'max_price': 0, 'min_price': 0, 'max_nights': 0, 'min_nights': 0}
    tours_price, tours_nights = [], []
    for dep_id, dep_value in tours.items():
        if dep_value['departure'] == departure:
            search_tours_info['tours_count'] += 1
            tours_price.append(dep_value['price'])
            tours_nights.append(dep_value['nights'])
    search_tours_info['max_price'] = max(tours_price)
    search_tours_info['min_price'] = min(tours_price)
    search_tours_info['max_nights'] = max(tours_nights)
    search_tours_info['min_nights'] = min(tours_nights)
    return search_tours_info


