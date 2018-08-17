# Map
#     - next_sence
#     - opening_sence
# Engine
#     - play
# Scence：场景
#     - enter
#     * Death
#     * Central Corridor: 中央控制室，夺取中子炸弹的地方
#     * Laser Weapon Aromory
#     * The Bridge: 中央走廊，游戏的起点
#     * Escape Pod：救生舱

# define Sence
class Sence(object):

    def __init__(self):
        pass

    def enter(self):
        pass


class Death(Sence):

    def enter(self):
        pass


class CentralCorridor(Sence):
    
    def enter(self):
        pass


class LaserWeaponAromory(Sence):
    
    def enter(self):
        pass


class TheBridge(Sence):
    
    def enter(self):
        pass


class EscapePod(Sence):
    
    def enter(self):
        pass


# define Map
class Map(object):

    def __init__(self, start_sence):
        pass

    def next_sence(self, scence_name):
        pass

    def opening_sence(self):
        pass

# define Engine
class Engine(object):

    def __init__(self, sence_map):
        pass

    def play(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()