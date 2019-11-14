import os
import pandas as pd
import shutil
import datetime


def get_file_details(list_values, name, year, month, date, size):
    data = {'Filename': name,
            'Year': year,
            'Month': month,
            'Date': date,
            'Size': size}
    list_values.append(data)
    return list_values


def image_date_sort(source_path, dest_path):
    list_values = list()
    if not os.path.isdir(dest_path):
        os.mkdir(dest_path)
    else:
        pass


    for folderName, subFolders, fnames in os.walk(source_path):
        for fname in fnames:
            if fname.endswith('.png') | fname.endswith('.jpg') | fname.endswith('.jpeg') | fname.endswith('.bmp'):
                fpath = os.path.join(folderName, fname)
                print(fpath)
                mdate = datetime.date.fromtimestamp(os.path.getmtime(fpath))
                year = str(mdate)[:4]
                month = str(mdate)[5:7]
                date = str(mdate)[-2:]
                size = os.path.getsize(fpath)

                list_values = get_file_details(list_values = list_values, name=fname, year=year, month=month, date=date, size=size)
                # if os.path.isdir(dest_path + "/" + year):
                if os.path.isdir(dest_path + "/" + year + "-" + month):

                    # Duplicate handling
                    if not os.path.exists(dest_path + "/" + year + "-" + month + "/" + fname):
                        shutil.copy(os.path.join(folderName, fname), os.path.join(dest_path, year + "-" + month))
                    else:
                        try:
                            os.mkdir(dest_path + "/" + year + "-" + month + "/" + "__2__")
                        except:
                            shutil.copy(os.path.join(folderName, fname),dest_path + "/" + year + "-" + month + "/" + "__2__")
                else:
                    try:
                        os.mkdir(dest_path + "/" + year + "-" + month)
                        shutil.copy(os.path.join(folderName, fname), dest_path + "/" + year + "-" + month)
                    except:
                        continue

            else:
                continue
    return list_values


SOURCE_PATH = "/mnt/d/Pictures/Images"
DEST_PATH = "/mnt/d/Pictures/Experiment"


def main():

    list_values = image_date_sort(source_path= SOURCE_PATH, dest_path= DEST_PATH)
    df2 = pd.DataFrame(list_values, columns=['Filename', 'Year', 'Month', 'Date', 'Size'])
    df2.to_csv(r'\image-details.csv', index=None, header=True)


if __name__ == '__main__':
    main()

