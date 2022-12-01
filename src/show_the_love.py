def show_the_love(share_list):
    smallest = min(share_list)
    add_on = (sum(share_list) - smallest) * 0.25
    return [k + add_on if k == smallest else k * 0.75 for k in share_list]

