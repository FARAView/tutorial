import zipfile

zipfile_path = "./download/all_registrants.csv.zip"
unzip_dirpath = "./unzipped"

with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
    zip_ref.extractall(unzip_dirpath)

if __name__ == "__main__":
    pass
