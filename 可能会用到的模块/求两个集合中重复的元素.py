def 求交集(集合一, 集合二):
    return [循环参数 for 循环参数 in 集合一 if 循环参数 in 集合二]


集合一 = eval(input("请输如集合一(比如'(1,2,3)'):"))
集合二 = eval(input("请输如集合二(比如'(1,2,3)'):"))


print(set(求交集(集合一, 集合二)))
