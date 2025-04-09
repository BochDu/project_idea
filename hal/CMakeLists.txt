# 收集所有源文件
file(GLOB_RECURSE HAL_SOURCES "*.c")

# 创建一个库
add_library(hal_lib ${HAL_SOURCES})

# 如果你需要包含其他目录的头文件，可以在这里添加
target_include_directories(hal_lib PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}
)