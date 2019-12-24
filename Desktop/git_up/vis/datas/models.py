from mongoengine import IntField, StringField, DynamicDocument, ListField, DictField
# Create your models here.


class USPTO_all(DynamicDocument):
    _id = IntField(primary_key=True)
    reaction_smiles = StringField(max_length=300)
    reactants = ListField(DictField())
    products = ListField(DictField())
    solvents = ListField(DictField())
    temperature = StringField(max_length=300)
    description = StringField(max_length=300)
    source = StringField(max_length=300)
    reference = StringField(max_length=300)
    paragraph = StringField(max_length=300)
    # 指明连接的数据表名
    meta = {
        'collection': 'USPTO_all_copy'
    }

    def __str__(self):
        return self.reaction_smiles

