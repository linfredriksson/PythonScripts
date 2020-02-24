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
        return None
    result = {
        "title": "",
        "issue": "",
        "paths": []}
    for line in data:
        tmp = line.strip()
        if '<a href="/Comic/' in tmp and '?id=' in tmp:
            title, issue = tmp.replace('<a href="/Comic/', "").split('/')
            issue = issue.split('?id=')[0]
            title = title.replace("-", "_")
            issue = issue.replace("-", "_")
            title = title.lower()
            issue = issue.lower()
            result["title"] = title
            result["issue"] = issue
        if '.push("https://' not in tmp:
            continue
        id0 = tmp.find('"')
        id1 = tmp.find('"', id0 + 1)
        if id0 == -1 or id1 == -1:
            continue
        result["paths"].append(tmp[id0+1:id1])
    return result


def download(image_url, out_path):
    resp = requests.get(image_url, stream=True)
    resp.raw.decode_content = True
    local_file = open(out_path, "wb")
    shutil.copyfileobj(resp.raw, local_file)
    del resp


def main():
    filename = "data.txt"
    data = parseData(readFile(filename))
    if data is None:
        print("Unable to parse data")
        return
    directory = os.path.join(data["title"], data["issue"])
    print("Title: %s" % data["title"])
    print("Issue: %s" % data["issue"])
    print("Creating directory: %s" % directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(len(data["paths"])):
        print("Downloading image %i/%i" % (i + 1, len(data["paths"])))
        tmp_path = os.path.join(directory, "page_%s.png" % str(i))
        if os.path.exists(tmp_path):
            print("Image already exists, skipping")
            continue
        download(data["paths"][i], tmp_path)
    print("Done")


main()
