"""
This file houses hard-coded filepaths used in other modules,
and replaces the path separator with an OS-specific one
"""
import os

def format_path(win_path):
    return os.path.join(win_path.split("\\"))

accumm_test_path   = format_path(".\\test_output\\accum.txt")
gentable_test_path = format_path(".\\test_input\\Table.txt")
