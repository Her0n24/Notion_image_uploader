import requests
import json
import datetime
import Tokens

def upload_file_to_notion(file_name: str, notion_token: str, file_upload_id: str) -> None:
    """
    Upload a file to Notion using the file upload ID.
    :param file_name: The name of the file to upload.
    :param notion_token: The Notion API token.
    :param file_upload_id: The ID of the file upload created in Notion.
    :return: None
    """

    with open(file_name, "rb") as f:
            # Provide the MIME content type of the file as the 3rd argument.
        files = {
            "file": (file_name, f, "image/png")
        }

        response = requests.post(
            f"https://api.notion.com/v1/file_uploads/{file_upload_id}/send",
            headers={
                "Authorization": f"Bearer {notion_token}",
                "Notion-Version": "2022-06-28"
            },
            files=files
        )
        
        response_json = response.json()

        # Save response to a file
        with open("file_upload_output.json", "w") as f:
            json.dump(response_json, f, indent=4)

        if response.status_code != 200:
            raise Exception(
                f"File upload failed with status code {response.status_code}: {response.text}")
