test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest


run test_is_even python even_or_odd.py 1
assert_no_stderr
assert_exit_code 0
assert_in_stdout "no"

run test_bad_input python even_or_odd.py a
assert_exit_code 1
assert_in_stderr "ERROR: Argument must be an int"

run test_no_input python even_or_odd.py 
assert_exit_code 1
assert_in_stderr "ERROR: Missing int"
