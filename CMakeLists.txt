cmake_minimum_required(VERSION 3.16.3)
project(cats-vs-dogs)

find_package(OpenCV REQUIRED)
find_package(Eigen3 REQUIRED)

include_directories(${EIGEN3_INCLUDE_DIR})

add_executable(${PROJECT_NAME} consume/main.cpp)

target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})