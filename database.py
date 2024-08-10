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


    
    # print("type(result):" , type(result))
    # result_all = result.all()
    # print("type(result.all()): ", type(result_all))
    # first_result = result_all[0]
    # print("type(first_result): ",type(first_result))
    # first_result_dict = dict(result_all[0])
    # print("type(first_result_dict): ",type(first_result_dict))
    # print("first_result_dict: ",first_result_dict)