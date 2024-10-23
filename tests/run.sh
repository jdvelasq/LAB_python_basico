#!/bin/bash

run_test() {
    local test_file=$1
    local test_name=$2

    echo "Running tests for $test_name..."
    pytest "$test_file" --maxfail=1 --disable-warnings -q
    if [ $? -eq 0 ]; then
        echo "$test_name passed"
    else
        echo "$test_name failed <--"
    fi
}

run_test "tests/test_pregunta_01.py" "pregunta_01"
run_test "tests/test_pregunta_02.py" "pregunta_02"
run_test "tests/test_pregunta_03.py" "pregunta_03"
run_test "tests/test_pregunta_04.py" "pregunta_04"
run_test "tests/test_pregunta_05.py" "pregunta_05"
run_test "tests/test_pregunta_06.py" "pregunta_06"
run_test "tests/test_pregunta_07.py" "pregunta_07"
run_test "tests/test_pregunta_08.py" "pregunta_08"
run_test "tests/test_pregunta_09.py" "pregunta_09"
run_test "tests/test_pregunta_10.py" "pregunta_10"
run_test "tests/test_pregunta_11.py" "pregunta_11"
run_test "tests/test_pregunta_12.py" "pregunta_12"