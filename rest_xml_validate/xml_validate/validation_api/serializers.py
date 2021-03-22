from rest_framework import serializers, status
from validation_api.models import MetaData
from lxml import etree
from io import StringIO
import os


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaData
        fields = ['data', 'version']

    def validate_version(self, data):
        version_numbers = os.listdir(os.getcwd() + '/validation_api/datacite_schema_versions/')
        if str(data) in version_numbers:
            return data
        else:
            raise serializers.ValidationError("Datacite Version " + str(data) + " is not supported.", code=404)

    def validate(self, data):
        version = data['version']
        xmlschema_path = os.getcwd() + '/validation_api/datacite_schema_versions/{}/datacite.xsd'.format(version)
        xmlschema_doc = etree.parse(xmlschema_path)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        try:
            valid = StringIO(data['data'])
            doc = etree.parse(valid)
            xmlschema.assertValid(doc)
            return data
        except:
            raise serializers.ValidationError(xmlschema.error_log.last_error, code=400)
