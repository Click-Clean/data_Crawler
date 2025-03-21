import json
import boto3

def make_json (title, body, url, author, media, created_at, category, image_url) :

    data = {
        "title" : title,
        "body" : body,
        "media" : media,
        "author" : author,
        "url" : url,
        "category" : category,
        "created_at" : created_at,
        "image_url" : image_url
        }

    # send_to_sqs(data)

    save_as_json(data)
    

def send_to_sqs (data) :

    # have to set !!
    queue_url = "" 
    
    sqs = boto3.client("sqs", region_name = "us-east-1")

    try :
        response = sqs.send_message(
            QueueUrl = queue_url,
            MessageBody = json.dumps(data, ensure_ascii = False),
            MessageGroupId = "default-group"
        )

    except Exception as e :
        print(f"Failed to send message to SQS : {e}")


def save_as_json (data) : 

    base_path = "../sample/"
    extension = ".json"

    filename = data["url"].split("article/")[1].replace("/", "_")[:14]

    with open(base_path + filename + extension, "w", encoding = "utf-8") as file :
        json.dump(data, file, indent = 4, ensure_ascii = False)
    
    
