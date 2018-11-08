import requests
save_room = []
r = requests.post("http://mazes.10x.org.il/")
maze_id = r.json()['maze_id']


def find_room(code, save_room):
    save_room.append(code)

    room = requests.get(f"http://mazes.10x.org.il/{maze_id}/{code}/")
    exit = room.json()
    total = exit['score']

    req = exit['exits']
    for i in req:
        if i['code'] not in save_room:
            total += find_room(i['code'], save_room)
    return total



to = find_room(r.json()['start'],save_room )
sul = requests.post(f"http://mazes.10x.org.il/solve/{maze_id}/{to}/")
print(sul.json())




