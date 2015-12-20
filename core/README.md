# Usage example

- Download the .src.rpm: 

```$ wget https://hvad.fedorapeople.org/fedora/shinken/shinken-2.4.1-1.fc20.src.rpm```

- Decompress it:

```$ rpm2cpio shinken-2.4.1-1.fc20.src.rpm|cpio -idv```

- Test patch:

```
$ patch -p0 --dry-run --verbose < 2.4.1-1.patch 
Hmm...  Looks like a unified diff to me...
The text leading up to this was:
--------------------------
|--- shinken.spec.ORIG	2015-01-20 14:00:05.411000000 -0500
|+++ shinken.spec	2015-01-20 14:08:51.430000000 -0500
--------------------------
checking file shinken.spec
Using Plan A...
Hunk #1 succeeded at 2.
Hunk #2 succeeded at 104.
done
```

- Patch ```$ cp shinken.spec shinken.spec.ORIG;patch -p0 < 2.4.1-1.patch```


- Copy files into rpmbuild ```$ cp path.cfg *.init *.service shinken.8shinken ~/rpmbuild/SOURCES/``` (adapt the destination path)

- Check the sha1 of latest commit at https://github.com/naparuba/shinken

- Update sha1 in shinken.spec if needed ('%global commit [...]' line)

- Update the patch if needed
```
$ diff -up shinken.spec.ORIG shinken.spec > 2.4.1-1.patch
```
- Download the git HEAD:
```
$ spectool -D --get-files --sourcedir --source 0 shinken.spec
```

- RPM compile ```$ rpmbuild -ba shinken.spec```

- Check the end of compile log:
```
Wrote: /root/rpmbuild/SRPMS/shinken-2.4.1-1_20151220git79972f5.el7.centos.src.rpm
Wrote: /root/rpmbuild/RPMS/noarch/shinken-2.4.1-1_20151220git79972f5.el7.centos.noarch.rpm
Wrote: /root/rpmbuild/RPMS/noarch/shinken-arbiter-2.4.1-1_20151220git79972f5.el7.centos.noarch.rpm
Wrote: /root/rpmbuild/RPMS/noarch/shinken-reactionner-2.4.1-1_20151220git79972f5.el7.centos.noarch.rpm
Wrote: /root/rpmbuild/RPMS/noarch/shinken-scheduler-2.4.1-1_20151220git79972f5.el7.centos.noarch.rpm
Wrote: /root/rpmbuild/RPMS/noarch/shinken-poller-2.4.1-1_20151220git79972f5.el7.centos.noarch.rpm
Wrote: /root/rpmbuild/RPMS/noarch/shinken-broker-2.4.1-1_20151220git79972f5.el7.centos.noarch.rpm
Wrote: /root/rpmbuild/RPMS/noarch/shinken-receiver-2.4.1-1_20151220git79972f5.el7.centos.noarch.rpm
```

- Go to play with shinken HEAD and report good issues :-)


