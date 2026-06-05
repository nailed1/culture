import requests
import numpy as np
import fastapi

app = fastapi.FastAPI()
data = np.array([1, 2, 3])
http = requests.Session()
