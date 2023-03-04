from flask import Flask
from elasticsearch import Elasticsearch
from application.elastic_.mapping import mapping
from application.elastic_.utils import (
    create_index_if_not_exists,
    index_data,
)
from application.shared.constants import (
    index_name,
    doc_type,
    elastic_host,
    elastic_port,
)


es_client = Elasticsearch([{'host': elastic_host, 'port': elastic_port}])
create_index_if_not_exists(index_name, es_client, mapping)
index_data(es_client, index_name, doc_type)


def register_blueprints(app):
    from application.views import api
    app.register_blueprint(api)


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app
