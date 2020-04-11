import email
import html2text
import argparse
import json
import datetime


class Emlx(object):
    """An apple proprietary emlx message"""

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
        with open(self.filename, "r") as f:
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


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Parser for emlx mail files')
    parser.add_argument('file', nargs='+',
                        help='Emlx mail file')
    parser.add_argument('--html', help="Get html content", action="store_true", default=False)
    parser.add_argument('--txt', help="Get txt content", action="store_true", default=False)
    parser.add_argument('--html2txt', help="Get html content in text format", action="store_true", default=False)
    parser.add_argument('--json', help="Get all in json", action="store_true", default=False)
    parser.add_argument('--head', help="Get head summary", action="store_true", default=False)

    args = parser.parse_args()
    if args.file:
        msg = Emlx()
        msg.filename = args.file[0]
        message = msg.parse()

        if args.html: print(msg.get_html())
        if args.txt: print(msg.get_txt())
        if args.html2txt: print(msg.get_html2txt())
        if args.json: print(msg.json())
        if args.head: print(msg.print_header())

        if args.html or args.txt or args.html2txt or args.json or args.head:
            pass
        else:
            msg.print_header()
            msg.print_txt()
            msg.print_html()
            msg.print_html2txt()

    else:
        parser.print_help()
