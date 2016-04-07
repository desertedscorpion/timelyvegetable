Name:           shinyalarm
Version:        VERSION
Release:        RELEASE
Summary:        Use my custom repo

Group:          Administrative
License:        GNU/GPL3
URL:            https://github.com/desertedscorpion/helplessmountain
Source:         %{name}-%{version}.tar.gz
Prefix:         %{_prefix}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  git coreutils
Requires:       git systemd

%define debug_package %{nil}

%description
Installs my custom repo (from a git repo) and schedules a service to update it regularly.

%prep
%setup -q

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir --parents ${RPM_BUILD_ROOT}/srv/rpm/shinyalarm
git -C ${RPM_BUILD_ROOT}/srv/rpm/shinyalarm init
git -C ${RPM_BUILD_ROOT}/srv/rpm/shinyalarm remote add origin https://github.com/desertedscorpion/hollowmoon.git
mkdir --parents ${RPM_BUILD_ROOT}/etc/yum.repos.d
cp shinyalarm.repo ${RPM_BUILD_ROOT}/etc/yum.repos.d
mkdir --parents ${RPM_BUILD_ROOT}/usr/lib/systemd/system
cp shinyalarm.service ${RPM_BUILD_ROOT}/usr/lib/systemd/system
cp shinyalarm.timer ${RPM_BUILD_ROOT}/usr/lib/systemd/system

%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%attr(0007,root,root) /srv/rpm/shinyalarm
%attr(0664,root,root) /etc/yum.repos.d/shinyalarm.repo
%attr(0664,root,root) /usr/lib/systemd/system/shinyalarm.service
%attr(0664,root,root) /usr/lib/systemd/system/shinyalarm.timer
