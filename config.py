from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Base directories
RAW_DATA_PATH = Path(os.getenv("RAW_DATA_PATH"))
PROCESSED_DATA_PATH = Path(os.getenv("PROCESSED_DATA_PATH"))


# Raw data files
raw_files = {
    "fire_dz": RAW_DATA_PATH / os.getenv("FIRE_DZ"),
    "fire_tn": RAW_DATA_PATH / os.getenv("FIRE_TN"),
    "landcover_dz": RAW_DATA_PATH / os.getenv("LANDCOVER_DZ"),
    "landcover_tn": RAW_DATA_PATH / os.getenv("LANDCOVER_TN"),
    "landcover_legend": RAW_DATA_PATH / os.getenv("LANDCOVER_LEGEND_RAW"),
    "climate_prec": RAW_DATA_PATH / os.getenv("CLIMATE_PREC"),
    "climate_tmax": RAW_DATA_PATH / os.getenv("CLIMATE_TMAX"),
    "climate_tmin": RAW_DATA_PATH / os.getenv("CLIMATE_TMIN"),
    "elevation": RAW_DATA_PATH / os.getenv("ELEVATION"),
    "dz_boundaries": RAW_DATA_PATH / os.getenv("DZ_BOUNDARIES"),
    "tn_boundaries": RAW_DATA_PATH / os.getenv("TN_BOUNDARIES"),
    "soil_bil": RAW_DATA_PATH / os.getenv("SOIL_BIL"),
    "soil_csv": RAW_DATA_PATH / os.getenv("SOIL_CSV"),
}

# Processed data files
processed_files = {
    "fire": PROCESSED_DATA_PATH / os.getenv("FIRE_PROCESSED"),
    "landcover": PROCESSED_DATA_PATH / os.getenv("LANDCOVER_PROCESSED"),
    "landcover_legend": PROCESSED_DATA_PATH / os.getenv("LANDCOVER_LEGEND_PROCESSED"),
    "climate": PROCESSED_DATA_PATH / os.getenv("CLIMATE_PROCESSED"),
    "elevation": PROCESSED_DATA_PATH / os.getenv("ELEVATION_PROCESSED"),
    "soil_raster": PROCESSED_DATA_PATH / os.getenv("SOIL_NC_PROCESSED"),
    "soil_att": PROCESSED_DATA_PATH / os.getenv("SOIL_ATT_PROCESSED"),
    "soil_nc": PROCESSED_DATA_PATH / os.getenv("SOIL_NC_PROCESSED"),
}
