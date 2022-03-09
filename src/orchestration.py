from dagster import job, op
from os import system

@op
def get_algo_data():
  system("python read_algorand_data.py")
    
@op
def write_algo_data():
  system("python write_algorand_price_data.py")

@job
def run_pipeline():
  get_algo_data()
  write_algo_data()
  
if __name__ == "__main__":
  result = run_pipeline.execute_in_process()

# dagster job execute -f orchestration.py
