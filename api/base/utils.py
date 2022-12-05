def crop_dict_values(item: dict):
    for each_dict in item:
        for key in each_dict.keys():
            value = each_dict[key]
            if len(each_dict[key]) > 40 and isinstance(each_dict[key], str):
                each_dict[key] = f"{value[:40]}..."
    return item
