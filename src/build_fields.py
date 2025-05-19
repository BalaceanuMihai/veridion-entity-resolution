import pandas as pd

import pandas as pd

def extract_fields(row):
    return {
        'name': str(row.get('company_name', '')).strip().lower(),
        'short_description': str(row.get('short_description', '')).strip().lower(),
        'long_description': str(row.get('long_description', '')).strip().lower(),
        'product_type': str(row.get('product_type', '')).strip().lower(),
        'main_industry': str(row.get('main_industry', '')).strip().lower(),
        'main_business_category': str(row.get('main_business_category', '')).strip().lower(),
        'main_sector': str(row.get('main_sector', '')).strip().lower(),
    }