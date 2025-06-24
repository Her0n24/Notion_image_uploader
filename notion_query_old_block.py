import requests
import time
from datetime import datetime, timedelta
import Tokens

def delete_old_blocks(page_id, notion_token, hour_limit= 23):
    # Calculate threshold
    threshold_time = (datetime.now() - timedelta(hours=hour_limit)).isoformat() + "Z"
    
    # Build request
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Notion-Version": "2022-06-28",
    }
    response = requests.get(url, headers=headers)
    blocks = response.json().get("results", [])

    # Step 2: Filter and delete old image/file blocks
    for block in blocks:
        block_type = block.get("type")
        created_time = block.get("created_time")
        block_id = block.get("id")

        # Only process image or file blocks
        if block_type in ["image", "file"]:
            # Compare created_time
            if created_time < threshold_time:
                # Step 3: Delete the block
                del_url = f"https://api.notion.com/v1/blocks/{block_id}"
                del_response = requests.delete(del_url, headers=headers)
                if del_response.status_code == 200:
                    print(f"Deleted {block_type} block: {block_id}")
                else:
                    print(f"Failed to delete block: {block_id}")
