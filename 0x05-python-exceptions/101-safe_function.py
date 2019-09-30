#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except Exception as err:
        res = None
        print("Exception: {}".format(str(err)), file=sys.stderr)
    return res
