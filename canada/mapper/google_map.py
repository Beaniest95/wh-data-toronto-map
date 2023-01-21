# %%
import glob
import googlemaps
import json
import pandas as pd
from loguru import logger
from typing import Dict, List, Any, Tuple

def to_json(file_path, enriched_path_suffix, file_name, file_format, data):
    save_path = f"{file_path}/{enriched_path_suffix}/{file_name}.{file_format}"
    logger.info(f"file path : {file_path}/{enriched_path_suffix}/{file_name}.{file_format}")
    with open(save_path, "w") as f:
        file = json.dumps(data, indent=4)
        f.write(file)

def enrich_data(gm_client, data) -> List[Dict[str, Any]]:
    result = []
    for row in data:
        enriched_row = row
        lat, lng = None, None
        geocode_info = None
        if row.get('url') != None:
            lat = float(row['url'].split('!')[5].split('3d')[-1])
            lng = float(row['url'].split('!')[6].split('4d')[-1])
        elif row.get('address') != None:
            try:
                geocode_info = gm_client.geocode('Toronto ' + row['address'])
                lat = geocode_info[0]['geometry']['location']['lat']
                lng = geocode_info[0]['geometry']['location']['lng']
            except Exception as e:
                logger.info(str(e))
                logger.info(row['address'])
                logger.info(f"geocode info: {geocode_info}")
        else:
            lat, lng = None, None

        enriched_row['lat'] = lat
        enriched_row['lng'] = lng
        result.append(enriched_row)

    return result

def google_map_mapper(google_variable):
    api_key=google_variable.api_key
    file_path=google_variable.file_path
    raw_path_suffix=google_variable.raw_path_suffix
    enriched_path_suffix=google_variable.enriched_path_suffix
    file_format=google_variable.file_format

    gm_client=googlemaps.Client(key=api_key)
    logger.info("Start Processing")

    for json_file_path in glob.glob(f"{file_path}/{raw_path_suffix}/*.{file_format}"):
        file_name = json_file_path.split(raw_path_suffix+'/')[-1].split(f'.{file_format}')[0]
        logger.info(f"ETL Process: {file_name}")
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            enriched_data = enrich_data(gm_client, data)
            to_json(file_path, enriched_path_suffix, file_name, file_format, enriched_data)
