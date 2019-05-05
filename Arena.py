#!/user/bin/env python3
map1 = [
    [133, -523, -558, 846, -907, -1224, -1346, 787, -411, -1826],
    [-1478, -853, -1401, 341, -26, 759, -444, 174, -1594, -2000],
    [861, -584, 670, 696, 676, -1674, -1737, -1407, -484, 248],
    [458, -1669, -419, -382, -895, 732, -1278, -1802, -527, 862],
    [-1297, 544, -1943, 563, -380, -1268, 266, -1309, -1946, 85],
    [-1981, -1631, -168, 741, -211, -1070, -1873, -554, 243, -901],
    [849, 971, -21, -1111, 463, 944, -124, -1414, -1463, -1287],
    [70, -1886, -1159, -73, 555, -426, -190, -1750, -1028, -188],
    [-1220, -1654, -931, -1100, -433, -1643, -1281, -455, 904, -126],
    [-1494, -632, 243, 90, 993, 322, 32, -388, -225, 952],
]

heroes = [
    ['mengqq',10000,100],
    ['chengyaojin',5000,200],
    ['yase',2000,500],
    ['kai',1000,1000],
    ['direnjie',100,2000]
    ]

def walk(blood,maps,path=[[0,0]]):
    
    _pos = path[-1]
    blood += maps[_pos[0]][_pos[1]]

    if _pos == [len(maps)-1,len(maps[0])-1]: #走到了终点
        return path

    else: # 没到终点
        _next_pos = [0,0]
        if _pos[1] < len(maps[0]) -1 and blood + maps[_pos[0]][_pos[1]+1] >0: #可以向右移动
            _next_pos = [_pos[0],_pos[1]+1]
            path.append(_next_pos)
            return walk(blood, maps, path)

        elif _pos[0] <len(maps)-1 and blood + maps[_pos[0]+1][_pos[1]] >0: # 可以向下移动
            _next_pos = [_pos[0]+1,_pos[1]]
            path.append(_next_pos)
            return walk(blood, maps, path)
        
        else: # 不能向右,也不能向下
            for m in range(len(path)-1,0,-1):  # 找到最后一个向右移动的位置
                if path[m][1] - path[m-1][1] == 1:
                    length = len(path)
                    _path = path
                    for n in range(m,len(path)): # 血量回復
                        blood -= maps[path[n][0]][path[n][1]]
                    new_path = path[:m]  #路徑回復
                #檢查恢復到的點是否可以向下移動
                    if new_path[-1][0] < len(maps)-1 and blood + maps[new_path[-1][0]+1][new_path[-1][1]] >0:
                        _next_pos = [new_path[-1][0]+1,new_path[-1][1]]
                        new_path.append(_next_pos)
                        return walk(blood,maps,new_path)
            return None # 之前没有向右移动过,又不能继续向下,则说明没有路径


def get_max_attack(heroes): # 获取当前最大攻击力的英雄
    tmp = [0,0,0]
    for i in range(len(heroes)):
        if heroes[i][2] > tmp[2]:
            tmp = heroes[i]
    return tmp

def get_way(heroes,map):  #
    the_hero = get_max_attack(heroes)
    path = walk(blood = the_hero[1], maps=map1)
    if path:
        print("the hero is : {} !".format(the_hero[0]) )
        print("the path is : {}".format(path))
        return the_hero
    else:
        for i in range(len(heroes)):
            if heroes[i] == the_hero:
                heroes[i][1] = 0
                heroes[i][2] = 0
                get_way(heroes,map1)
    return None

get_way(heroes=heroes, map=map1)


