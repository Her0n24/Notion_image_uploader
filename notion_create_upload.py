import json
import requests
from datetime import datetime, timezone
import Tokens
import logging
logging.basicConfig(
    level=logging.INFO,
    datefmt= '%Y-%m-%d %H:%M:%S',
                    )

notion_token = Tokens.NOTION_KEY

def create_upload_and_get_id(notion_token: str) -> str:
    """
    Create a file upload in Notion and return the file upload ID.
    :param notion_token: The Notion API token.
    :return: The file upload ID.
    
    This function creates a file upload in Notion and returns the ID of the created file upload.
    It uses the Notion API to create a file upload with a specified filename and content type
    (in this case, "image/png"). The response is saved to a file named "create_upload_output.json".
    If the request fails, an exception is raised with the status code and error message.
    """

    payload = {
        "filename": "latest_dashboard",
        "content_type": "image/png"
    }

    file_create_response = requests.post("https://api.notion.com/v1/file_uploads", json=payload, headers={
        "Authorization": f"Bearer {notion_token}",
        "accept": "application/json",
        "content-type": "application/json",
        "Notion-Version": "2022-06-28"
    })

    response_json = file_create_response.json()

    # Save response to a file
    with open("create_upload_output.json", "w") as f:
        json.dump(response_json, f, indent=4)


    if file_create_response.status_code != 200:
        logging.error(
            f"File creation failed with status code {file_create_response.status_code}: {file_create_response.text}"
        )
        raise Exception(
            f"File creation failed with status code {file_create_response.status_code}: {file_create_response.text}"
        )

    file_upload_id: str = json.loads(file_create_response.text)['id']

    return file_upload_id