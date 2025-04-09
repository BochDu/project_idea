# 嵌入式工程设计

## 分层结构
应用层 --- app
依赖： app -> mid,fun,dal
功能： 自动进料页面

功能层 --- fun
依赖： fun -> min,dal
功能： 呼吸灯，自动进料

设备抽象层 --- dal
依赖： dal -> mid,hal
功能： LED，自动进料通信协议

中间服务层 --- mid
依赖： mid -> hal
功能： 模块间发布订阅通信（权限管理），日志系统，内存管理，线程池，数据结构

硬件抽象层 --- hal
例子： GPIO，UART，TIMER

## 编译运行
```
python3 chitu.py
./build/chitu
```








