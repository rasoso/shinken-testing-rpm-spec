# Usage example

- Download the .src.rpm:

```$ wget http://copr-be.cloud.fedoraproject.org/results/hvad/shinken/epel-7-x86_64/shinken-2.2-RC1.fc20/shinken-2.2-RC1.el7.centos.src.rpm```

- Decompress it:

```$ rpm2cpio shinken-2.2-RC1.el7.centos.src.rpm|cpio -idv```

- Test patch:

```
$ patch -p0 --dry-run --verbose < 2.2-RC1.patch
Hmm...  Looks like a unified diff to me...
The text leading up to this was:
--------------------------
|--- shinken.spec.ORIG  2015-01-15 14:31:01.438000000 -0500
|+++ shinken.spec       2015-01-15 14:33:19.665000000 -0500
--------------------------
checking file shinken.spec
Using Plan A...
Hunk #1 succeeded at 2.
Hunk #2 succeeded at 105.
done
```

- Patch ```$ cp shinken.spec shinken.spec.ORIG;patch -p0 < 2.2-RC1.patch```


- Copy files into rpmbuild ```$ cp path.cfg *.init *.service shinken.8shinken shinken-2.2-RC1.tar.gz ~/rpmbuild/SOURCES/``` (adapt the destination path)

- Check the sha1 of latest commit at https://github.com/naparuba/shinken

- Update sha1 in shinken.spec if needed

- Update the patch if needed
```
$ diff -up shinken.spec.ORIG shinken.spec > 2.2-RC1.patch
```
- Download the git HEAD:
```
$ spectool -D --get-files --sourcedir --source 0 shinken.spec
```

- RPM compile ```$ rpmbuild -ba shinken.spec```

- Check the end of compile log:
```
Wrote: /home/test/rpmbuild/SRPMS/shinken-2.2-20150115git9c8a04f.el7.centos.src.rpm
Wrote: /home/test/rpmbuild/RPMS/noarch/shinken-2.2-20150115git9c8a04f.el7.centos.noarch.rpm
Wrote: /home/test/rpmbuild/RPMS/noarch/shinken-arbiter-2.2-20150115git9c8a04f.el7.centos.noarch.rpm
Wrote: /home/test/rpmbuild/RPMS/noarch/shinken-reactionner-2.2-20150115git9c8a04f.el7.centos.noarch.rpm
Wrote: /home/test/rpmbuild/RPMS/noarch/shinken-scheduler-2.2-20150115git9c8a04f.el7.centos.noarch.rpm
Wrote: /home/test/rpmbuild/RPMS/noarch/shinken-poller-2.2-20150115git9c8a04f.el7.centos.noarch.rpm
Wrote: /home/test/rpmbuild/RPMS/noarch/shinken-broker-2.2-20150115git9c8a04f.el7.centos.noarch.rpm
Wrote: /home/test/rpmbuild/RPMS/noarch/shinken-receiver-2.2-20150115git9c8a04f.el7.centos.noarch.rpm
```

- Go to play with shinken HEAD and report good issues :-)

