import requests
import shutil
import os


def readFile(path):
    data = None
    if not os.path.exists(path):
        return data
    with open(path) as f:
        data = f.readlines()
    return data


def parseData(data):
    if data is None:
        print "Unable to parse data"
        return None
    result = []
    for line in data:
        tmp = line.strip()
        if '.push("https://' not in tmp:
            continue
        id0 = tmp.find('"')
        id1 = tmp.find('"', id0 + 1)
        if id0 == -1 or id1 == -1:
            continue
        result.append(tmp[id0+1:id1])
    return result


def download(image_url, out_path):
    resp = requests.get(image_url, stream=True)
    resp.raw.decode_content = True
    local_file = open(out_path, "wb")
    shutil.copyfileobj(resp.raw, local_file)
    del resp


def main():
    filename = "data.txt"
    image_name = "page_%s.png"
    data = readFile(filename)
    paths = parseData(data)
    for i in range(len(paths)):
        download(paths[i], image_name % str(i))
    print "Done"


main()
