#------download files from url
from pathlib import Path
import requests

DATA_PATH = Path("data")
PATH = DATA_PATH / "mnist"

PATH.mkdir(parents=True, exist_ok=True)

URL = "http://deeplearning.net/data/mnist/"
FILENAME = "mnist.pkl.gz"

if not (PATH / FILENAME).exists():
        content = requests.get(URL + FILENAME).content
        (PATH / FILENAME).open("wb").write(content)

#--------create file to automically install required packages
# pip install -r requirements.txt
# in requirements.txt
#         BeautifulSoup==3.2.0
#         Django==1.3
#         Fabric==1.2.0
#         Jinja2==2.5.5
#         PyYAML==3.09
#         Pygments==1.4
#         SQLAlchemy==0.7.1
#         South==0.7.3
#         amqplib==0.6.1
#         anyjson==0.3

