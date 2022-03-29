import os

TORTOISE_ORM = {
    "connections": {"default": "postgres://userAP8:MqEy5fvcMnrg4Ulp@postgresql.tbml.svc.cluster.local:5432/sampledb"},
    "apps": {
        "models": {
            "models": [n
                "db.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}
