import time
import network
import machine

def do_connect():
    """
    连接wifi网络
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('nova 7 SE 5G', 'zyz2529443')
        i = 1
        while not wlan.isconnected():
            print('正在连接网络...{}'.format(i))
            time.sleep(0.5)
            i = i+1
    print('network config:', wlan.ifconfig())
    
def create_udp_socket():
    import socket
    
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", 7788)) # 绑定一个固定的端口
    return udp_socket


#if __name__ == "__main__":
    #do_connect() # 让esp32连接wifi,让其拥有ip地址
    
    #udp_socket = create_udp_socket() # 创建udp socket
    
    #led = machine.Pin(2, machine.Pin.OUT)
    
    #while True: # 接收udp数据
        #recv_data, sender_info = udp_socket.recvfrom(1024)
        #print("{}发送的数据：{}".format(sender_info, recv_data))
        
        #recv_data_str = recv_data.decode("utf-8")
        #print("解码后的数据：{}".format(recv_data_str))
        
        # 根据接收到的udp数据控制LED灯的亮灭
        #if recv_data_str == "light_on":
            #led.value(1)
        #elif recv_data_str == "light_off":
            #led.value(0)
        
    
