from flask import (
    Blueprint,
    jsonify,
    request,
    render_template,
)
from application.shared.constants import (
    index_name,
)
from application import es_client as es

api = Blueprint('api', __name__)


@api.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'No search query provided'})

    # define Elasticsearch query
    es_query = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["headline", "short_description"]
            }
        }
    }

    # execute search query against Elasticsearch index
    res = es.search(index=index_name, body=es_query)

    # extract relevant fields from search results
    hits = res['hits']['hits']
    results = []
    for hit in hits:
        result = {
            'headline': hit['_source']['headline'],
            'short_description': hit['_source']['short_description'],
            'date': hit['_source']['date'],
            'link': hit['_source']['link']
        }
        results.append(result)

    # return search results as JSON
    return jsonify({'results': results})


@api.route('/suggest', methods=['GET'])
def suggest():
    text = request.args.get('text', '')
    field = request.args.get('field', 'headline')
    size = int(request.args.get('size', '10'))

    suggester = {
        "suggest": {
            "text": text,
            "my_suggestion": {
                "prefix": text,
                "completion": {
                    "field": f"{field}.suggest",
                    "size": size
                }
            }
        }
    }

    res = es.search(index=index_name, body=suggester)

    suggestions = []
    if res['suggest'] and res['suggest']['my_suggestion'][0]['options']:
        for option in res['suggest']['my_suggestion'][0]['options']:
            suggestions.append(option['text'])

    return jsonify({"suggestions": suggestions})


@api.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        res = es.search(index="news_articles", body={
                        "query": {"match": {"headline": query}}})
        hits = res['hits']['hits']
        return render_template('results.html', hits=hits, query=query)
    else:
        return render_template('index.html')
