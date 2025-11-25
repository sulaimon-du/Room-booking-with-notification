from properties.rooms import create_room, get_room_info 


def new_room(room_name, description = None):
    create = create_room(room_name, description)
    if not create:
        info = get_room_info(room_name)
        return f"Комната успешно созданна. {info}"
    return create


def room_info(room_name):
    info = get_room_info(room_name)
    return [i for i in info]

    


