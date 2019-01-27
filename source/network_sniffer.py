import webbrowser
import subprocess
import os
import re

def cmd(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = p.communicate()
    return output

def getData():
    lines = cmd(["arp", "-a"])
    lines = lines.replace("\n", "")
    l = []
    for line in lines.split("\r"):
        data = " ".join(line.split()).split(" ")
        if re.search("\\d+.\\d+.\\d+", data[0]):
            l.append(data)
    return l

def saveFile(filename, content):
    f = open(filename, "w")
    f.write(content)
    f.close()

def createHTML(data):
    html = "<html><head></head><body>"
    for d in data:
        html += "<p><a href='%s'>%s</a></p>" % (d[0], d[0])
    html += "</body></html>"
    return html

def main(chrome_path, html_path):
    saveFile(html_path, createHTML(getData()))
    webbrowser.get(chrome_path).open("file:///" + html_path)

if __name__ == "__main__":
    chrome_path = r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    html_path = os.getcwd() + "/" + "network_sniffer.html"
    main(chrome_path, html_path)
