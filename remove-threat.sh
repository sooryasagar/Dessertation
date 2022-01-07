
#!/bin/bash

# Checking user arguments
if [ "x$1" == "xdelete" ]; then
    exit 0;
fi

LOCAL=`dirname $0`;
cd $LOCAL
cd ../

PWD=`pwd`

# Removing file
rm -f $3
if [ $? -eq 0 ]; then
    echo "`date` $0 Removed positive threat located in $3" >> ${PWD}/../logs/active-responses.log
else
    echo "`date` $0 Error removing positive threat located in $3" >> ${PWD}/../logs/active-responses.log
fi

exit 0;