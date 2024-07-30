import sys

from . import main
from .argparse import parser
from .config import update_config_json_schema

if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])  # skip first argument (path to this file)

    if args.update_config:
        update_config_json_schema()
        sys.exit(0)

    sys.exit(main())
