import pandas as pd
from datetime import datetime, timedelta

# Helper to compute frequency days
def calculate_frequency_days(row):
    frequency_map = {
        'weekly': 7,
        'bi-weekly': 14,
        'monthly': 30,
        'bi-monthly': 60,
        'quarterly': 90,
        'half-yearly': 180,
        'yearly': 365
    }
    return frequency_map.get(row['Frequency'].lower(), None)

# Calculate next contact date
def update_next_contact(row):
    if not pd.isnull(row['Last_Contact']) and not pd.isnull(row['Frequency_Days']):
        last_contact = row['Last_Contact'].date() if isinstance(row['Last_Contact'], pd.Timestamp) else row['Last_Contact']
        return last_contact + timedelta(days=int(row['Frequency_Days']))
    return None

# Calculate next birthday from original date
def calculate_next_date(original_date):
    today = datetime.now().date()
    if pd.isnull(original_date):
        return None
    original_date = original_date.date() if isinstance(original_date, pd.Timestamp) else original_date
    this_year_date = original_date.replace(year=today.year)
    return this_year_date if this_year_date >= today else this_year_date.replace(year=today.year + 1)
