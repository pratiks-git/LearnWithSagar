
BEGIN{
    
}

{
    if ($NF==403){
        for(i=1; i<=NF; i++)
        if ($i ~ /\[.*\]/){
            print $i, count, $NF
            count++
        }
    }
}

END{

}


awk '{ if ($NF==403){ for(i=1; i<=NF; i++) if ($i ~ /\[.*\]/){print $i, $NF; count++} } }'