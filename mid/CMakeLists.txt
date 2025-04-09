# 收集所有源文件
file(GLOB_RECURSE MID_SOURCES "*.c")

# 创建一个库
add_library(mid_lib ${MID_SOURCES})

# 设置头文件包含路径
target_include_directories(mid_lib PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/../hal
)