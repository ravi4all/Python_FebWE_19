def player_health():
    health = 80
    return health

def enemy_health():
    health = 50
    return health

def game():
    p_h = player_health()
    # print(p_h)
    e_h = enemy_health()
    if p_h < e_h:
        print("Low Power...")
    else:
        print("Hit hard to win...")

game()