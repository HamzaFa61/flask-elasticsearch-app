# Flask App with Elasticsearch Docker Image

This Flask app uses Elasticsearch 7.17.9 Docker image to enable search and auto-suggest features using a news JSON dataset obtained from Kaggle. This app is written in Python version 3.11.1.

## Requirements
- Docker
- Python 3.11.1 or higher

## Installation
1. Clone this repository to your local machine
```bash
git clone https://github.com/HamzaFa61/flask-elasticsearch-app.git
```
2. Open the terminal and navigate to the directory where you cloned this repository
```bash
cd flask-elasticsearch-app
```
3. Start the Elasticsearch Docker container:
```bash
start elasticsearch: sudo docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:7.17.9
```
4. Install the required Python packages:
```bash
pip install -r requirements.txt
```
## Usage
1. Start the flask app:
```bash
flask run
```
2. Open your browser and go to http://localhost:5000 to view the app
3. Type in a search query into the search box to retrieve relevant news articles.
4. As you type, the auto-suggest feature will show a dropdown of suggested search terms.

## Credits
This app was developed using the news JSON dataset from Kaggle (https://www.kaggle.com/datasets/rmisra/news-category-dataset). Special thanks to the Elasticsearch team for their awesome search technology.

