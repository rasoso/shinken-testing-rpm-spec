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

Download the source from github:
- ```spectool -D --get-files --sourcedir --source 0 <package.spec>```

Build the .rpm and the .src.rpm:
- ```rpmbuild -ba <package.spec>```

Build the rpms for a specific distribution:
- ```mock -r epel-6-x86_64 <path>/rpmbuild/SRPMS/shinken-pack-linux-snmp-1.4-20141213git580d7e2.el7.centos.src.rpm```

