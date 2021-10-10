

import init
import build
import sys

path = "."
sources = init.list_files(path, init.cpp_filter)
template = init.cmake_gen_library("mylibrary", sources, "include")

with open("CMakeLists.txt", "w") as fileHandle:
    fileHandle.write(template)

# print(template)
