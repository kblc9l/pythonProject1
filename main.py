from api_func import show_image, get_map_image_by_ll_z



ll = input('ВВеди координаты через запятую')
z = int(input('Введи маштаб от 0 до 21'))


show_image(get_map_image_by_ll_z(ll, z))

