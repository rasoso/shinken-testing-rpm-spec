%global commit f82af82c55d9b4eaa5b1fac0019b3209b962ca93
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date %(date +%%Y%%m%%d)
%global checkout %{date}git%{shortcommit}
%global module  raw-socket
%global githubproject mod-rawsocket
%global repo savoirfairelinux
%global json_version 1.5.1

Name:           shinken-mod-%{module}
Version:        %{json_version}
Release:        %{checkout}%{?dist}
Summary:        Module for Shinken Broker. Export data into a network socket
License:        AGPL
#URL:            https://github.com/%{repo}/mod-%{module}
URL:            https://github.com/%{repo}/%{githubproject}
#Source0:        https://github.com/%{repo}/mod-%{module}/archive/%{commit}.tar.gz#/%{name}-%{version}-%{commit}.tar.gz
Source0:        https://github.com/%{repo}/%{githubproject}/archive/%{commit}.tar.gz#/%{name}-%{version}-%{commit}.tar.gz

BuildArch: noarch

# shinken-master has the CLI /usr/sbin/shinken
# The --config option of shinken has been added after 2.0
BuildRequires:         shinken >= 2.2


%description
Module for Shinken Broker. Export data into a network socket

%prep
#%setup -n mod-%{module}-%{commit}
%setup -n %{githubproject}-%{commit}

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
