cmake_minimum_required(VERSION 3.0)

project(hello)

set_property(SOURCE hello.cpp
	PROPERTY
	COMPILE_FLAGS "-g -O2 -Wall -Wunused")

add_executable(hello hello.cpp)
