import json

def main():
    text_fptr = open('news.txt', 'r').read()
    sub_fptr = open('subs.json', 'r')
    subs = json.load(sub_fptr)
    print(subs, type(subs))


    for i in text:
        text_fptr+text_fptr.replace(subs[i]["old"], subs[i]["new"])
main()