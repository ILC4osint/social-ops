# pylint: disable=no-member
import argparse
from loguru import logger
from socint.adapters.ventric import VetricAdapter


def main():
    parser = argparse.ArgumentParser(description="Social Int")
    parser.add_argument("--query", required=True, help="Query string to search for.")
    parser.add_argument("--source", choices=["ventric"],
                        default="ventric",
                        help="Use source/outlet. Default is 'ventric'.")
    args = parser.parse_args()

    adapter = VetricAdapter(args.source)
    results = adapter.search_posts(args.query)

    for post in results:
        logger.INFO(post)

if __name__ == "__main__":
    main()
