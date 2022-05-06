def get_new_search_filter_index(r):
    search_filter_index = -1

    if r == "Filter_Name":
        search_filter_index = 0
    elif r == "Filter_Address":
        search_filter_index = 1
    elif r == "Filter_Tel":
        search_filter_index = 2
    return search_filter_index