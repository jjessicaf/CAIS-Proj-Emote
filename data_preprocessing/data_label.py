import csv
import os.path

# label chats for 10 lines
# output as csv with chat and corresponding label
def label(src, dest, dest_name, lines, Dict, labels):
    with open(os.path.join(dest, dest_name), 'w') as file:
        # initialize labels in output file
        l = [item for item in range(1, 61)]
        fieldnames = ['chats']
        fieldnames += l
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        # open source as readable
        with open(os.path.abspath(src), 'r') as fp:
            rl = fp.readlines()
            count = len(rl)

            window = []
            emotes = []
            mode = ''
            for i in range(0, lines):
                temp = ''
                curr_line = rl[i].split()
                for word in curr_line:
                    if word.strip() in Dict:
                        temp += word + ' '
                        Dict[word] += 1
                        if (mode == '') or (Dict[mode] < Dict[word]):
                            mode = word
                window.append(rl[i].strip())
                emotes.append(temp)

            if mode != '':
                row = {}
                row['chats'] = rl[lines - 1].strip('\n')
                for k in labels:
                    if mode != k:
                        row[labels[k]] = 0
                    else:
                        row[labels[k]] = 1

                writer.writerow(row)

            for j in range(lines, count):
                # update window, delete first item
                for e in emotes[0].split():
                    if e != '' and Dict[e] > 0:
                        Dict[e] -= 1

                # reset
                del window[0]
                del emotes[0]
                if mode != '' and Dict[mode] == 0:
                    mode = ''
                temp = ''

                curr_line = rl[j].split()
                for word in curr_line:
                    if word.strip() in Dict:
                        temp += word + ' '
                        Dict[word] += 1
                        if (mode == '') or (Dict[mode] < Dict[word]):
                            mode = word

                window.append(rl[j].strip())
                emotes.append(temp)

                if mode == '': # if there was no emote
                    continue

                row = {}
                row['chats'] = rl[j].strip('\n')
                for k in labels:
                    if mode != k:
                        row[labels[k]] = 0
                    else:
                        row[labels[k]] = 1
                writer.writerow(row)

        fp.close()

# main method to execute code
def main():
    Dict = {'Joebart5head': 0, 'joebartAlpha': 0, 'joebartAlvin': 0, 'joebartArf': 0, 'joebartBusiness': 0,
            'joebartCam': 0, 'joebartClown': 0,
            'joebartCrimsonChin': 0, 'joebartDoofed': 0, 'joebartExcited': 0, 'joebartEZ': 0, 'joebartFeelsBad': 0,
            'joebartFreddy': 0, 'joebartHappy': 0, 'joebartHesChoking': 0,
            'joebartHuh': 0, 'joebartKekw': 0, 'joebartLonghead': 0, 'joebartLongneck': 0, 'joebartLove': 0,
            'joebartMald': 0, 'joebartMan': 0, 'joebartMonka': 0, 'joebartNinja': 0,
            'joebartOof': 0, 'joebartPain': 0, 'joebartPepega': 0, 'joebartPepehands': 0, 'joebartPog': 0,
            'joebartPogu': 0, 'joebartPumpkinHead': 0, 'joebartPumpkinJoe': 0,
            'joebartSad': 0, 'joebartSimon': 0, 'joebartSquidward': 0, 'joebartTheodore': 0, 'joebartThinking': 0,
            'joebartWeBelieve': 0, 'joebartWeirdchamp': 0, 'joebartWhat': 0,
            'joebartWide': 0, 'joebartZooted': 0, 'HeyGuys': 0, 'Kappa': 0, 'LUL': 0, 'PogChamp': 0, 'VoHiYo': 0,
            'NotLikeThis': 0, '<3': 0, 'BibleThump': 0, 'WutFace': 0, 'ResidentSleeper': 0,
            'Kreygasm': 0, 'SeemsGood': 0, 'catJAM': 0, 'HYPERCATJAM': 0, 'KappaPride': 0, 'PogBones': 0,
            'PartyPopper': 0, 'DoritosChip': 0}

    labels = {'Joebart5head': 1, 'joebartAlpha': 2, 'joebartAlvin': 3, 'joebartArf': 4, 'joebartBusiness': 5,
              'joebartCam': 6, 'joebartClown': 7,
              'joebartCrimsonChin': 8, 'joebartDoofed': 9, 'joebartExcited': 10, 'joebartEZ': 11, 'joebartFeelsBad': 12,
              'joebartFreddy': 13, 'joebartHappy': 14, 'joebartHesChoking': 15,
              'joebartHuh': 16, 'joebartKekw': 17, 'joebartLonghead': 18, 'joebartLongneck': 19, 'joebartLove': 20,
              'joebartMald': 21, 'joebartMan': 22, 'joebartMonka': 23, 'joebartNinja': 24,
              'joebartOof': 25, 'joebartPain': 26, 'joebartPepega': 27, 'joebartPepehands': 28, 'joebartPog': 29,
              'joebartPogu': 30, 'joebartPumpkinHead': 31, 'joebartPumpkinJoe': 32,
              'joebartSad': 33, 'joebartSimon': 34, 'joebartSquidward': 35, 'joebartTheodore': 36,
              'joebartThinking': 37, 'joebartWeBelieve': 38, 'joebartWeirdchamp': 39, 'joebartWhat': 40,
              'joebartWide': 41, 'joebartZooted': 42, 'HeyGuys': 43, 'Kappa': 44, 'LUL': 45, 'PogChamp': 46,
              'VoHiYo': 47, 'NotLikeThis': 48, '<3': 49, 'BibleThump': 50, 'WutFace': 51, 'ResidentSleeper': 52,
              'Kreygasm': 53, 'SeemsGood': 54, 'catJAM': 55, 'HYPERCATJAM': 56, 'KappaPride': 57, 'PogBones': 58,
              'PartyPopper': 59, 'DoritosChip': 60}

    dictlow = dict((k.lower(), v) for k, v in Dict.items())
    labels = dict((k.lower(), v) for k, v in labels.items())
    lines = 10

    # source and destination
    src = './data/combined/chat.txt'
    dest = './data/labeled'

    label(src, dest, 'output.csv', lines, dictlow, labels)


if __name__ == '__main__':
    main()