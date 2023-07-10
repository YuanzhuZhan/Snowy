from machine import Pin, PWM
import time

def motor_init():
    '''
    左右轮电机初始化
    '''
    # 左轮PWM引脚
    l_pwm0 = PWM(Pin(13), freq=1000)  # create PWM object from a pin
    l_pwm1 = PWM(Pin(12), freq=1000)  # create PWM object from a pin
    # 右轮PWM引脚
    r_pwm0 = PWM(Pin(14), freq=1000)  # create PWM object from a pin
    r_pwm1 = PWM(Pin(27), freq=1000)  # create PWM object from a pin
    return l_pwm0, l_pwm1, r_pwm0, r_pwm1

# 0度   p2.duty_u16(1638)  # set duty cycle from 0 to 65535 as a ratio duty_u16/65535
# 90度  p2.duty_u16(4915)
# 180度 p2.duty_u16(8192)

def go_forward(l_pwm0, l_pwm1, r_pwm0, r_pwm1):
    high = 50000
    l_pwm0.duty_u16(high)
    l_pwm1.duty_u16(0)
    r_pwm0.duty_u16(high)
    r_pwm1.duty_u16(0)
    
    
def turn_left(l_pwm0, l_pwm1, r_pwm0, r_pwm1):
    left = 50000
    right = 30000
    l_pwm0.duty_u16(left)
    l_pwm1.duty_u16(0)
    r_pwm0.duty_u16(right)
    r_pwm1.duty_u16(0)
    
def turn_right(l_pwm0, l_pwm1, r_pwm0, r_pwm1):
    left = 30000
    right = 50000
    l_pwm0.duty_u16(left)
    l_pwm1.duty_u16(0)
    r_pwm0.duty_u16(right)
    r_pwm1.duty_u16(0)
    
def go_back(l_pwm0, l_pwm1, r_pwm0, r_pwm1):
    high = 50000
    l_pwm0.duty_u16(0)
    l_pwm1.duty_u16(high)
    r_pwm0.duty_u16(0)
    r_pwm1.duty_u16(high)
    
def rotate_clockwise(l_pwm0, l_pwm1, r_pwm0, r_pwm1):
    high = 50000
    l_pwm0.duty_u16(high)
    l_pwm1.duty_u16(0)
    r_pwm0.duty_u16(0)
    r_pwm1.duty_u16(high)    
    
def rotate_anti_clockwise(l_pwm0, l_pwm1, r_pwm0, r_pwm1):
    high = 50000
    l_pwm0.duty_u16(0)
    l_pwm1.duty_u16(high)
    r_pwm0.duty_u16(high)
    r_pwm1.duty_u16(0)    

def motor_deinit(l_pwm0, l_pwm1, r_pwm0, r_pwm1):
    '''
    turn off PWM on the pin
    '''
    l_pwm0.deinit()
    l_pwm1.deinit()
    r_pwm0.deinit()
    r_pwm1.deinit()

def stop(l_pwm0, l_pwm1, r_pwm0, r_pwm1):
    high = 50000
    l_pwm0.duty_u16(0)
    l_pwm1.duty_u16(0)
    r_pwm0.duty_u16(0)
    r_pwm1.duty_u16(0)
    
#if __name__ == "__main__":
    #l_pwm0, l_pwm1, r_pwm0, r_pwm1 = motor_init()
    #go_forward(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
    #time.sleep(3)
    #go_back(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
    #time.sleep(3)
    #turn_left(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
    #time.sleep(3)
    #turn_right(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
    #time.sleep(3)
    #rotate_clockwise(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
    #time.sleep(3)
    #rotate_anti_clockwise(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
    #time.sleep(3)
    
    #motor_deinit(l_pwm0, l_pwm1, r_pwm0, r_pwm1)