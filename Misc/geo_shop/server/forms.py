from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, Field
from wtforms.validators import InputRequired as IR, NumberRange as NR, Optional


class TagListField(Field):

    def process_formdata(self, valuelist):

        if valuelist:
            self.data = set([x.strip() for x in valuelist[0].split(',')])
        else:
            self.data = []

    def invalid_tags(self, possible_tags):

        invalid_tags = []
        if len(self.data) > 0:
            for tag in self.data:
                if tag not in possible_tags:
                    invalid_tags.append(tag)
        return invalid_tags


class SearchForm(FlaskForm):

    total_products = IntegerField('total_products', [IR(), NR(min=1)])
    radius = IntegerField('radius', [IR(), NR(min=0)])

    lat = FloatField('lat', [IR(), NR(min=-90, max=90)])
    lng = FloatField('lng', [IR(), NR(min=-180, max=180)])

    tags = TagListField('tags', [Optional()])
