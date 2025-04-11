# 收集所有源文件
file(GLOB_RECURSE DAL_SOURCES "*.c")

# 创建一个库
add_library(dal_lib ${DAL_SOURCES})

# 如果你需要包含其他目录的头文件，可以在这里添加
target_include_directories(dal_lib PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/../mid
    ${CMAKE_CURRENT_SOURCE_DIR}/../hal
)

# 收集当前目录下的所有 .a 文件
file(GLOB_RECURSE STATIC_LIBRARIES "*.a")

# 添加静态库到项目中
foreach(LIB ${STATIC_LIBRARIES})
    get_filename_component(LIB_NAME ${LIB} NAME_WE)
    add_library(${LIB_NAME} STATIC IMPORTED)
    set_target_properties(${LIB_NAME} PROPERTIES IMPORTED_LOCATION ${LIB})
    # 将静态库链接到 app_lib
    target_link_libraries(app_lib PUBLIC ${LIB_NAME})
endforeach()