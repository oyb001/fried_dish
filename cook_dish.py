# coding:utf-8


class PourOil(object):
    """
    倒油动作
    """

    def __init__(self, name):
        self.name = name

    def run(self):
        """
        执行
        :return:
        """
        print(f"倒入:{self.name}")


class BMM(object):
    """
    主料焯水
    """

    def __init__(self, name):
        self.name = name

    def run(self):
        """
        执行
        :return:
        """
        print(f"主料焯水:{self.name}")


class PickUpPan(object):
    """
    起锅装盘
    """

    def __init__(self, name):
        self.name = name

    def run(self):
        """
        执行
        :return:
        """
        print(f"{self.name}:起锅装盘")


class AddSeason(object):
    """
    加入动作
    """

    def __init__(self, name):
        self.name = name

    def add_a(self):
        """
        执行
        :return:
        """
        print(f"加入主料:{self.name}")

    def add_b(self):
        """
        执行
        :return:
        """
        print(f"加入配料:{self.name}")


class Thicken(object):
    """
    勾芡
    """

    def __init__(self, time, name):
        self.time = time
        self.name = name

    def run(self):
        """
        执行
        :return:
        """
        print(f"勾芡:{self.name}:时间:{self.time}")


class Cook(object):
    """
    炒
    """

    def __init__(self, time):
        self.time = time

    def run(self):
        """
        执行
        :return:
        """
        print(f"炒持续时间:{self.time}:分")


class Warm(object):
    """
    炖
    """

    def __init__(self, time):
        self.time = time

    def run(self):
        """
        执行
        :return:
        """
        print(f"炖持续时间:{self.time}:分")


class Yxrs(object):
    """
    鱼香肉丝
    """

    def __init__(self):
        # 倒油
        PourOil("花生油").run()
        # 加入葱姜蒜(配料)
        AddSeason("葱姜蒜").add_b()
        # 加入肉丝、胡萝卜丝、黑木耳丝等(主料)
        AddSeason("肉丝、胡萝卜丝、黑木耳").add_b()
        # 炒
        Cook(2).run()
        # 勾芡
        Thicken(2, "勾兑XX").run()
        # 起锅装盘
        PickUpPan("鱼香肉丝").run()


class Qjrs(object):
    """
    青椒肉丝
    """

    def __init__(self):
        # 倒油
        PourOil("菜籽油").run()
        # 加入葱姜蒜(配料)
        AddSeason("葱姜蒜").add_b()
        # 3、加入肉丝、青椒丝等(主料)
        AddSeason("肉丝、青椒丝").add_b()
        # 炒
        Cook(3).run()
        # 起锅装盘
        PickUpPan("青椒肉丝").run()


class Ympgt(object):
    """
    排骨玉米汤
    """
    def __init__(self):
        # 主料焯水
        PourOil("主料焯水").run()
        # 3、加入排骨(主料)
        AddSeason("排骨").add_b()
        # 炖
        Warm(30).run()
        # 加入玉米(配料)
        AddSeason("玉米").add_b()
        # 炖
        Warm(10).run()
        # 起锅装盘
        PickUpPan("排骨玉米汤").run()


if __name__ == "__main__":
    Yxrs()
    Qjrs()
    Ympgt()
