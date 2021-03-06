# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Google spreadsheet key
#SPREADSHEET_KEY = "10HmPJvXi_X2RHb8s_oQ2WGGsBlz-tHuW2n1dsomaD7c"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Spreadsheet cache lifetime in seconds. (Default: 4)
# SPREADSHEET_CACHE_TTL = 4

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# Get context from a local file or URL. This file can be a CSV or Excel
# spreadsheet file. Relative, absolute, and remote (http/https) paths can be 
# used.
CONTEXT_SOURCE_FILE = "data/_slides.xlsx"

# EXPERIMENTAL: Path to a credentials file to authenticate with Google Drive.
# This is useful for for automated deployment. This option may be replaced by
# command line flag or environment variable. Take care not to commit or publish
# your credentials file.
# CREDENTIALS_PATH = ""

# S3 bucket configuration
S3_BUCKETS = {
     #Provide target -> s3 url pairs, such as:
         #"mytarget": "mys3url.bucket.url/some/path"
     #then use tarbell publish mytarget to publish to it
    'production': 'recoveredfactory.net/dbootcamp-2015',
    'staging': 'recoveredfactory.net/dbootcamp-2015',
}

# Default template variables
DEFAULT_CONTEXT = {
    'data': [   {   'column1': u'row1, column1',
                    'column2': u'row1, column2'},
                {   'column1': u'row2, column1',
                    'column2': u'row2, column2'}],
    'headline': u'Test headline',
    'keyed_data': {   'key1': {   'column1': u'key1, column1',
                                  'column2': u'key1, column2',
                                  'key': u'key1'},
                      'key2': {   'column1': u'key2, column1',
                                  'column2': u'key2, column2',
                                  'key': u'key2'}},
    'name': 'dc-dbootcamp-2015',
    'title': 'DC Data Bootcamp 2015'
}
