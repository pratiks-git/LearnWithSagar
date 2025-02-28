### To print all the ip-addresses
```
awk '{ for(i=1; i<=NF; i++) {if ($i ~ /[0-9]+\.[0-9]+\.[0-9]+\.[0-9]/){print $i, count ;count++}} } END{ print "No of ip-addresses are: " count}' user_activity.log 
```

### To print unique ip-addresses 
```
awk '{ for(i=1; i<=NF; i++) {if ($i ~ /[0-9]+\.[0-9]+\.[0-9]+\.[0-9]/){a[$i]++}} } END{ for (b in a){print b; count++} ; print "No of unique ip-addresses are: " count} ' user_activity.log
```

### To print all users
```
awk '{ for(i=1; i<=NF; i++) {if ($i ~ "user"){print $i, count ;count++}} } END{ print "No of users are: " count}' user_activity.log
```

### To print unique users
```
awk '{ for(i=1; i<=NF; i++) {if ($i ~ "user"){a[$i]++}} } END{ for(b in a){ print b; count++ };print "No of unique users are: " count}' user_activity.log
```

### Http status codes
```
awk '{if($NF==500) a++ ; if($NF==200) b++;  if($NF==403) c++ ;if($NF==404) d++} END{print "500: "a "\n200: "b "\n403: "c "\n404: "d}' user_activity.log | sort -k1
```

### Failed Login Attempts with timestamp
```
awk '{ if ($NF==403){ for(i=1; i<=NF; i++) if ($i ~ /\[.*\]/){print $i,$NF; count++} } } END{print "Total failed attempts are: " count}' user_activity.log 
```

## Summary report
1. Total number of unique users
```
awk '{ for(i=1; i<=NF; i++) {if ($i ~ "user"){a[$i]++}} } END{ for(b in a) count++ ;print "No of unique users are: " count}' user_activity.log
```

2. Total number of requests per user
```
awk '{ for(i=1; i<=NF; i++) {if ($i ~ "user"){a[$i]++}} } END{ print "No of unique users are: " count ;for(b in a) print b, a[b]}' user_activity.log
```

3. Total number of successful requests (status code 200).
```
awk ' $NF ==200 {count++} END{print "Total number of successful requests: " count}' user_activity.log
```

4. Total number of failed requests (status codes 404 and 403).
```
awk ' $NF==404 || $NF==403 {count++} END{print "Total number of failed requests: " count}' user_activity.log
```