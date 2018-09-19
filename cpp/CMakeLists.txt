
include_directories(${PKG_DEPS_INCLUDE_DIRS})

add_executable(teng_base teng_base.cc)
target_link_libraries(teng_base ${PKG_DEPS_LIBRARIES})

add_test(
    NAME teng_base_test
    COMMAND teng_base
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR})

