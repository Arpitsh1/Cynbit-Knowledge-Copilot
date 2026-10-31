
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def main():

    if len(sys.argv) != 3:

        print(
            'Usage: python ingest_url.py '
            '"https://example.com/page" output.txt'
        )

        raise SystemExit(2)

    url = sys.argv[1]

    output = Path(sys.argv[2])

    response = requests.get(
        url,
        timeout=25,
        headers={
            "User-Agent": "CynbitAssessmentPrototype/1.0"
        }
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    for tag in soup([
        "script",
        "style",
        "nav",
        "footer",
        "header"
    ]):

        tag.decompose()

    text = "\n".join(
        line.strip()
        for line in soup.get_text("\n").splitlines()
        if line.strip()
    )

    output.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output.write_text(
        f"Source URL: {url}\n\n{text}\n",
        encoding="utf-8"
    )

    print(f"Saved extracted text to: {output}")

    print(
        "Review the extracted text for accuracy "
        "and permission before using it."
    )


if __name__ == "__main__":
    main()
