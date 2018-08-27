# god of war boss battle
from sys import exit
from random import randint

class Fighter(object):
    # 父类，衍生出player和boss

    def __init__(self, name, hp, atk, skills):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.skills = skills

    # def round_act(self, action):
    #     # 打印动作的描述
    #     print(f"{self.name}{self.skills[action].describ}")

        # 返回该动作的结果


class Player(Fighter):
    # 这个类，进行角色属性的定义，角色每回合动作的具体执行

    # 玩家特有属性，怒气值。初始为100
    def __init__(self, name, hp, atk, skills, guard=50, speed=50, rage=100):
        super().__init__(name, hp, atk, skills)
        self.rage = rage
        self.guard = 50
        self.speed = 50


    # 每回合动作
    def round_act(self, action):
        player_act = self.skills[action]
        # 打印动作描述
        print(f"{self.name}{player_act.describ}")
        # 角色状态更新，造成伤害，防御力，速度，怒气值
        self.damage_to_boss = player_act.damage
        self.guard += player_act.guard_plus
        self.speed += player_act.speed_plus
        # self.round_property = {
        #     "damage_to_boss": player_act.damage,
        #     "self_guard_plus": player_act.guard_plus + self.guard,
        #     "self_speed_plus": player_act.speed_plus + self.speed
        # }
        self.rage += player_act.rage_plus
        if self.rage > 100:
            self.rage = 100
        
        # 将状态变更返回
        return self

    # 打印并返回玩家指令列表
    def show_commands(self):
        print("\n请做出你的应对措施: \n")
        command_list = {}
        key_list = list(self.skills.keys())
        for command in range(len(key_list)):
            command_list[str(command+1)] = key_list[command]
            print(f"\t{command+1}. {key_list[command]}\n")
        
        return command_list

    def die(self):
        print("YOU DIE!")

class Boss(Fighter):
    # 对boss属性进行定义，boss动作执行
    # boss特有属性，韧性，在boss回合，如果玩家选择跟boss硬碰硬，但伤害能力没有达到boss韧性值，则反过来承受所有伤害
    # 韧性初始值100
    def __init__(self, name, hp, atk, skills, tough=100):
        super().__init__(name, hp, atk, skills)
        self.tough = tough
        
    def round_act(self, action):
        boss_act = self.skills[action]
        # 打印boss动作起始描述
        print(f"{self.name}{boss_act.describ['start']}")

        # boss状态更新
        self.tough += boss_act.tough_plus
        self.guard_break = boss_act.guard_break
        self.skill_speed = boss_act.skill_speed
        self.damage_to_player = boss_act.damage
        # self.round_property = {
        #     # damage, guard_break, skill_speed, tough_plus
        #     "damage_to_player": boss_act.damage,
        #     "guard_break_to_player": boss_act.guard_break,
        #     "skill_speed": boss_act.skill_speed,
        #     "self_tough_plus": boss_act.tough_plus,
        #     "choice_true": boss_act.describ["choice_true"],
        #     "choice_false": boss_act.describ["choice_false"]
        # }

        # 返回状态变更
        return self

    def die(self):
        print("已屠杀猎物！")

class Scene(object):

    # 场景
    def __init__(self, action, describ):
        self.action = action
        self.describ = describ

    def enter(self):
        print(self.describ)



class Engine(object):
    # 这个类，进行回合的推进。数据的保存。玩家指令的输入。

    def __init__(self, player, boss):
        self.current_player = player
        self.current_boss = boss


    # 玩家操作
    def play(self):
        # 输入指令，确定当前回合，增加回合
        self.round_boss(self.current_player, self.current_boss)

    def round_boss(self, player, boss):
        # boss回合，首先是打印出boss动作前缀，得到boss动作的数据变更
        boss_skills_list = list(boss.skills.keys())
        boss = boss.round_act(boss_skills_list[randint(0, len(boss_skills_list)-1)])

        # 打印玩家指令列表
        command_list = player.show_commands()
        # 玩家做出指令
        choice = input("> ")
        # 玩家角色做出动作，得到玩家角色动作的数据变更
        player = player.round_act(command_list[choice])
        # 显示玩家做出选择的后果
        player, boss = self.round_result(player, boss)
        
        # 如果会返回结果，说明双方HP均未降低至0以下，游戏继续，进入下一回合
        
        # 进入玩家回合。
        self.round_player(player, boss)

    def round_player(self, player, boss):
        print("\n>> 到你的回合了")
        # 获取玩家指令，并打印
        command_list = player.show_commands()

        # 玩家输入指令
        choice = input("> ")

        # 玩家角色做出动作，玩家数据变更
        player = player.round_act(command_list[choice])


        # 将玩家和boss数据反馈
        self.round_result(player)

        # 进入boss回合
        self.round_boss(player, boss)


    def round_result(self, player, boss=None):
        # 确定双方黄hp，任何一方死亡，进入死亡场景

        # boss回合的情况
        if boss:

            # boss攻击的破防能力、技能速度大于玩家防御和速度，韧性大于玩家攻击时，仅有玩家收到攻击
            if boss.guard_break > player.guard or boss.skill_speed > player.speed and boss.tough > player.damage_to_boss:
                self.current_player.hp -= boss.damage_to_player
                print("\noh!bad  choice\n")
                print(f"{self.current_boss.name}的血量减少0")
                print(f"{self.current_player.name}的血量减少{boss.damage_to_player}")
            # boss攻击奏效，但玩家攻击大于boss韧性，boss也会受到伤害
            elif boss.guard_break > player.guard and boss.skill_speed > player.speed and boss.tough < player.damage_to_boss:
                self.current_player.hp -= boss.damage_to_player
                self.current_boss.hp -= player.damage_to_boss
                print("\nWell, not bad.\n")
                print(f"{self.current_boss.name}的血量减少{player.damage_to_boss}")
                print(f"{self.current_player.name}的血量减少{boss.damage_to_player}")
            # boss破防能力低于玩家，且技能速度低于玩家速度，此次攻击无效
            elif boss.guard_break < player.guard and boss.skill_speed < player.speed:
                print("\nnice choice\n")

            if self.current_player.hp <= 0:
                self.current_player.die()
                self.game_set(self.current_boss)
            elif self.current_boss.hp <= 0 and self.current_player.hp > 0:
                self.current_boss.die()
                self.game_set(self.current_player)

        # 玩家回合
        else:
            
            # 玩家在自己回合中做出有伤害的操作
            if player.damage_to_boss:
                self.current_boss.hp -= player.damage_to_boss
                print(f"{self.current_boss.name}的血量减少{player.damage_to_boss}")
                
                # 如果boss死亡
                if self.current_boss.hp < 0:
                    self.current_boss.die() 
                    self.game_set(self.current_player)

            # 玩家在自己回合的动作没伤害
            else:
                print("what are you fxxking doing?")

        # 确定回合，对比数据，输出战斗结果
        return self.current_player, self.current_boss

    def game_set(self, winner):
        print(f"winner is {winner.name}")
        exit(0)

class Action(object):

    # 动作，比如闪避，卢恩符文，攻击
    # 每个动作都有固有属性
    # 1. 攻击力 2. 破甲能力（决定是否可防御） 3. 速度加成（决定是否可闪避） 
    def __init__(self, describ, damage):
        self.damage = damage
        self.describ = describ


class BossAction(Action):
    # boss动作的属性，有描述，伤害，破甲能力，技能速度, 韧性加成，错误选择的后果
    def __init__(self, describ, damage, guard_break, skill_speed, tough_plus):
        super().__init__(describ, damage)
        self.guard_break = guard_break
        self.skill_speed = skill_speed
        self.tough_plus = tough_plus
        # self.bad_choice = bad_choice

class PlayerAction(Action):
    # 玩家动作的属性，有描述，伤害，防御加成，速度加成，当前是否可用

    def __init__(self, describ, damage, guard_plus, speed_plus, rage_plus=0):
        super().__init__(describ, damage)
        self.guard_plus = guard_plus
        self.speed_plus = speed_plus
        self.rage_plus = rage_plus
        


class Battle(object):
    
    # 战斗，基础属性有1. 回合数；2. 玩家；
    def __init__(self, player, boss):
        self.player = player
        self.boss = boss
        self.round = 0






# BOSS动作创建
ice_ball = BossAction({
    "start": "的双手冒出冷气，向你射出了无数的冰球!",
    "choice_true": "哦吼，你成功躲过了这次攻击",
    "choice_false": "冰球追踪着你，一齐向你打击过来！！"
}, 50, 100, 999, 0)
fire = BossAction({
    "start": "咏唱了一段咒文，地板迅速变红，热气袭面而来...",
    "choice_true": "哦吼，你成功躲过了这次攻击",
    "choice_false": "地面下喷射出了岩浆，你受到了重创！！"
}, 150, 999, 30, 0)
thunder = BossAction({
    "start": "悬浮在半空，用权杖划出了一道弧线，权杖上闪烁着雷光...",
    "choice_true": "哦吼，你成功躲过了这次攻击",
    "choice_false": "强光闪烁，你未能反应过来，受到了雷电的重创！！！"
    }, 50, 999, 0, 999)
jump = BossAction({
    "start": "发出红光，纵身一跃...",
    "choice_true": "哦吼，你成功躲过了这次攻击",
    "choice_false": "你没能躲过这次从天而降的攻击，整个人被踩在了脚下，硬生生挨下了数次踢击！！"
    }, 30, 999, 50, 999)
rush = BossAction({
    "start": "摆出了助跑的姿势，以迅雷般的速度向你冲来...",
    "choice_true": "哦吼，你成功躲过了这次攻击",
    "choice_false": "你根本没能反应过来，被狠狠的冲撞后，整个人被砸在了地上，还没能缓过神来，又被甩飞，砸到了岩石上！！！"
    }, 80, 999, 999, 999) # 必中技能，除非使用斯巴达之怒

boss_skills = {
    "iceBall": ice_ball,
    "fire": fire,
    "thunder": thunder,
    "jump": jump,
    "rush": rush
}

# 玩家动作创建
attack = PlayerAction("挥舞起混沌之刃，地狱之火随着刀刃飞舞...", 200, 0, 0, 30)    # 平A
runes = PlayerAction("发动了霜巨人的狂暴，抡起利维坦之斧疯狂砸地，像是在给对手拜年", 500, 50, 80)   # 卢恩符文攻击
dodge = PlayerAction("漂亮的闪躲，你成功躲过了敌人的攻击", 0, 0, 200)     # 闪避
guard = PlayerAction("面对敌人的攻击，你沉稳的架起了盾牌，成功的化解了这次的危机", 0, 200, 0, 20)     # 防御
sparta = PlayerAction("斯巴达的血液沸腾，你激活了全身的愤怒，震开了敌人！", 0, 9999, 9999, -100)    # 斯巴达之怒 

player_skills = {
    "attack": attack,
    "runes": runes,
    "dodge": dodge,
    "guard": guard,
    "sparta": sparta
}

# self, name, hp, atk, skills, guard=50, speed=50, rage=100
# name, hp, atk, skills, tough=100):
kratos = Player("Kratos", 300, 100, player_skills)
zeus = Boss("Zeus", 800, 100, boss_skills)

battle = Engine(kratos, zeus)
battle.play()