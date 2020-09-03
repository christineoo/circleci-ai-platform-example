import pandas as pd

def main():
  dates = pd.date_range('20130101', periods=6)
  print(dates)
  print('testing 12345, trigger circleci ~!!')

if __name__ == '__main__':
  main()
