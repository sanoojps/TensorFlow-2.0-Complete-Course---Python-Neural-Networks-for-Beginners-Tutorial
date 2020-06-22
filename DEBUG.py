import sys
DEBUG = True

def debug(
    *msg,
    debug: bool = DEBUG
):
    if debug is True:
        _debug_with_args(*msg)

# logic
# expecting string message at odd indices
# values at even
# to print "value1 is 1 and value2 is 2"
# you send
# debug_args(
#       "value1 is",
#       1,
#       "and value2 is",
#       2
# )
def _debug_with_args(*argv):
    # get args
    # construct the format string
    string_interpolation_symbol = "{}"
    format_string = ""
    values = []
    for index,arg in enumerate(argv):
        # if string simply concatenate 
        if isinstance(arg,str) is True:
            format_string += (arg + " ")
        else:
            # requires interpolation
            format_string += (string_interpolation_symbol + " ")
            values.append(arg)

        # print(arg)

    print(
        format_string.format(
            *values
        )
    )

# _debug_with_args(
#     "But",
#     3,
#     2
# )

debug(
    "But",
    3,
    2
)

if __name__ == "__main__":
    # execute only if run as a script
    if len(sys.argv) == 2:
        msg = sys.argv[1]
        debug(msg=msg)

    elif len(sys.argv) == 3:
        msg = sys.argv[1]
        debug = sys.argv[2]
        debug(msg=msg, debug=debug)

    else:
        print("Nothing to debug")