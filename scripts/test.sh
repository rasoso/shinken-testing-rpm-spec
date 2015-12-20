for i in `ls *.spec|sed 's/shinken\-//'|sed 's/\.spec//'`
do
    SPEC_SHA1=`grep '^%global commit' shinken-$i.spec|sed 's/%global commit //'`
    REPO_SHA1=`cat $i/.git/refs/heads/master`
    if [ "$SPEC_SHA1" =  "$REPO_SHA1" ]
    then
	echo OK $i
    else
	echo KO $i spec: $SPEC_SHA1 repo: $REPO_SHA1
    fi
done
