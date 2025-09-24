import argparse

def get_common_parser(description=None):
    parser = argparse.ArgumentParser(description=description)

    # universal flag for file path
    parser.add_argument(
        '-f', '--file',
        type=str,
        required=True,
        help='Path to input file'
    )

    return parser
