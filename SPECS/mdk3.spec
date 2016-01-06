Name:       mdk3
Version:    6
Release:    1
Summary:    An 802.11 wireless network security testing tool
Group:      Applications/System
License:    GPLv2
URL:        http://aspj.aircrack-ng.org
#Source0:    http://aspj.aircrack-ng.org/%{name}-v%{version}.tar.bz2
Source0:    %{name}-v%{version}.tar.bz2

%description
%{summary} 

%prep
%setup -q -n %{name}-v%{version}

%build
make

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
%doc AUTHORS COPYING CHANGELOG docs/*
%{_sbindir}/%{name}

%changelog
* Wed Jan 06 2016 Ivaylo Kuzev <ivkuzev@gmail.com> - 6-1
- Initial Build
