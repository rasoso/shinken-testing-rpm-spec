# shinken-testing-rpm-spec
spec files for testing shinken

These are *unofficial* .spec files for *testing* shinken with rpm
packages on most recent code (HEAD of github).

Use official methods for production :-)

This needs a shinken >= 2.2 in order to have the "shinken install" --local option.

The rpm naming is:
- ```shinken-<pack|module>-<name>-<json version>-<YYYYMMDD compile day>git<short sha1>.<....>.rpm```
- example: ```shinken-pack-linux-snmp-1.4-20141213git580d7e2.el7.centos.src.rpm```

# Usage examples

Download the source from github with spectool from rpmdevtools package:
- ```spectool -D --get-files --sourcedir --source 0 <package.spec>```

Build the .rpm and the .src.rpm with the rpmbuild command from rpm-build package:
- ```rpmbuild -ba <package.spec>```

Build the rpms for a specific distribution with mock command from mock package:
- ```mock -r epel-6-x86_64 <path>/rpmbuild/SRPMS/shinken-pack-linux-snmp-1.4-20141213git580d7e2.el7.centos.src.rpm```

