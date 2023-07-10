Page({
  onLoad: function(options) {
    console.log('Page loaded');
    // 在此处编写页面加载时的逻辑代码
    // 可以根据需要进行数据初始化、请求数据等操作
    // 在onLoad函数中创建变量
    this.udp = wx.createUDPSocket()
    this.udp.bind()
  },

  // 前进
  moveForward: function() {
    this.udp.send({
      address: '192.168.43.87',
      port: 7788,
      message: 'go_forward'
    })
    console.log('go_forward')
  },
  
  // 后退
  moveBackward() {
    this.udp.send({
      address: '192.168.43.87',
      port: 7788,
      message: 'go_back'
    })
    console.log('go_back')
  },
  
  // 左转
  moveLeft() {
    this.udp.send({
      address: '192.168.43.87',
      port: 7788,
      message: 'turn_left'
    })
    console.log('turn_left')
  },
  
  // 右转
  moveRight() {
    this.udp.send({
      address: '192.168.43.87',
      port: 7788,
      message: 'turn_right'
    })
    console.log('turn_right')
  },
  
  // 停止
  stop() {
    this.udp.send({
      address: '192.168.43.87',
      port: 7788,
      message: 'stop'
    })
    console.log('stop')
  },
  // 顺时针旋转
  rotateClockwise() {
    this.udp.send({
      address: '192.168.43.87',
      port: 7788,
      message: 'rotate_clockwise'
    })
    console.log('rotate_clockwise')
  },
  
  // 逆时针旋转
  rotateCounterClockwise() {
    this.udp.send({
      address: '192.168.43.87',
      port: 7788,
      message: 'rotate_anti_clockwise'
    })
    console.log('rotate_anti_clockwise')
  },
  
  // 挥手
  swingArm1() {
    this.udp.send({
      address: '192.168.43.87',
      port: 7788,
      message: 'arm_dance1'
    })
    console.log('arm_dance1')
  },
  
  // 快速挥手
  swingArm2() {
    this.udp.send({
      address: '192.168.43.87',
      port: 7788,
      message: 'arm_dance2'
    })
    console.log('arm_dance2')
  },

  // 投掷
  throw() {
    this.udp.send({
      address: '192.168.43.87', 
      port: 7788,
      message: 'throw'
    })
    console.log('throw')
  }
});
