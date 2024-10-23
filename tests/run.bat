@echo off

setlocal enabledelayedexpansion

rem Function to run tests
:run_test
set test_file=%1
set test_name=%2

echo Running tests for %test_name%...
pytest %test_file% --maxfail=1 --disable-warnings -q
if %errorlevel% equ 0 (
    echo %test_name% passed
) else (
    echo %test_name% failed <--
)
goto :eof

rem Run tests for each question
call :run_test "tests\test_pregunta_01.py" "pregunta_01"
call :run_test "tests\test_pregunta_02.py" "pregunta_02"
call :run_test "tests\test_pregunta_03.py" "pregunta_03"
call :run_test "tests\test_pregunta_04.py" "pregunta_04"
call :run_test "tests\test_pregunta_05.py" "pregunta_05"
call :run_test "tests\test_pregunta_06.py" "pregunta_06"
call :run_test "tests\test_pregunta_07.py" "pregunta_07"
call :run_test "tests\test_pregunta_08.py" "pregunta_08"
call :run_test "tests\test_pregunta_09.py" "pregunta_09"
call :run_test "tests\test_pregunta_10.py" "pregunta_10"
call :run_test "tests\test_pregunta_11.py" "pregunta_11"
call :run_test "tests\test_pregunta_12.py" "pregunta_12"

endlocal