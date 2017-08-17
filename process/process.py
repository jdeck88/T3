import argparse
from .ocr import run_ocr
from .discovery import run_discovery

"""process.Process: provides entry point main()."""
__version__ = "0.1.0"

# main class
def main():
    parser = argparse.ArgumentParser(
            description="T3: A Toolset for processing Text and building Taxonomies",
    )

    parser.add_argument (
        "task",
        metavar="[ocr,cleanup,keywords,discovery,build_owl]",
        help="Choose one of the following options: ocr,cleanup,keywords,discovery,build_owl"
    )
    parser.add_argument(
        "input_file",
        help="Input PDF file location" 
    )
    parser.add_argument(
        "output_file",
        help="Output Text file location"
    )

    args = parser.parse_args()

    if args.task == "ocr":
        run_ocr(args.input_file, args.output_file) 
    elif args.task == "cleanup":
        print("cleanup not implemented yet. but will operate on an input file and apply functions to cleanup file")
    elif args.task == "keywords":
        print("keywords not implemented yet. but will operate on an input file to generate a list of keywords")
    elif args.task == "discovery":
        run_discovery(args.input_file, args.output_file) 
    elif args.task == "build_owl":
        print("build_owl not implemented yet. but will operate on an an input CSV or TSV file to build an OWL ontology file")
    else:
        print ("must specify a valid task to begin")

