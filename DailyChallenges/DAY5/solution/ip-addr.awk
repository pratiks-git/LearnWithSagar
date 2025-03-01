
BEGIN{
    
}

{
    for(i=1; i<=NF; i++)
        if ($i ~ 192){
            print $i, count
            count++
        }     
}

END{
print "No of ip-addresses are: " count
}

