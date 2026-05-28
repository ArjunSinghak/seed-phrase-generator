cmake_minimum_required(VERSION 3.10)
project(seed-phrase-generator VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(seed-phrase-generator
    src/main.cpp
    src/entropy.cpp
    src/mnemonic.cpp
    src/checksum.cpp
)

target_include_directories(seed-phrase-generator PRIVATE include)

enable_testing()
add_executable(test_seed_phrase
    tests/test_mnemonic.cpp
    src/entropy.cpp
    src/mnemonic.cpp
    src/checksum.cpp
)
target_include_directories(test_seed_phrase PRIVATE include)
target_link_libraries(test_seed_phrase PRIVATE GTest::GTest)
add_test(NAME mnemonic_test COMMAND test_seed_phrase)