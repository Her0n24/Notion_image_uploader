import requests
import json
import datetime
import Tokens
import notion_create_upload as ncu
import notion_upload_file as nuf
import notion_attach_block as nab
import notion_query_old_block as nqob

notion_token = Tokens.NOTION_KEY
page_id = Tokens.PAGE_ID

# Need better algorithm to get the run number

run = "00"
run = run.zfill(2)  # Ensure run is two digits
today = datetime.date.today() #- datetime.timedelta(days=1)
today_str = today.strftime("%Y%m%d")
yesterday = today - datetime.timedelta(days=1)
yesterday_str = yesterday.strftime("%Y%m%d")
city = "Reading"

# Delete old blocks of previous forecast before posting new ones
nqob.delete_old_blocks(Tokens.PAGE_ID, Tokens.NOTION_KEY)

file_name = f'/home/tsing/Documents/dev/Afterglow/output/{today_str}{run}0000_afterglow_dashboard_{city}.png'

file_upload_id = ncu.create_upload_and_get_id(notion_token)
print(f"File upload ID: {file_upload_id}")

nuf.upload_file_to_notion(file_name, notion_token, file_upload_id)

nab.append_image_to_block(page_id, file_upload_id, notion_token)

file_name = f'/home/tsing/Documents/dev/Afterglow/output/{today_str}{run}0000-18h-AIFS_cloud_cover_{city}.png'

file_upload_id = ncu.create_upload_and_get_id(notion_token)
print(f"File upload ID: {file_upload_id}")
nuf.upload_file_to_notion(file_name, notion_token, file_upload_id)

nab.append_image_to_block(page_id, file_upload_id, notion_token)


file_name = f'/home/tsing/Documents/dev/Afterglow/output/{today_str}{run}0000-42h-AIFS_cloud_cover_{city}.png'

file_upload_id = ncu.create_upload_and_get_id(notion_token)
print(f"File upload ID: {file_upload_id}")
nuf.upload_file_to_notion(file_name, notion_token, file_upload_id)

nab.append_image_to_block(page_id, file_upload_id, notion_token)