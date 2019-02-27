
'''

class robot:
    population =0
    def  __init__(self,name):
        self.name=name
        print('Initializing {}'.format(self.name))
        #('(initlation {})’,format(self.name))

        robot.population+=1

    def die(self):
        robot.population-=1
        if robot.population==0:
            print("we have {:d} robot are working".format(robot.population))
        #('we have {:d} robots are  working’,format(robot.population))
        else:
            print("there are {:d}robot are working".format(robot.population))

''''''ls1=robot("lo-23")
ls1.die()
ls2=robot("kk-23")
ls2.die()''''''
#die 对象中的population 每次执行都是0

ls1=robot("lo-23")
ls2=robot("kk-23")
#以上会累加populaion的值
ls2.die()
ls1.die()
'''

