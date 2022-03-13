import os

TORTOISE_ORM = {
    "connections": {"default": "postgres://userAP8:MqEy5fvcMnrg4Ulp@tbml-test-db-tbml.apps.okd4.cjlabs.dev:443/sampledb"},
    "apps": {
        "models": {
            "models": [
                "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}