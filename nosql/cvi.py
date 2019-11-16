import mongoengine

from nosql.job import  Job

class Cvi(mongoengine.Document):
    title = mongoengine.StringField(required=True)
    ref = mongoengine.StringField(required=True)
    number = mongoengine.IntField()

    jobs = mongoengine.EmbeddedDocumentListField(Job)

    meta = {
        'db_alias': 'core',
        'collection': 'cvis'
    }
