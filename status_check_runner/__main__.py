import sys

from . import main, update_config_json_schema
from .argparse import parser

if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])  # skip first argument (path to this file)

    if args.update_config:
        update_config_json_schema()
        sys.exit(0)

    sys.exit(main())
