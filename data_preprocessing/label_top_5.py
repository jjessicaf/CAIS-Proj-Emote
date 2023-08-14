import csv
import os
import pandas as pd


# labels just the top 5 most used emotes
# since the other labels had very few lines of support,
# limiting to top 5 emotes for clearer results
def label_top_5(df, dest, dest_name, Dict, labels):
  with open(os.path.join(dest, dest_name), 'w') as file:
    l = [item for item in range(1, 6)]
    fieldnames = ['chats']
    fieldnames += l
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for index, row in df.iterrows():
      for key in Dict:
        if (row[Dict[key]] == 1):
          r = {}
          r['chats'] = row['chats'].strip('\n')
          for k in labels:
            if (key != k):
              r[labels[k]] = 0
            else:
              r[labels[k]] = 1
          writer.writerow(r)

# main method to execute code
def main():
    Dict = {'joebartBusiness': 5, 'joebartLongneck': 19, 'joebartWeBelieve': 38, 'LUL': 45, 'catJAM': 55}
    labels = {'joebartBusiness': 1, 'joebartLongneck': 2, 'joebartWeBelieve': 3, 'LUL': 4, 'catJAM': 5}
    Dictlow = dict((k.lower(), v) for k, v in Dict.items())
    labels = dict((k.lower(), v) for k, v in labels.items())

    src = 'output.csv'
    path = './data/labeled'
    file_path = os.path.join(path, src)

    df = pd.read_csv(file_path)
    df.dropna(inplace=True) # drop blank rows

    label_top_5(df, path, 'train5.csv', Dictlow, labels)


if __name__ == '__main__':
    main()