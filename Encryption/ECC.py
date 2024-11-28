import math
import random
 
 
def extend_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, y, x = extend_gcd(b, a % b)
        return g, x, y - (a // b) * x
 
 
def niyuan(a, b):  # 计算a模b的逆元
    g, x, y = extend_gcd(a, b)
    if g != 1:
        print("a和b不互素，因此不存在逆元")
        return None
    else:
        return x % b
 
 
def tuoyuan_jia(P_x, P_y, Q_x, Q_y, a, b, p):  # 椭圆曲线中的加法
    if P_x == Q_x and P_y == Q_y:
        lada = ((3 * (P_x ** 2) + a) * niyuan(2 * P_y, p)) % p
        x3 = (lada ** 2 - P_x - Q_x) % p
        y3 = (lada * (P_x - x3) - P_y) % p
        return x3, y3
    elif P_x != Q_x:
        lada = ((Q_y - P_y) * niyuan(Q_x - P_x, p)) % p
        x3 = (lada ** 2 - P_x - Q_x) % p
        y3 = (lada * (P_x - x3) - P_y) % p
        return x3, y3
    elif P_x == Q_x and P_y != Q_y:
        return 0, 0
 
 
def tuoyuan_cheng(P_x, P_y, k, a, b, p):  # 椭圆曲线中的乘法，这里的k为乘于几，乘几那么就相当于几个点相加
    k = int(k)  # 确保k是整数类型
    new_x, new_y = P_x, P_y
    for i in range(k - 1):
        new_x, new_y = tuoyuan_jia(new_x, new_y, P_x, P_y, a, b, p)
    return new_x, new_y
 
 
def message_to_point(P_x, P_y, message, a, b, p):
    points = []
    n = 1
    for char in message:
        k = ord(char) + 1
        print(k)
        x, y = tuoyuan_cheng(P_x, P_y, k, a, b, p)
        points.append((x, y))
        print("{}=>({},{})".format(n, x, y))
        n += 1
    return points
 
def points_to_message(P_x, P_y,points,a, b, p):
    message = ""
    for point in points:
        x = point[0]
        y = point[1]
        fuP_x=P_x
        fuP_y=-P_y
        n=0
        while x!=P_x and y!=P_y:
            x , y=tuoyuan_jia(x, y, fuP_x, fuP_y, a, b, p)
            n+=1
        char=chr(n)
        message+=char
    print("解密后的字符串"+message)
    return message
 
def cal_jie(P_x, P_y, a, b, p):
    fuP_x = P_x
    fuP_y = -P_y % p
    new_x, new_y = P_x, P_y
    n = 1  # 初始化n
    while True:
        n += 1
        new_x, new_y = tuoyuan_jia(new_x, new_y, P_x, P_y, a, b, p)
        if new_x == fuP_x and new_y == fuP_y:
            return n + 1
 
 
def encode(P_x, P_y, Q_x, Q_y, k, points, a, b, p):
    poointsC1 = []
    poointsC2 = []
    kP_x, kP_y = tuoyuan_cheng(P_x, P_y, k, a, b, p)
    poointsC1.append((kP_x, kP_y))
    print("计算得密文为")
    print("c1")
    print(poointsC1)
    kQ_x, kQ_y = tuoyuan_cheng(Q_x, Q_y, k, a, b, p)
    for point in points:
        x = point[0]
        y = point[1]
        x = int(x)
        y = int(y)
        newkQ_x, newkQ_y = tuoyuan_jia(kQ_x, kQ_y, x, y, a, b, p)
        poointsC2.append((newkQ_x, newkQ_y))
    print("c2")
    print(poointsC2)
    return poointsC1, poointsC2
 
 
def decode(poointsC1, poointsC2, d, a, b, p):
    points = []
    C1 = poointsC1[0]
    C1_x = C1[0]
    C1_y = C1[1]
    inv_dC1_x, inv_dC1_y = tuoyuan_cheng(C1_x, C1_y,d,a, b, p)
    inv_dC1_y=-inv_dC1_y
    for point in poointsC2:
        C2_x = point[0]
        C2_y = point[1]
        #M_x=(C2_x-inv_dC1_x)%p
        #M_y=(C2_y-inv_dC1_y)%p
        M_x, M_y = tuoyuan_jia(C2_x, C2_y, inv_dC1_x, inv_dC1_y, a, b, p)
        points.append((M_x, M_y))
    print(points)
    return points
 
 
def main():
    print("****ECC椭圆曲线加解密****")
    while True:
        a = int(input("请输入椭圆曲线参数a(a>0)的值："))
        b = int(input("请输入椭圆曲线参数b(b>0)的值："))
        p = int(input("请输入椭圆曲线参数p(a>0)的值："))
 
        if 4 * (a ** 3) - 27 * (b ** 2) % p == 0:
            print("输入的参数有误，请重新输入")
        else:
            break
 
    print("user1：在如上坐标系中选一个素阶点P")
    P_x = int(input("请输入选取的x坐标值："))
    P_y = int(input("请输入选取的y坐标值："))
 
    n = cal_jie(P_x, P_y, a, b, p)
    d = int(input(("user1：请输入用于生成公钥的私钥d(<{})：".format(n))))
    Q_x, Q_y = tuoyuan_cheng(P_x, P_y, d, a, b, p)
    print("       计算Q=d*P得公钥Q为(" + str(Q_x) + "," + str(Q_y) + ")")
 
    mingwen = input("user2：请输入需要加密的字符串：")
    mingwen = mingwen.strip()  # 通过strip()方法可以去除字符串两端的空格
    print("明文映射的点为：")
    points1 = message_to_point(P_x, P_y, mingwen, a, b, p)
 
    k = input("user2：请输入秘密选择的k(<{})：".format(n))  # 这一步我们不用，我们选择用随机数
    # k = random.randint(1, n)  # 生成1到阶n之间的随机整数,用于计算kP,kQ
    print("user2:计算得密文为")
    poointsC1, poointsC2 = encode(P_x, P_y, Q_x, Q_y, k, points1, a, b, p)
 
    print("user1解密得到明文映射的点为:")
    points2=decode(poointsC1, poointsC2, d, a, b, p)
    points_to_message(P_x, P_y,points2,a, b, p)
 
 
if __name__ == "__main__":  # 函数入口
    main()
