import sys

import pdfkit


def main(html_path, pdf_path):
    pdfkit.from_file(html_path, output_path=pdf_path)


if __name__ == "__main__":
    html = sys.argv[1]
    pdf = sys.argv[2]

    main(html, pdf)
