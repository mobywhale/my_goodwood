import mongoengine
import datetime


class Job(mongoengine.EmbeddedDocument):
    job = mongoengine.StringField(required=True)
    line = mongoengine.StringField(required=True)
    description = mongoengine.StringField()
    location = mongoengine.ListField()
    complete = mongoengine.BooleanField( default=False)
    add_omit = mongoengine.BooleanField(default=False)

    meta = {
        'db_alias': 'core',
        'collection': 'jobs'
    }