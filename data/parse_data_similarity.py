# Python
import requests
import json
import os
# Data Processing Tools
import numpy as np
from numpy import dot
from numpy.linalg import norm


# Variables
NODE_ENV = os.environ.get("NODE_ENV", "develop")
API_URL = 'http://52.78.81.59:8000/cluster/' if NODE_ENV == "production" else 'http://localhost:8000/cluster/'
headers = {'content-type': 'application/json'}
