- s3-analyzer.py - this is the python program or script which can be used for analysing given json file containg data about S3 buckets
- We can use "-h" option to get information about usage of this script
e.g 
``` 
$ python3 s3-analyzer.py -h
usage: s3-analyzer.py [-h] -f FILENAME {get_summary,get_large_buckets,get_cost} ...

positional arguments:
  {get_summary,get_large_buckets,get_cost}
                        Command to execute
    get_summary         Print a summary of each bucket: Name, region, size (in GB), and versioning status
    get_large_buckets   Identify buckets larger than 80 GB or given threshold from every region which are unused for 90+ days
    get_cost            Generate a cost report: total s3 buckets cost grouped by region and department

options:
  -h, --help            show this help message and exit
  -f FILENAME, --fileName FILENAME
                        json file name containing s3 bucket list
```

- Example usage:
```
$ python3 s3-analyzer.py -f ../buckets.json get_summary
Name: prod-data, Region: us-west-2, Size: 120 GB, Versioning: True
Name: dev-app-logs, Region: us-east-1, Size: 10 GB, Versioning: False
Name: backup, Region: eu-central-1, Size: 80 GB, Versioning: True
Name: audit-logs, Region: ap-southeast-1, Size: 50 GB, Versioning: True
Name: test-results, Region: us-west-1, Size: 15 GB, Versioning: False
Name: old-backups, Region: us-east-2, Size: 200 GB, Versioning: True
Name: staging-resources, Region: eu-west-1, Size: 30 GB, Versioning: False
Name: app-analytics, Region: ap-northeast-1, Size: 250 GB, Versioning: True
Name: raw-data, Region: us-west-2, Size: 90 GB, Versioning: False
Name: compliance-data, Region: ca-central-1, Size: 300 GB, Versioning: True
```