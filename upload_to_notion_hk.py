import requests
import json
import datetime
import Tokens
import notion_create_upload as ncu
import notion_upload_file as nuf
import notion_attach_block as nab
import notion_query_old_block as nqob
import logging
logging.basicConfig(
    level=logging.INFO,
    datefmt= '%Y-%m-%d %H:%M:%S',
                    )
import os

notion_token = Tokens.NOTION_KEY
page_id = Tokens.PAGE_ID

import argparse
def parse_args():
    parser = argparse.ArgumentParser(description="Notion Upload HK")
    parser.add_argument('--date', type=str, default=None,
                        help="Specify the date in YYYYMMDD format (default: today)")
    return parser.parse_args()

args = parse_args()

if args.date:
    today = datetime.datetime.strptime(args.date, "%Y%m%d").date()
else:
    today = datetime.date.today()

# Need better algorithm to get the run number

run = "12"
# today = datetime.date.today() #- datetime.timedelta(days=1)
today_str = today.strftime("%Y%m%d")
yesterday = today - datetime.timedelta(days=1)
yesterday_str = yesterday.strftime("%Y%m%d")
city = "HongKong"

# Delete old blocks of previous forecast before posting new ones
nqob.delete_old_blocks(Tokens.PAGE_ID, Tokens.NOTION_KEY)

# Posting new forecast to the page
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Afterglow', 'output'))
file_name = os.path.join(output_dir, f"{today_str}{run}0000_afterglow_dashboard_{city}_hk.png")

file_upload_id = ncu.create_upload_and_get_id(notion_token)
logging.info(f"File upload ID: {file_upload_id}")
nuf.upload_file_to_notion(file_name, notion_token, file_upload_id)

nab.append_image_to_block(page_id, file_upload_id, notion_token)

file_name = os.path.join(output_dir, f"{today_str}{run}0000-24h-AIFS_cloud_cover_{city}_hk.png")

file_upload_id = ncu.create_upload_and_get_id(notion_token)
logging.info(f"File upload ID: {file_upload_id}")

nuf.upload_file_to_notion(file_name, notion_token, file_upload_id)

nab.append_image_to_block(page_id, file_upload_id, notion_token)

file_name = os.path.join(output_dir, f"{today_str}{run}0000-48h-AIFS_cloud_cover_{city}_hk.png")

file_upload_id = ncu.create_upload_and_get_id(notion_token)
logging.info(f"File upload ID: {file_upload_id}")

nuf.upload_file_to_notion(file_name, notion_token, file_upload_id)

nab.append_image_to_block(page_id, file_upload_id, notion_token)