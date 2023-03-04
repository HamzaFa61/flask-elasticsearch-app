# Description: Mapping for the news index

mapping = {
    "mappings": {
        "properties": {
            "link": {
                "type": "text"
            },
            "headline": {
                "type": "text",
                "fields": {
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "category": {
                "type": "text"
            },
            "short_description": {
                "type": "text",
                "fields": {
                    "suggest": {
                        "type": "completion"
                    }
                }
            },
            "authors": {
                "type": "text"
            },
            "date": {
                "type": "date"
            }
        }
    }
}
