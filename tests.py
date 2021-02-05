#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 5

def test_code():
    assert main.length3("apple", "potato", "tomato") == 17, 'length3("apple", "potato", "tomato") == 17 failed'
    assert main.length3("a", "aaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa") == 32, 'length3("a", "aaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa") == 32'

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
