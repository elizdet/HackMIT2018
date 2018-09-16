from flask import Flask, request, render_template
import requests
import os
import json
import time


app = Flask(__name__)

subscription_key = "ec897a8cde484a4f9571c53708dc472a"

def azure_api(img_url):
    uri_base = 'https://westus.api.cognitive.microsoft.com'
    # Request headers. header = json or octet-stream
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    # Request parameters.
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    #image_path = (os.path.expanduser("~/Desktop/scared.jpg"))
    #image_data = open(image_path, "rb").read()

    # Body. The URL of a JPEG image to analyze.
    body = {'url': img_url}


    try:
        print ("inside")
        # Execute the REST API call and get the response.
        # data when data, body when jsob
        response = requests.request('POST', uri_base + '/face/v1.0/detect', json = body, headers=headers,
                                    params=params)

        #print('Response: ', response)
        parsed = json.loads(response.text)
        emotions = parsed[0]['faceAttributes']['emotion']
        print("parsed: ", emotions)   
        return emotions

        #print (json.loads(response.text)['faceAttributes'])
        #print(json.dumps(parsed, sort_keys=True, indent=2))

    except Exception as e:
        print('Error:')
        print(e)




@app.route('/', methods=['POST'])
def index():
    results = azure_api(request.data)
    requests.post("http://localhost:8000", json=results)
    # Can do anything with request.data now 
    return render_template('index.html', results= "tstesults1")
                                                           


if __name__ == '__main__':
    #  azure_api()
    app.run()
