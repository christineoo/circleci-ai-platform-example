import os

import pandas as pd
from google.cloud import bigquery


def main():
  dates = pd.date_range('20130101', periods=6)
  print(dates)
  print('testing 12345, trigger circleci ~!!')

  client = bigquery.Client(location="US")

  dirname = os.path.dirname(__file__)
  sql_file_path = os.path.join(dirname, 'sql/example.sql')
  query = open(sql_file_path).read()

  query_job = client.query(
            query,
            location="US",
            )

  df = query_job.to_dataframe()
  print(df)



if __name__ == '__main__':
  main()
