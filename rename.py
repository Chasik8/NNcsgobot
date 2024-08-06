import os, glob


def main():
    dir = 'traning1'
    path = f'{dir}\images'
    kol = 0
    for filename in glob.glob(os.path.join(path, '*.jpg')):
        os.rename(f"{filename}", f"{path}\{str(kol)}.jpg")
        kol += 1
    path = f'{dir}\labels'
    kol = 0
    for filename in glob.glob(os.path.join(path, '*.txt')):
        os.rename(f"{filename}", f"{path}\{str(kol)}.txt")
        kol += 1
    # with open(os.path.join(os.getcwd(), filename), 'r') as f:
    #     f.rename


if __name__ == '__main__':
    main()
