import argparse

parser = argparse.ArgumentParser(prog="status_check_runner")

parser.add_argument(
    "--update-config",
    action="store_true",
    help="Update the configuration's JSON schema",
)
