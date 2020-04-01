import argparse
from py_comm_server import py_comm_server as pcs


def run_this_shit():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', action='store',
                        dest='simple_value',
                        help='Store a simple value')

    parser.add_argument('-c', action='store_const',
                        dest='constant_value',
                        const='value-to-store',
                        help='Store a constant value')

    parser.add_argument('-t', action='store_true',
                        default=False,
                        dest='boolean_t',
                        help='Set a switch to true')

    parser.add_argument('-f', action='store_false',
                        default=True,
                        dest='boolean_f',
                        help='Set a switch to false')

    parser.add_argument('-a', action='append',
                        dest='collection',
                        default=[],
                        help='Add repeated values to a list')

    parser.add_argument('-A', action='append_const',
                        dest='const_collection',
                        const='value-1-to-append',
                        default=[],
                        help='Add different values to list')

    parser.add_argument('-B', action='append_const',
                        dest='const_collection',
                        const='value-2-to-append',
                        help='Add different values to list')

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')

    results = parser.parse_args()

    print('simple_value     = {!r}'.format(results.simple_value))

    #print('This is what I input as arg:', results.simple_value)

    run_this_shit()
