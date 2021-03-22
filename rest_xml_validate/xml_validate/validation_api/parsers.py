from rest_framework.parsers import BaseParser


class PlainTextParser(BaseParser):
    """
    Plain text parser.
    """
    media_type = 'text/plain'
    charset = 'utf-8'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a dict {'data': stream_string} that can be read by the MetaDataSerializer
        """
        return {'data': stream.read().decode('utf-8')}
