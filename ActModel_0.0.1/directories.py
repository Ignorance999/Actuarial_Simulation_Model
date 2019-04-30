"""
This file houses hard-coded filepaths used in other modules,
and replaces the path separator with an OS-specific one
"""
import os

def format_path(win_path):
    return os.path.join(win_path.split("\\"))

accumm_test_path   = format_path(".\\test_output\\accum.txt")
gentable_test_path = format_path(".\\test_input\\Table.txt")

# input.py directories
test_input_dir  = format_path(".\\test_input\\")
mpf_dir         = format_path(".\\MPF\\")
script_dir      = format_path(".\\script\\")
test_output_dir = format_path(".\\test_output\\accum.txt")

# input.py single-input paths 
report_var_test_path    = format_path(".\\test_output\\REPORTVAR.txt")
output_format_test_path = format_path(".\\test_output\\out1.txt")

# input.py keygen-tables paths
prod_table_path   = format_path(".\\Prod\\PROD.txt")
scen_table_path   = format_path(".\\Prod\\scen.txt")
global_table_path = format_path(".\\Prod\\GLOBAL.txt")


