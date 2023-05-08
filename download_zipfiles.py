from pathlib import Path
from typing import List
from urllib.request import urlretrieve

from tqdm import tqdm


def load_lines(f: str) -> List[str]:
    lines = []
    with open(f, 'r') as fp:
        for line in fp.readlines():
            lines += [line]
    return lines


def main():

    root = Path('data')

    zipfile_dir = root / 'zip_files'
    zipfile_dir.mkdir(parents=True, exist_ok=True)

    metric_url_dir = root / 'urls' / 'metrics'

    urls = []
    for metric_url_file in metric_url_dir.glob('*.txt'):
        urls += load_lines(metric_url_file)

    for url in tqdm(urls):
        print(url)
        f = zipfile_dir / Path(url).name
        urlretrieve(url, f)


if __name__ == '__main__':
    main()
