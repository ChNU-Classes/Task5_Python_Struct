def filter_list(list_with_str_int):
    list_with_int = []
    for item in list_with_str_int:
        if isinstance(item, int):
            list_with_int.append(item)
    return list_with_int