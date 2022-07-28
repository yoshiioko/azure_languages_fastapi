import requests as req
import config


def call_text_analytics_api(headers, document, endpoint):
    response = req.post(config.API_URL + endpoint, headers=headers, json=document)
    return response.json()
