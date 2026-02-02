# FIXME: ImportError: module 'non_existent_module' not found
import non_existent_module

def reverse_string(s):
    # FIXME: LogicError: Logic doesn't reverse, just returns same
    return s

def count_vowels(s):
    count = 0
    i = 0
    while i < len(s):
        if s[i] in "aeiou":
            count += 1
        # FIXME: InfiniteLoop: i is never incremented
    return count

def parse_age(age_str):
    # FIXME: ValueError: if age_str is not a number
    return int(age_str)

def print_welcome():
  print("Welcome")
   # FIXME: IndentationError: unexpected indent
    print("To the club")
