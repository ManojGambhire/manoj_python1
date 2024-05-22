def game_win_lose(comp,you):
    if (comp==you):
        return None
    elif comp== 's':
        if(you=="w"):
            return False
        elif you=="g":
            return True
    elif comp=="W":
        if(you=="s"):
            return True
        elif (you=="g"):
            return False
    elif comp=="g":
        if(you=="s"):
            return False
        elif you=="w":
            return True
