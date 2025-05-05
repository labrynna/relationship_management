def update_next_contact(row):
    if not pd.isnull(row['Last_Contact']) and not pd.isnull(row['Frequency_Days']):
        last_contact = row['Last_Contact'].date() if isinstance(row['Last_Contact'], pd.Timestamp) else row['Last_Contact']
        return last_contact + timedelta(days=int(row['Frequency_Days']))
    return None
