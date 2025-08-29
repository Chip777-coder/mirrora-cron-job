
from flask import Flask, request
from connector import log_to_notion

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def github_webhook():
    payload = request.get_json()
    repo = payload.get("repository", {}).get("name")
    event_type = request.headers.get("X-GitHub-Event")
    content = str(payload)

    if repo:
        log_to_notion(repo, event_type, content)

    return "", 200
