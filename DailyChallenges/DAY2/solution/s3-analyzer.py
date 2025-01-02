import json
import argparse
from datetime import datetime 

def get_bucket_list(file_name):
    with open(file_name, "r") as f:
        bucket_list = json.loads(f.read())["buckets"]
    return bucket_list

def summary(bucket_list):
    for i in bucket_list:
        print(f"Name: {i['name']}, Region: {i['region']}, Size: {i['sizeGB']} GB, Versioning: {i['versioning']}")

def get_large_buckets(bucket_list):
    large_buckets = []
    now = datetime.now()
    for i in bucket_list:
        date = datetime.strptime(i["createdOn"], "%Y-%m-%d")
        now = datetime.now()
        age = (now - date).days
        if i["sizeGB"] >= 80 and age > 90:
            large_buckets.append({"Name" : i["name"], "Age": age})
            print(f"'Name' : {i['name']}, 'Age': {age}")
            
def get_cost(bucket_list):
    COST_STANDARD = 0.023
    COST_GLACIER = 0.004  
    region_cost = {}
    team_cost = {}
    environment_cost = {}
    for i in bucket_list:
        size = i["sizeGB"]
        region = i["region"]
        team = i["tags"]["team"]
        environment = i["tags"]["environment"]
        region_cost[region] = round((region_cost.get(region, 0) + size * COST_STANDARD),2)
        team_cost[team] = round((team_cost.get(team, 0) + size * COST_STANDARD),2)
        environment_cost[environment] = round((environment_cost.get(environment, 0) + size * COST_STANDARD),2)
    print(f"=== Total cost breakdown ===")

    for i in region_cost:
        print(f"'Region' : {i}, 'Cost' : {region_cost[i]}")
    for i in team_cost:
        print(f"'Team' : {i}, 'Cost' : {team_cost[i]}")
    for i in environment_cost:
        print(f"'Environment' : {i}, 'Cost' : {environment_cost[i]}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    #Add argumets
    parser.add_argument("-f", "--fileName", required=True, help = "json file name containing s3 bucket list")
    
    # Subcommands for different operations
    subparsers = parser.add_subparsers(dest="command", required=True, help="Command to execute")

    subparsers.add_parser("get_summary", help="Print a summary of each bucket: Name, region, size (in GB), and versioning status")
    large_buckets_parser = subparsers.add_parser("get_large_buckets", help="Identify buckets larger than 80 GB or given threshold from every region which are unused for 90+ days")
    subparsers.add_parser("get_cost", help="Generate a cost report: total s3 buckets cost grouped by region and department")

    large_buckets_parser.add_argument("-t", "--threshold", type=int, default=80, help="Size threshold in GB (default: 80)")

    #Read arguments from command line
    args = parser.parse_args()
    #print(args.fileName)



    file_name=args.fileName
    bucket_list = get_bucket_list(file_name)
    if args.command == "get_summary":
       summary(bucket_list)
       
    if args.command == "get_large_buckets":
       get_large_buckets(bucket_list)

    if args.command == "get_cost":
       get_cost(bucket_list)