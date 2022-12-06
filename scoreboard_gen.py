import image_gen
import argparse

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description = "A simple script for adding a scoreboard like text to an image",
    )

    parser.add_argument("-v", "--version",
                        version=f"{parser.prog} version 1.0",
                        help="Print the current version of the program.",
                        action="version")

    parser.add_argument("file",
                        type=str,
                        help="Specify the file you want to create the image from.")

    parser.add_argument("image",
                        help="Specify the image you want to add the text to.",
                        type=str
                        )

    parser.add_argument("-o",
                        help="Specify the output file name, but not the directory",
                        type=str)

    parser.add_argument("-d",
                        help="specify the output directory, while the filename stays the same",
                        type=str)

    parser.add_argument("-q",
                        help="Dont show the generated image.",
                        action="store_true")

    parser.add_argument("--stats",
                        type=str,
                        required=True,
                        nargs="+",
                        help="Specify the statistics you want to display. Enter stats separated by a whitespace")

    return parser


def main() -> None:
    parser = init_argparse()
    parser.parse_args()
    args = parser.parse_args()

    image_gen.modify(args.stats, args.image, args.file, args.o, args.d, args.q)
    print(args.stats)


if __name__ == "__main__":
    main()