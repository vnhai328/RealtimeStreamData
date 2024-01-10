config = {
    "openai": {
        "api_key": "ur open AI key"
    },
    "kafka": {
        "sasl.username": "confluent key",
        "sasl.password": "confluent paass",
        "bootstrap.servers": "ur bootstrap server",
        "security.protocol": "SASL_SSL",
        "sasl.mechanism": "PLAIN",
        "session.timeout.ms": 50000
    },
    "schema_registry": {
        "url": "",
        "basic.auth.user.info": "username:password"
    }
}
