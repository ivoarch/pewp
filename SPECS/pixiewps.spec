Name:           pixiewps
Version:        1.2.2
Release:        1
Summary:        An offline WPS bruteforce utility         
License:        GPLv2
URL:            https://github.com/wiire/pixiewps
Source0:        %{name}-%{version}.tar.gz

%description
Pixiewps is a tool written in C used to bruteforce offline the WPS pin 
exploiting the low or non-existing entropy of some Access Points, the so-called "pixie dust attack" 
discovered by Dominique Bongard in summer 2014. It is meant for educational purposes only.

As opposed to the traditional online bruteforce attack, implemented in tools like Reaver or Bully 
which aim to recover the pin in a few hours, this method can get the pin in only a matter of milliseconds to minutes, 
depending on the target, if vulnerable.

%prep
%setup -q

%build
cd src
make %{?_smp_mflags}

%install
install -m 755 -D src/%{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}
install -m 644 -D README.md $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}/README.md

%files
%{_bindir}/%{name}
%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jan 06 2016 Ivaylo Kuzev <ivkuzev@gmail.com> - 1.2-1
- Initial build
 
