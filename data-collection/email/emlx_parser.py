import email
import html2text
import argparse
import json
import datetime
import glob, os
import re
import pandas as pd
import shutil

class Emlx(object):
    def __init__(self):
        super(Emlx, self).__init__()
        self.filename = None
        self.bytecount = 0
        self.email = None
        self.txt = None
        self.html = None
        self.html2txt = None

    def __str__(self):
        return "Emlx Mail : %s " % (self.filename)

    def parse(self):
        """return the data structure for the current emlx file
        * an email object
        * the plist structure as a dict data structure
        """
        with open(self.filename, "r", errors='ignore') as f:
            # extract the bytecount
            content = f.readlines()

        if content:
            t = open(self.filename, "rb")
            self.bytecount = int(t.readline().strip())
            # parse du mail
            self.email = email.message_from_bytes(t.read(self.bytecount))

        for part in self.email.walk():
            if part.get_content_type() == 'text/plain':
                self.txt = part.get_payload()

            elif part.get_content_type() == "text/html":
                self.html = part.get_payload()
                self.html2txt = html2text.html2text(part.get_payload())

        return self.email

    # ---------------------------------------------- GET

    def get_txt(self):
        return self.txt

    def get_html(self):
        return self.html

    def get_html2txt(self):
        return self.html2txt

    # -------------------------------------------------- Print
    def print_header(self):
        print("From : " + self.email["From"])
        print("To : " + self.email["To"])
        print("Subject : " + self.email["Subject"])
        print("Date : " + self.email["Date"])

    def print_txt(self):
        print("--------- TXT ---------")
        print(self.txt)
        print("-----------------------")

    def print_html2txt(self):
        print("----- HTML 2 TEXT -----")
        print(self.html2txt)
        print("-----------------------")

    def print_html(self):
        print("----- HTML 2 TEXT -----")
        print(self.html)
        print("-----------------------")

    # -------------------------------------------------- Json

    def json(self):
        clean = {}
        clean["filename"] = self.filename
        clean["From"] = self.email["From"]
        clean["To"] = self.email["To"]
        clean["Subject"] = self.email["Subject"]
        clean["Date"] = str(datetime.datetime.strptime(self.email["Date"], "%a, %d %b %Y %H:%M:%S %z"))
        clean["txt"] = self.txt
        clean["html"] = self.html
        clean["html2txt"] = self.html2txt
        return json.dumps(clean)

# path for the data file
os.chdir("/Users/rachelzheng/Documents/GitHub/savvy-sue/data/okdata")

# brand - new dict
#brand = ["Men's Wearhouse", "American Eagle", "L.L.Bean", "Express", "DICK's" "Hillister"]
brand = {}

# look for all files ending with "emlx" extension
for file in glob.glob("*.emlx"):
    print(file)
    msg = Emlx()
    msg.filename = file
    message = msg.parse()
    #txt_info = msg.get_txt()
    info = msg.get_html()
    title_data = re.search('<title>(.*)</title>', info)
    title = title_data.group(1)
    print(title)
    if title not in brand.keys():
        brand[title] = 1
    else:
        brand[title] += 1
    print("finish")
    #file_orginal_path = "/Users/rachelzheng/Documents/GitHub/savvy-sue/data/" + str(file)
    #file_new_path = "/Users/rachelzheng/Documents/GitHub/savvy-sue/data/okdata/" + str(file)
    #shutil.move(file_orginal_path, file_new_path)

    # look for store information
    #if not any(x in txt_info for x in brand):
    #    print("not found")
        #print(msg.get_txt())
    #    break

print(brand)
#print("final result")

brand = pd.DataFrame(brand.items())
brand.to_excel("brand.xlsx", index=None)