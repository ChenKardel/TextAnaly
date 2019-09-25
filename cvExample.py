
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
subscription_key = "cced4caa372c41deac94a069a20212f2"
endpoint = "https://kardel2.cognitiveservices.azure.com/"

credentials = CognitiveServicesCredentials(subscription_key)
text_analytics = TextAnalyticsClient(endpoint=endpoint, credentials=credentials)
documents = [
    {
        "id": "1",
        "language": "en",
        "text": "@Breaking911 Build that wall!! 👍"
    }
]
response = text_analytics.entities(documents=documents)

for document in response.documents:
    print("Document Id: ", document.id)
    print("\tKey Entities:")
    for entity in document.entities:
        print("\t\t", "NAME: ", entity.name, "\tType: ",
              entity.type, "\tSub-type: ", entity.sub_type)
        for match in entity.matches:
            print("\t\t\tOffset: ", match.offset, "\tLength: ", match.length, "\tScore: ",
                  "{:.2f}".format(match.entity_type_score))
