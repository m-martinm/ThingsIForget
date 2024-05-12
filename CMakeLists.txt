cmake_minimum_required(VERSION 3.16)
project(Example_name)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Set C standard
set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED True)
set(CMAKE_EXPORT_COMPILE_COMMANDS True)
# Add the main executable
add_executable(${PROJECT_NAME} path/to/main.c.cpp)

if(WIN32)
    set_target_properties(${PROJECT_NAME} PROPERTIES SUFFIX ".exe")
elseif(UNIX)
    add_compile_options(-Werror -Wall -pedantic)
    # Set compiler flags for debug configuration
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g -fsanitize=address")
endif()

# find math library and link to all targets as default

find_library(MATH_LIBRARY m)
if(MATH_LIBRARY)
    link_libraries(${MATH_LIBRARY})
endif()

set(HEADER_DIRS path/to/one/dir path/to/other/dir)
include_directories(${HEADER_DIRS})

# Add subdirectory to find libraries for example
add_subdirectory(path/to/dir)
target_link_libraries(${PROJECT_NAME} PRIVATE example_library_name)  # Link the test with ModuleA

