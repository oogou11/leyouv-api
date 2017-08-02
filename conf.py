import leconfig.loader

leconfig.loader.load_to_dict(globals(),
                             filename="services.py")


import mongoengine
for alias, attrs in MONGO.items():
    mongoengine.register_connection(alias, **attrs)