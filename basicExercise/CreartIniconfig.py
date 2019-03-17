import configparser

# 先构建一个对象
config = configparser.ConfigParser()
class  CreatIni():

    # 来让我们写入几组数据
    # 先新增一个section
    config.add_section("开源优测")

    # 在新增的section下加key-value键值对
    config.set("开源优测", "微号", "DeepTest")
    config.set("开源优测", "口号", "自我娱乐娱乐")
    config.set("开源优测", "号外", "其实我开了好多号")

    # 再新增一个section，但不加key-value键值对
    config.add_section("我好孤单")
    # 写入文件
    with open('iniConfig.ini', 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    config.read("iniConfig.ini")
    # 获取它的所有section
    sections = config.sections()
    print(sections)

    # 获取section下所有的options
    for sec in sections:
        options = config.options(sec)
        print(options)

        # 根据sections和options获取对应的value值
    for sec in sections:
        for option in config.options(sec):
            print("[%s] %s=%s " % (sec, option, config.get(sec, option)))

