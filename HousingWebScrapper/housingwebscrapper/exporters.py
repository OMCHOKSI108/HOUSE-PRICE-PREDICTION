from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter, JsonItemExporter

"""
This exporter works when you
        add a new option in FEED_EXPORTERS within settings.py pointing to this class
        add a CSV_DELIMITER key in settings.py
    
    Then, start scrapy with following command
    scrapy crawl spidername --set FEED_URI=output.csv --set FEED_FORMAT=custom_csv


"""

class CsvOptionRespactingItemExporter(CsvItemExporter):
    """
    Custom CSV exporter that respects the CSV_DELIMITER setting.
    """

    def __init__(self, *args, **kwargs):
        # Get the custom delimiter from settings
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter
        super(CsvOptionRespectingItemExporter, self).__init__(*args, **kwargs)