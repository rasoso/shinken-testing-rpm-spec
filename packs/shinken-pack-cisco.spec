%global commit 7a3835efe02a95aef77b44a77e5147251eeacbdd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date %(date +%%Y%%m%%d)
%global checkout %{date}git%{shortcommit}
%global builddir $RPM_BUILD_DIR/build-pack-%{pack}-%{commit}
%global repo shinken-monitoring
%global pack  cisco
%global json_version 1.4

Name:           shinken-pack-%{pack}
# This is the version documented in the package.json file.
Version:        %{json_version}
Release:        %{checkout}%{?dist}
Summary:        Shinken configuration pack for Cisco
License:        AGPL
URL:            https://github.com/%{repo}/pack-%{pack}
Source0:        https://github.com/%{repo}/pack-%{pack}/archive/%{commit}.tar.gz#/%{name}-%{version}-%{commit}.tar.gz

BuildArch: noarch

# shinken-master has the CLI /usr/sbin/shinken
# The --config option of shinken has been added after 2.0
BuildRequires:         shinken >= 2.2

#Requires:       shinken-master

%description
Shinken configuration pack for Cisco

%prep
%setup -n pack-%{pack}-%{commit}

%build
# directories needed by "shinken [...] install [...]"
mkdir -p %{builddir}/var/lib/shinken/modules
mkdir -p %{builddir}/var/lib/shinken/doc
mkdir -p %{builddir}/var/lib/shinken/inventory
mkdir -p %{builddir}/var/lib/shinken/share
mkdir -p %{builddir}/etc/shinken/packs
mkdir -p %{builddir}/var/lib/shinken/libexec
# shinken.ini file to install pack in $RPM_BUILD_DIR/build/
# note that lib has no prefix because this is the path of cli for shinken 
echo '[paths]'                                 > $RPM_BUILD_DIR/shinken.ini.packaging
echo "t = $RPM_BUILD_DIR/build-pack-%{pack}-%{commit}" >> $RPM_BUILD_DIR/shinken.ini.packaging
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
cp -r %{builddir}/* $RPM_BUILD_ROOT/

%files
#/var/lib/shinken/modules/*   
#/var/lib/shinken/doc/*
/var/lib/shinken/inventory/*
#/var/lib/shinken/share/*    # not used for this module
/var/lib/shinken/share/images/*
/etc/shinken/packs/*
#/etc/shinken/modules/*

