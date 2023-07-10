import motor
import SG90
import HC_SR04
from PC远程控制LED import do_connect, create_udp_socket
import _thread
import time
from machine import PWM, Pin
import socket

def create_udp_socket():
    import socket
    
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", 7788)) # 绑定一个固定的端口
    return udp_socket

def motor_thread(l_pwm0, l_pwm1, r_pwm0, r_pwm1):
    while True:
        recv_data, sender_info = udp_socket.recvfrom(1024)
        #print("{}发送的数据：{}".format(sender_info, recv_data))
        recv_data_str = recv_data.decode("utf-8")
        print("解码后的数据：{}".format(recv_data_str))
        #time.sleep(0.01)  # 每0.01s接收一次数据
        
        # 根据接收到的udp数据控制电机运动
        if recv_data_str == "go_forward":
            motor.go_forward(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received go_forward')
        elif recv_data_str == "turn_left":
            motor.turn_left(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received turn_left')
        elif recv_data_str == "turn_right":
            motor.turn_right(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received turn_right')
        elif recv_data_str == "go_back":
            motor.go_back(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received go_back')
        elif recv_data_str == "stop":
            motor.stop(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received stop')
        elif recv_data_str == "rotate_clockwise":
            motor.rotate_clockwise(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received rotate_clockwise')
        elif recv_data_str == "rotate_anti_clockwise":
            motor.rotate_anti_clockwise(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received rotate_anti_clockwise')
            
            
def arm_thread(arm_l, arm_r):
    while True:
        recv_data, sender_info = udp_socket.recvfrom(1024)
        #print("{}发送的数据：{}".format(sender_info, recv_data))
        recv_data_str = recv_data.decode("utf-8")
        print("解码后的数据：{}".format(recv_data_str))
        #time.sleep(0.01)  # 每0.01s接收一次数据
        
        if recv_data_str == "arm_dance1":
            SG90.arm_dance1(arm_l, arm_r)
            print('received arm_dance1')
        elif recv_data_str == "arm_dance2":
            SG90.arm_dance2(arm_l, arm_r)
            print('received arm_dance2')
            
def head_thread(head):
    while True:
        recv_data, sender_info = udp_socket.recvfrom(1024)
        #print("{}发送的数据：{}".format(sender_info, recv_data))
        recv_data_str = recv_data.decode("utf-8")
        print("解码后的数据：{}".format(recv_data_str))
        time.sleep(0.2)  # 每0.2s接收一次数据
        
        if recv_data_str == "head_dance":
            print('ok')
            SG90.head_dance(head)
        
def HC_SR04_thread(trig, echo, l_pwm0, l_pwm1, r_pwm0, r_pwm1):
    distance_check = False
    while True:
        recv_data, sender_info = udp_socket.recvfrom(1024)
        #print("{}发送的数据：{}".format(sender_info, recv_data))
        recv_data_str = recv_data.decode("utf-8")
        print("解码后的数据：{}".format(recv_data_str))
        time.sleep(0.2)  # 每0.2s接收一次数据
        
        if recv_data_str == "turn on distance check":
            distance_check = True
        elif recv_data_str == "turn off distance check":
            distance_check = False
        
        if distance_check:
            distance = HC_SR04.measure_distance(trig, echo)
            print("Distance: {:.2f} cm".format(distance))
            time.sleep(0.5)
            # 根据距离发送电机指令，始终与前方障碍物保持30cm的距离
            if distance < 30:
                motor.go_back(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            else:
                motor.go_forward(l_pwm0, l_pwm1, r_pwm0, r_pwm1)

    
if __name__ == "__main__":
    do_connect() # 让esp32连接wifi,让其拥有ip地址
    
    udp_socket = create_udp_socket() # 创建udp socket
    
    # 初始化硬件
    l_pwm0, l_pwm1, r_pwm0, r_pwm1 = motor.motor_init()
    arm_l, arm_r, head = SG90.SG90_init()
    trig, echo = HC_SR04.HC_SR04_init()
    
    # 创建并启动线程
    #_thread.start_new_thread(motor_thread, (l_pwm0, l_pwm1, r_pwm0, r_pwm1))
    #_thread.start_new_thread(arm_thread, (arm_l, arm_r))
    #_thread.start_new_thread(head_thread, (head,))
    #_thread.start_new_thread(HC_SR04_thread, (trig, echo, l_pwm0, l_pwm1, r_pwm0, r_pwm1))

    
    # 启动主线程
    while True:
        recv_data, sender_info = udp_socket.recvfrom(1024)
        #print("{}发送的数据：{}".format(sender_info, recv_data))
        recv_data_str = recv_data.decode("utf-8")
        print("解码后的数据：{}".format(recv_data_str))
        #time.sleep(0.01)  # 每0.01s接收一次数据
        
        # 根据接收到的udp数据控制电机运动
        if recv_data_str == "go_forward":
            motor.go_forward(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received go_forward')
        elif recv_data_str == "turn_left":
            motor.turn_left(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received turn_left')
        elif recv_data_str == "turn_right":
            motor.turn_right(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received turn_right')
        elif recv_data_str == "go_back":
            motor.go_back(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received go_back')
        elif recv_data_str == "stop":
            motor.stop(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received stop')
        elif recv_data_str == "rotate_clockwise":
            motor.rotate_clockwise(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received rotate_clockwise')
        elif recv_data_str == "rotate_anti_clockwise":
            motor.rotate_anti_clockwise(l_pwm0, l_pwm1, r_pwm0, r_pwm1)
            print('received rotate_anti_clockwise')
            
        elif recv_data_str == "arm_dance1":
            SG90.arm_dance1(arm_l, arm_r)
            print('received arm_dance1')
        elif recv_data_str == "arm_dance2":
            SG90.arm_dance2(arm_l, arm_r)
            print('received arm_dance2')
        elif recv_data_str == "throw":
            SG90.throw(arm_l, arm_r)
            print('received throw')
    

        
   
