# 设置 CMake 最低版本要求
cmake_minimum_required(VERSION 3.10)

# 设置项目名称
project(001)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 11)

# 添加子目录
add_subdirectory(app)
add_subdirectory(dal)
add_subdirectory(fun)
add_subdirectory(hal)
add_subdirectory(mid)

# 创建可执行文件
add_executable(chitu app/main.cpp)

# 链接库
target_link_libraries(chitu PRIVATE
    app_lib
    dal_lib
    fun_lib
    hal_lib
    mid_lib
)