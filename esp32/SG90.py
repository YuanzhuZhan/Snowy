from machine import Pin, PWM
import time
from PC远程控制LED import do_connect

def SG90_init():
    '''
    三个舵机的PWM初始化
    '''
    # 左臂 
    arm_l = PWM(Pin(26), freq=50)  # create PWM object from a pin
    # 右臂
    arm_r = PWM(Pin(25), freq=50)  # create PWM object from a pin
    #arm_l.duty(256)  # set duty cycle from 0 to 1023 as a ratio duty/1023, (now 25%)
    # 头部
    head = PWM(Pin(33), freq=50)   # create PWM object from a pin
    return arm_l, arm_r, head

def arm_dance1(arm_l, arm_r):
    '''
    左右臂有节奏挥舞1
    '''
    interval = 0.1
    for i in range(10):
        arm_l.duty_u16(1638) # 左臂0度
        time.sleep(interval)
        arm_r.duty_u16(4915) # 右臂90度
        time.sleep(interval)
        arm_l.duty_u16(4915) # 左臂90度
        time.sleep(interval)
        arm_r.duty_u16(1638) # 右臂0度
        
        interval += 0.05
        
def arm_dance2(arm_l, arm_r):
    '''
    左右臂有节奏挥舞2
    '''
    interval = 0.1
    for i in range(10):
        arm_l.duty_u16(1638) # 左臂0度
        time.sleep(interval)
        arm_r.duty_u16(3800) # 右臂60度左右
        time.sleep(interval)
        arm_l.duty_u16(3800) # 左臂60度左右
        time.sleep(interval)
        arm_r.duty_u16(1638) # 右臂0度
        
def throw(arm_l, arm_r):
    '''
    左臂投掷
    '''
    interval = 0.1
    d_theta = 50
    theta = 3800
    # 蓄力
    for i in range(20):
        arm_l.duty_u16(theta)  
        theta -= d_theta
        time.sleep(interval)
        
    # 投掷
    arm_l.duty_u16(7000)
    time.sleep(interval)
    print('finish')
        
    
        
        
        
        
def head_dance(head):
    '''
    头部舵机运动
    '''
    for _ in range(10):  # 循环执行10次
        head.duty_u16(1638) #0度
        time.sleep(0.09)
        for i in range(1638, 8192, 500):
            head.duty_u16(i)
            time.sleep(0.2)
            

def SG90_deinit(arm_l, arm_r, head):
    '''
    turn off PWM on the pin
    '''
    arm_l.deinit()
    arm_r.deinit()
    head.deinit()
    
# 0度   p2.duty_u16(1638)  # set duty cycle from 0 to 65535 as a ratio duty_u16/65535
# 90度  p2.duty_u16(4915)
# 180度 p2.duty_u16(8192)
 
 
if __name__ == "__main__":
    arm_l, arm_r, head = SG90_init()
    #arm_dance1(arm_l, arm_r)
    arm_dance2(arm_l, arm_r)
    #head_dance(head)
    
    #throw(arm_l, arm_r)
    
    SG90_deinit(arm_l, arm_r, head)
    