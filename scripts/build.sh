for spec in `ls *.spec`
do
    spectool -D --get-files --sourcedir --source 0 $spec
    rpmbuild -ba $spec
done
