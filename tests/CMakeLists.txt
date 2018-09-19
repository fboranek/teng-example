find_package(Boost COMPONENTS unit_test_framework filesystem REQUIRED)

include_directories(${PKG_DEPS_INCLUDE_DIRS})
link_libraries(${Boost_UNIT_TEST_FRAMEWORK_LIBRARY} ${Boost_FILESYSTEM_LIBRARY} ${Boost_SYSTEM_LIBRARY} ${PKG_DEPS_LIBRARIES})
add_definitions(-DBOOST_TEST_DYN_LINK)

add_executable(test_base test_base.cc)
add_executable(test_filesystem test_filesystem.cc)

add_test(
    NAME test_teng_base
    COMMAND test_base
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR})

 add_test(
    NAME test_filesystem
    COMMAND test_filesystem
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR})
