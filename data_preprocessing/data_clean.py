import emoji
import os

def clean(file, dir):
    # initialize lists of things to exclude
    # nightbot commands
    nb = ['nightbot', '!commands', '!commercial', '!filters', '!permit', '!game', '!marker', '!poll', '!regulars',
          '!songs',
          '!tags', '!title', '!winner', '!gamble']
    # subscription and primes
    sp = ['gifted tier', 'subscribed tier', 'subscribed prime', 'gifting', 'subscribed']
    # other words to ignore
    ignore = ['http', 'tinyurl', '@']

    chats = []  # strings
    users = set()  # unique users

    get_file = open(os.path.join(dir, file), 'r')

    # remove bot messages, commands and links
    # Separate emojis from data
    # delete @ user
    for row in get_file.readlines():
        row = row[10:]  # ignore time
        x = row.split(':', 1)  # name, msg
        x[0] = x[0].strip('\n ')
        x[1] = x[1].strip('\n ')

        if len(x[1]) == 0:  # skip blank chats
            continue

        # nightbot
        if x[0] == 'Nightbot' or x[1][0] == '!':
            continue
        for cmd in nb:
            if x[1].lower().find(cmd) != -1:
                continue

        # subs, etc
        if (x[1].lower().find('gifted') != -1 or x[1].lower().find('subscribed') != -1 or x[1].lower().find(
                'gifting') != -1):
            continue

        users.add(x[0])

        old = x[1].split()
        new = []

        # remove ignored words, user mentions
        for w in old:
            for i in ignore:
                w = w.lower().replace(i, '')  # removes all occurrences
            for u in users:
                w = w.replace(u, '')  # remove user mentions
            w = ''.join(ch for ch in w if ch.isalnum() and not ch.isdigit())  # remove numbers, special characters
            if w != '':
                new.append(w.strip(' '))

        x[1] = ' '.join(new)

        x[1] = emoji.replace_emoji(x[1], replace='')

        if len(x[1].strip('\n ')) > 0:
            chats.append(x[1].strip(' '))

    # writing files
    file_name = 'clean-' + file
    with open(os.path.join(dir, file_name), 'w') as fp:
        for msg in chats:
            fp.write(msg + '\n')
        fp.close()

def main():
    src = './data/raw'
    dest = './data/clean'
    directory_files = os.listdir(src)
    for file in directory_files:
        if 'txt' in file:
            clean(file, dest)


if __name__ == '__main__':
    main()