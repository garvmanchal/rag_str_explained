from app.ingestion.chunking import chunk_document
from datetime import date
from app.database.vector_db import vector_db


def seed_index():
    ''' 
    runs once when the app starts : chunk and index one sample document
    '''
    handbook = (
        "Full-time employees accrue 12 paid sick days per year. Sick days reset every "
        "January 1st and are tracked in the HR portal. Employees must notify their "
        "manager before 10am on the day of absence. Unused sick days roll over up to a "
        "maximum of 5 days into the following               year. Part-time employees accrue sick "
        "days on a pro-rated basis based on hours worked."

    )

    for chunk in chunk_document(
        source_id = "hr-handbook",
        heading = "Sick leave",
        text = handbook,
        permission_scope = "all-employees",
        updated_at = str(date(2026,9,2))
    ):
        vector_db.upsert(chunk)









