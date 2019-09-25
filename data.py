from typing import Union

import pandas as pd
import os

# pd.read_csv

ROOT_DIR = "/media/kardel/Ubuntu 17.0/russian-troll-tweets-master"

from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials


def get_text_analytics():
    subscription_key = "cced4caa372c41deac94a069a20212f2"
    endpoint = "https://kardel2.cognitiveservices.azure.com/"
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics = TextAnalyticsClient(endpoint=endpoint, credentials=credentials)
    return text_analytics


def save_content(filename: Union[list, str], dirname=ROOT_DIR):
    all_dirs = os.listdir(dirname)
    data = [os.path.join(dirname, _dir) for _dir in all_dirs if _dir.endswith(".csv")]
    if type(filename) == str:
        s = open(os.path.join(dirname, filename), 'w')
        for datum in data:
            df = pd.read_csv(datum)
            lines = df["content"].values
            for line in lines:
                # print(line)
                if type(line) == str:
                    s.write(line + "\n")

                else:
                    print(line)
        s.close()
    elif type(filename) == list and len(filename) == len(data):
        for fn, datum in zip(filename, data):
            s = open(os.path.join(dirname, fn), 'w')

            df = pd.read_csv(datum)
            lines = df["content"].values
            for line in lines:
                # print(line)
                if type(line) == str:
                    s.write(line + "\n")

                else:
                    print(line)
            s.close()


def get_contents(dirname=ROOT_DIR, filename="summary.txt", start_line=None, end_line=None):
    f = open(os.path.join(dirname, filename), 'r')
    # print("start_line: " + str(start_line) + "end_line:" + str(end_line))
    if start_line is None and end_line is None:
        lines = f.readlines()
    elif start_line is not None and end_line is None:
        for _ in range(start_line):
            f.readline()
        lines = f.readlines()
    elif start_line is not None and end_line is not None:
        print("go")
        lines = []
        for _ in range(start_line):
            f.readline()
        for _ in range(start_line, end_line):
            line = f.readline()
            lines.append(line)
    f.close()
    return [line.strip() for line in lines]


def contents2docs(contents, lang="en"):
    return [{"id": str(i + 1), "language": lang, "text": content} for i, content in enumerate(contents)]


def do_sth_line_by_line(func, dirname=ROOT_DIR, filename="summary.txt"):
    f = open(os.path.join(dirname, filename), 'r')
    line = f.readline()
    while line is not None:
        func(line)
    f.close()


def get_eng_line(x):
    lines = []
    text_analytics = get_text_analytics()
    if type(x) == str:
        documents = [
            {
                'id': '1',
                'text': x
            }]
    elif type(x) == list:
        i = 1
        documents = []
        for x_ in x:
            documents.append({
                'id': str(i),
                'text': x_
            })
            i += 1
    response = text_analytics.detect_language(documents=documents)
    for i, document in enumerate(response.documents):
        lang = document.detected_languages
        print(lang)
        if len(lang) == 1 and lang[0].name == "English":
            lines.append(documents[i]["text"])
    return lines


if __name__ == '__main__':
    save_content(["summary" + str(i) + ".txt".format(i) for i in range(1, 14)])
    with open(os.path.join(ROOT_DIR, "eng_summary1.txt"), 'w') as f:
        for batch in range(1):
            lines = get_contents(filename="summary1.txt", start_line=1, end_line=(batch + 1) * 1000 + 1)
            print(len(lines))
            print(lines)
            elines = get_eng_line(lines)
            print(len(elines))
            for eline in elines:
                f.write(eline + '\n')
        f.close()
    text_analytics = get_text_analytics()
    documents = [{"id": "1",
                  "text": "Один полицейский погиб и двое ранены в результате стрельбы в Колорадо. https://t.co/4ofRePjPJZ"},
                 {"id": "2",
                  "text": "The very first law in advertising is to avoid the concrete promise and cultivate the delightfully vague."}]
    response = text_analytics.detect_language(documents=documents)
    for document in response.documents:
        lang = document.detected_languages
        print(lang)
        if len(lang) == 1:
            print(lang[0].name)
