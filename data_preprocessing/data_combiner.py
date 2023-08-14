import os

# combine files
def combine(src, dest):
  data = ""
  directory_files = os.listdir(src)
  for file in directory_files:
    if 'txt' not in file:
        continue
    get_file = open(os.path.join(src, file),'r')
    data += get_file.read() + "\n"

  # writing file
  file_name = 'chat.txt'
  with open (os.path.join(dest, file_name), 'w') as fp:
    fp.write(data)
    fp.close()

# main method to execute code
def main():
    src = './data/clean'
    dest = './data/combined'
    combine(src, dest)


if __name__ == '__main__':
    main()