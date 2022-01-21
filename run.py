import glob
import os

def read_all_picture_files():
    return glob.glob(os.path.join("input", "*.jpg"))

def main():
    print("good")

if __name__ == "__main__":
    main()