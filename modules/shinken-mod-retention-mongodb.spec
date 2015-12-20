%global commit 26e0738932cf8d67051b94831939188a728b91cf
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date %(date +%%Y%%m%%d)
%global checkout %{date}git%{shortcommit}
%global module  retention-mongodb
%global repo shinken-monitoring
%global json_version 1.4.2

Name:           shinken-mod-%{module}
Version:        %{json_version}
Release:        %{checkout}%{?dist}
Summary:        Shinken module for saving retention data from schedulers to a mongodb cluster
License:        AGPL
URL:            https://github.com/%{repo}/mod-%{module}
Source0:        https://github.com/%{repo}/mod-%{module}/archive/%{commit}.tar.gz#/%{name}-%{version}-%{commit}.tar.gz

BuildArch: noarch

# shinken-master has the CLI /usr/sbin/shinken
# The --config option of shinken has been added after 2.0
BuildRequires:         shinken >= 2.2


%description
Shinken module for loading Nagios retention data. Load only (no write). For migration.

The high availability allow the Arbiter to send a configuration to a
spare scheduler, but a spare scheduler does not have any saved states
for hosts and services. It will have to recheck them all. It is better
to use a distributed retention module so spares will have all the
information they need to start with an accurate picture of the current
states and scheduling.

%prep
%setup -n mod-%{module}-%{commit}

%build
# directories needed by "shinken [...] install [...]"
mkdir -p $RPM_BUILD_DIR/build-mod-%{module}/var/lib/shinken/modules
mkdir -p $RPM_BUILD_DIR/build-mod-%{module}/var/lib/shinken/doc
mkdir -p $RPM_BUILD_DIR/build-mod-%{module}/var/lib/shinken/inventory
mkdir -p $RPM_BUILD_DIR/build-mod-%{module}/var/lib/shinken/share
mkdir -p $RPM_BUILD_DIR/build-mod-%{module}/etc/shinken/packs
mkdir -p $RPM_BUILD_DIR/build-mod-%{module}/var/lib/shinken/libexec
# shinken.ini file to install module in $RPM_BUILD_DIR/build/
# note that lib has no prefix because this is the path of cli for shinken 
echo '[paths]'                                 > $RPM_BUILD_DIR/shinken.ini.packaging
echo "t = $RPM_BUILD_DIR/build-mod-%{module}" >> $RPM_BUILD_DIR/shinken.ini.packaging
echo 'etc = %%(t)s/etc/shinken'               >> $RPM_BUILD_DIR/shinken.ini.packaging
echo 'lib = /var/lib/shinken'                 >> $RPM_BUILD_DIR/shinken.ini.packaging
echo 'share = %%(t)s%%(lib)s/share'           >> $RPM_BUILD_DIR/shinken.ini.packaging
echo 'cli = %%(lib)s/cli'                     >> $RPM_BUILD_DIR/shinken.ini.packaging
echo 'packs = %%(etc)s/packs'                 >> $RPM_BUILD_DIR/shinken.ini.packaging
echo 'modules = %%(t)s%%(lib)s/modules'       >> $RPM_BUILD_DIR/shinken.ini.packaging
echo 'doc = %%(t)s%%(lib)s/doc'               >> $RPM_BUILD_DIR/shinken.ini.packaging
echo 'inventory = %%(t)s%%(lib)s/inventory'   >> $RPM_BUILD_DIR/shinken.ini.packaging
echo 'libexec = %%(t)s%%(lib)s/libexec'       >> $RPM_BUILD_DIR/shinken.ini.packaging
# install module in $RPM_BUILD_DIR/build/
/usr/sbin/shinken -D -c ../shinken.ini.packaging  install --local .

%install
cp -r ../build-mod-%{module}/* $RPM_BUILD_ROOT/

%files
/var/lib/shinken/modules/*   
/var/lib/shinken/doc/source/89_packages/*
/var/lib/shinken/inventory/*
#/var/lib/shinken/share/*    # not used for this module
#/etc/shinken/packs/*        # not used for this module
/etc/shinken/modules/*

