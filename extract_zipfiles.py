import zipfile
from pathlib import Path


def main():
    zipfile_dir = Path('data') / 'zip_files'
    csvfile_dir = Path('data') / 'csv_files'
    print(zipfile_dir)
    for f in zipfile_dir.rglob('*'):
        print(f)
        with zipfile.ZipFile(f, 'r') as zip_ref:
            zip_ref.extractall(csvfile_dir)


if __name__ == '__main__':
    main()
