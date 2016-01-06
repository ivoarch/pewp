Summary:        Brute force attack against WPS, that actually works
Name:           bully
Version:        1.0.22
Release:        1
License:        GPLv2+
Group:          Applications/System
Source0:        %{name}-1.0-22.tar.gz
URL:            http://code.google.com/p/bully/            
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libpcap-devel openssl-devel
 
%description
Bully is a new implementation of the WPS brute force attack, written in C. It is conceptually identical
to other programs, in that it exploits the (now well known) design flaw in the WPS specification. It has
several advantages over the original reaver code. These include fewer dependencies, improved memory and
cpu performance, correct handling of endianness, and a more robust set of options. It runs on Linux, and
was specifically developed to run on embedded Linux systems (OpenWrt, etc) regardless of architecture.

Bully provides several improvements in the detection and handling of anomalous scenarios. It has been
tested against access points from numerous vendors, and with differing configurations, with much success.

%prep
%setup -q -n %{name}-1.0-22

%build
cd src
make %{?_smp_mflags}

%install
install -m 755 -D src/%{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/bully

%changelog
* Tue Jan 05 2016 Ivaylo Kuzev <ivoarch@gmail.com> - 1.0.22-1
- Initial spec
