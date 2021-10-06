# Import dependencies and APIs

import pandas as pd
import numpy as np
import requests
import json
from us import zipcode # look this up, probably wrong
from config import censuskey
censuskey

census_url=f"api.census.gov/data/{year}/pep/population?get=COUNTY,DATE_CODE,DATE_DESC,DENSITY,POP,NAME,STATE&for=region:*&key={censuskey}"

census_url

