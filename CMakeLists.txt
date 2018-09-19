cmake_minimum_required(VERSION 3.6)

project(teng-examples CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF) # on g++ this ensures: -std=c++14 and not -std=gnu++14

message(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
if(UNIX)
    include(FindPkgConfig)
    pkg_check_modules(PKG_DEPS REQUIRED libteng)
else()
    find_library(TENG_LIBRARY teng)
    if(TENG_LIBRARY)
        set(PKG_DEPS_LIBRARIES ${TENG_LIBRARY})
    else()
        message(FATAL_ERROR "Failed to find tang library")
    endif()
    find_file (TENG_INCLUDE teng.h)
    if(TENG_INCLUDE)
        get_filename_component(TENG_INCLUDE_DIR ${TENG_INCLUDE} DIRECTORY)
        set(PKG_DEPS_INCLUDE_DIRS ${TENG_INCLUDE_DIR})
    endif()
endif()

message(STATUS "include directories = ${PKG_DEPS_INCLUDE_DIRS}")
message(STATUS "link libraries      = ${PKG_DEPS_LIBRARIES}")


file(GLOB TEMPLATES templates/*)
file(COPY ${TEMPLATES} DESTINATION ${CMAKE_BINARY_DIR}/templates/)

enable_testing()
add_subdirectory(cpp)
add_subdirectory(python)
add_subdirectory(tests)