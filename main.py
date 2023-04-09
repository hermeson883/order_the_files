import os

def organize_folder():
    types = ['.zip', '.csv', '.pdf']

    base_path = os.path.expanduser('~')
    path = os.path.join(base_path, 'downloads'.capitalize())

    csw = os.chdir(path)

    full_list = os.listdir(csw)

    print(full_list)

    for type_ in types:
        if type_ not in os.listdir():
            os.mkdir(f'Files {type_}')

    for file in full_list:
        for type_ in types:
            if type_ in file:
                old_path = os.path.join(path, file)
                new_path = os.path.join(path, type_, file)
                os.replace(old_path, new_path)

if __name__ == '__main__':
    organize_folder()