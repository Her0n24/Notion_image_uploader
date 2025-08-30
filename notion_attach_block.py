import json
import requests
import Tokens
import logging
logging.basicConfig(
    level=logging.INFO,
    datefmt= '%Y-%m-%d %H:%M:%S',
                    )

## Append image to desired block (this could be a page,
# or a block within a page)

def append_image_to_block(append_block_id: str, file_upload_id: str, Notion_key: str) -> None:
    """
    Append an image to a Notion block using the file upload ID.
    :return: None
    """

    url = f"https://api.notion.com/v1/blocks/{append_block_id}/children"

    payload = {
        "children": [
            {
                "object": "block",
                "type": "image",
                "image": {
                    "type": "file_upload",
                    "file_upload": {
                        "id": file_upload_id
                    }
                }
            }
        ]
    }

    response = requests.patch(url, headers={
        "Authorization": f"Bearer {Notion_key}",
        "accept": "application/json",
        "content-type": "application/json",
        "Notion-Version": "2022-06-28"
    }, data=json.dumps(payload))

    response_json = response.json()

    with open("attach_bloc_output.json", "w") as f:
        json.dump(response_json, f, indent=4)

    if response.status_code != 200:
        logging.error(
            f"Block append failed with status code {response.status_code}: {response.text}"
        )
        raise Exception(
            f"Block append failed with status code {response.status_code}: {response.text}")