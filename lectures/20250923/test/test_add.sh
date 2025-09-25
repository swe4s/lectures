test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

#$ python mymath.py add 1 1
#2

run test_add_ints_1 python src/mymath.py add 1 1
assert_in_stdout 2
assert_exit_code 0

run test_add_ints_2 python src/mymath.py div 1 0
assert_in_stdout "Error: Division by zero"
assert_exit_code 1
