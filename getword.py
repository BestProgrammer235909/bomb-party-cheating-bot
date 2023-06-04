def getword(s, used, alphabet):
    words_file_path = r"C:\Users\jorda\PycharmProjects\BombPartyBot\images\dict.txt"
    with open(words_file_path, 'r') as file:
        words = [line.strip() for line in file]
    words = sorted(words, key=len)
    for i in words:
        if s.lower() in i.lower():
            used.append(i)
            return [i, set(alphabet + list(i))]
