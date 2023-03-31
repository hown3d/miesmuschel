import http.client
import json
from urllib import parse

DEFAULT_HEADERS = {'Content-type': 'application/json'}


class MessageService:
    def __init__(self, chatter_url: str, timeout: float = 100):
        parts = parse.urlparse(chatter_url)
        self.port = parts.port
        self.hostname = parts.hostname
        self.timeout = timeout

    def get(self, message: str) -> str:
        conn = http.client.HTTPConnection(host=self.hostname, port=self.port, timeout=self.timeout)
        body = {
            "message": message
        }
        body_json = json.dumps(body)
        conn.request("GET", "/chatter/message", body=body_json)
        resp = conn.getresponse()
        resp_body = resp.read().decode()
        return resp_body
