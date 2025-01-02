#!/bin/bash


REPORT_FILE=Report.txt
check_disk_usage(){
    echo "=== Disk Usage ===" >> $REPORT_FILE
    df -h >> $REPORT_FILE
    cat $REPORT_FILE
}


running_services(){
    echo "=== Running Services ===" >> $REPORT_FILE
    systemctl list-units --state running --type service >> $REPORT_FILE
    cat $REPORT_FILE
}

memory_usage() {
    echo "=== Memory usage ===" >> $REPORT_FILE
    free -h >> $REPORT_FILE
    cat $REPORT_FILE
}

cpu_usage(){
    echo "=== CPU Usage ===" >> $REPORT_FILE
    mpstat -P ALL >> $REPORT_FILE
    cat $REPORT_FILE
}

send_email_report(){
    echo "Sending server health report through mail ..."
    TO="recipient@example.com"
    SUBJECT="Test Email"
    BODY=`cat $REPORT_FILE`
    echo -e "Subject: $SUBJECT\n\n$BODY" | ssmtp $TO
}

echo "
################################################
#   Welcome to the server health monitor app   #
################################################

----------- Menu -----------

1 Check Disk Usage
2 Monitor Running Services
3 Assess Memory Usage
4 Evaluate CPU Usage
5 Comprehensive Report via Email Every Four Hours

"
read -p "Select the option from the menu: " menu

echo "You selected $menu"

if [ $menu == 1 ]
then
    check_disk_usage
elif [ $menu == 2 ]
then
    running_services
elif [ $menu == 3 ] 
then 
    memory_usage
elif [ $menu == 4 ]
then 
    cpu_usage
elif [ $menu == 5 ]
then
    send_email_report
fi