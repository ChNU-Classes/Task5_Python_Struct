def tallest_skyscraper(sky_list):
    return sum(1 for i in sky_list if sum(i) > 0)

