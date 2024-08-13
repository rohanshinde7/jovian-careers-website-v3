from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

# Create the engine with an SSL connection and increased timeout
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))

        jobs = []
        # Convert each row into a dictionary
        for row in result:
            row_dict = dict(zip(result.keys(), row))
            jobs.append(row_dict)

    return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            {"val": id}  # Pass the parameter as a dictionary
        )

        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(zip(result.keys(), rows[0]))
