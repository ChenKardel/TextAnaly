from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import os
import data
def step1():
    subscription_key = "cced4caa372c41deac94a069a20212f2"
    endpoint = "https://kardel2.cognitiveservices.azure.com/"
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics = TextAnalyticsClient(endpoint=endpoint, credentials=credentials)
    documents = data.contents2docs(data.get_contents(filename="eng_summary1.txt"))
    response = text_analytics.sentiment(documents=documents)
    f = open(os.path.join(data.ROOT_DIR, "score.txt"), 'w')
    for document in response.documents:
        print("Document Id: ", document.id, ", Sentiment Score: ",
              "{:.2f}".format(document.score), file=f)

    f.close()

def step2():
    fscore = open(os.path.join(data.ROOT_DIR, "score.txt"), 'r')
    fcontent = open(os.path.join(data.ROOT_DIR, "eng_summary1.txt"), 'r')
    fyygq = open(os.path.join(data.ROOT_DIR, "yygq.txt"), 'w')
    finsult = open(os.path.join(data.ROOT_DIR, "insult.txt"), 'w')
    for scoreLine, content in zip(fscore, fcontent):
        score = float(scoreLine.split(" ")[-1])
        if score > 0.5:
            print(content, "score="+str(score), file=fyygq)
        else:
            print(content, "score="+str(score), file=finsult)

    fscore.close()
    fcontent.close()
    fyygq.close()
    finsult.close()

if __name__ == '__main__':
    step2()