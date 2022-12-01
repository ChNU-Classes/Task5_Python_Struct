def chatroom_status(users_list):
    if len(users_list) == 0: return "no one online"
    if len(users_list) == 1: return f"{users_list[0]} online"
    if len(users_list) == 2:
        return f"{users_list[0]} and {users_list[1]} online"
    else:
        return f"{users_list[0]}, {users_list[1]} and {len(users_list) - 2} more online"



