import json
from flask import Flask, request
from settings import api_version
from pipelines import used_vocabulary

app = Flask(__name__)


@app.route("/api/{}/get-dictionary-from-src".format(api_version), methods=['POST'])
def get_dictionary_from_src():
    src = json.loads(request.data)["src"]
    # TODO: SET CONTENT-TYPE
    return json.dumps({
        "data": {"src": src, "dictionary": [{"dictionaryWord": k[0],
                                             "partOfSpeechTag": k[1],
                                             "entriesInSrc": [{"start": entry[0], "end":
                                                 entry[0]+entry[1]} for entry in v]
                                             } for k, v in used_vocabulary(src).items()]},
        "error": None,
        "meta": {"languages": ["en"]}
        })


if __name__ == "__main__":
    app.run()

