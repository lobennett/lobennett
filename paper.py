import argparse
from metapub import PubMedFetcher
from datetime import datetime


def main():
    """
    Fetch paper metadata from DOI or PMID and write to papers.yml
    """
    # Parser
    parser = argparse.ArgumentParser(
        description="Fetch paper metadata from DOI or PMID"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--doi", type=str, help="DOI of the paper")
    group.add_argument("--pmid", type=str, help="PMID of the paper")
    parser.add_argument(
        "--read-on", type=str, help="Date read in YYYY-MM-DD format (defaults to today)"
    )
    args = parser.parse_args()

    # Fetching paper metadata
    fetch = PubMedFetcher()
    article = (
        fetch.article_by_doi(args.doi) if args.doi else fetch.article_by_pmid(args.pmid)
    )

    # Get identifier for output
    identifier = args.doi if args.doi else args.pmid

    # Get date - from flag or defaults to today
    read_date = args.read_on if args.read_on else datetime.now().strftime("%Y-%m-%d")

    # Writing to papers.yml
    with open("papers.yml", "a") as file:
        file.write("  - title: " + repr(article.title) + "\n")
        file.write("    authors: " + repr(article.authors) + "\n")
        file.write("    journal: " + repr(article.journal) + "\n")
        file.write("    year: " + str(article.year) + "\n")
        file.write(
            "    " + ("doi" if args.doi else "pmid") + ": " + repr(identifier) + "\n"
        )
        file.write("    read_on: '" + read_date + "'\n")


if __name__ == "__main__":
    main()
