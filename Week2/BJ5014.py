# F: 
F, S, G, U, D = map(int, input().split())

button_click = [0] * (F + 1)
isArrive = False

queue = list()
queue.append(S)
while queue:
    s = queue.pop(0)
    if s == G:
        isArrive = True
        break
    for ts in [s + U, s - D]:
        if ts == s:
            continue
        if 0 < ts <= F and button_click[ts] == 0:
            button_click[ts] = button_click[s] + 1
            queue.append(ts)

if isArrive:
    print(button_click[G])
else:
    print("use the stairs")