# Arena
面试遇到的算法题:
王者农药新模式 -- "智慧王者", 提供五个英雄,假设各自血量和攻击力如下:

梦琪: 10000血, 100攻击力
程咬金: 5000血, 200攻击力
亚瑟: 2000血, 500攻击力
铠: 1000血, 1000攻击力
狄仁杰: 100血, 2000攻击力

地图被画成一张MxN的棋盘,左上角为英雄的出生地,右下角则为敌方基地.所有的格子中,要么是"敌方水晶塔", 要么是"回血包".其中,敌方水晶塔会对英雄造成x点伤害,
每个水晶塔有自己独立的伤害值,而加血卷轴可以恢复英雄的血量.当英雄的血量小于等于0时,英雄死亡,游戏结束.英雄每次只能向下或向右移动一个格子,知道达到敌方
基地的格子,摧毁基地取得胜利.
如果给定一张随机生成的地图如下,其中,负数代表敌方水晶塔的伤害值,正数代表回复血量值:
![如图](https://github.com/pythonob/Arena/blob/master/1.PNG)

问:
1. 选择哪个英雄,既可以保证胜利,又能提供最大攻击力? 请给出算法,在任意随机地图下都有效.即地图随机生成,针对每一种随机地图,算法都可以给出英雄选择.
2. 如上图给定的地图,应选择哪一个英雄?
3. 请给出以上算法所计算的最优路线
