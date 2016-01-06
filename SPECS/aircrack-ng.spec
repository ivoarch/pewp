Name:           aircrack-ng
Version:        1.2.rc3
Release:        1
Summary:        Reliable 802.11 (wireless) sniffer and WEP/WPA-PSK key cracker
License:        GPL
#Source:         http://dl.aircrack-ng.org/%{name}-%{version}.tar.gz
Source:         %{name}-1.2-rc3.tar.gz
URL:            http://www.aircrack-ng.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  openssl-devel sqlite-devel libnl-devel pcre-devel 
Group:          Applications/System

%description
aircrack-ng is a set of tools for auditing wireless networks. It's an
enhanced/reborn version of aircrack. It consists of airodump-ng (an 802.11
packet capture program), aireplay-ng (an 802.11 packet injection program),
aircrack (static WEP and WPA-PSK cracking), airdecap-ng (decrypts WEP/WPA
capture files), and some tools to handle capture files (merge, convert,
etc.).

%prep
%setup -q -n %{name}-1.2-rc3

%build
export CFLAGS=$RPM_OPT_FLAGS

# sqlite: needed to compile airolib-ng and add support for airolib-ng
#         databases in aircrack-ng.
#
# experimental: needed to compile tkiptun-ng, easside-ng (and buddy-ng),
#               wesside-ng and besside-ng.
#               If you want to build besside-ng-crawler, you will need
#               LibPCAP (development package). On Debian based
#               distributions: libpcap-dev
#
# pcre:	Add support for regular expression matching for ESSID in airodump-ng and besside-ng.
make %{?_smp_mflags} sqlite=true pcre=true experimental=true

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} mandir=%{_mandir}/man1 sqlite=true pcre=true experimental=true

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog LICENSE README VERSION test/ patches/
%{_bindir}/aircrack-ng
%{_bindir}/airdecap-ng
%{_bindir}/airdecloak-ng
%{_bindir}/airolib-ng
%{_bindir}/besside-ng-crawler
%{_bindir}/buddy-ng
%{_bindir}/ivstools
%{_bindir}/kstats
%{_bindir}/makeivs-ng
%{_bindir}/packetforge-ng
%{_bindir}/wpaclean
%{_sbindir}/airbase-ng
%{_sbindir}/aireplay-ng
%{_sbindir}/airmon-ng
%{_sbindir}/airodump-ng
%{_sbindir}/airodump-ng-oui-update
%{_sbindir}/airserv-ng
%{_sbindir}/airtun-ng
%{_sbindir}/besside-ng
%{_sbindir}/easside-ng
%{_sbindir}/tkiptun-ng
%{_sbindir}/wesside-ng
%{_mandir}/man1/aircrack-ng.1.gz
%{_mandir}/man1/airdecap-ng.1.gz
%{_mandir}/man1/airdecloak-ng.1.gz
%{_mandir}/man1/airolib-ng.1.gz
%{_mandir}/man1/besside-ng-crawler.1.gz
%{_mandir}/man1/buddy-ng.1.gz
%{_mandir}/man1/ivstools.1.gz
%{_mandir}/man1/kstats.1.gz
%{_mandir}/man1/makeivs-ng.1.gz
%{_mandir}/man1/packetforge-ng.1.gz
%{_mandir}/man1/wpaclean.1.gz
%{_mandir}/man8/airbase-ng.8.gz
%{_mandir}/man8/aireplay-ng.8.gz
%{_mandir}/man8/airmon-ng.8.gz
%{_mandir}/man8/airodump-ng-oui-update.8.gz
%{_mandir}/man8/airodump-ng.8.gz
%{_mandir}/man8/airserv-ng.8.gz
%{_mandir}/man8/airtun-ng.8.gz
%{_mandir}/man8/besside-ng.8.gz
%{_mandir}/man8/easside-ng.8.gz
%{_mandir}/man8/tkiptun-ng.8.gz
%{_mandir}/man8/wesside-ng.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jan 05 2016 Ivaylo Kuzev <ivoarch@gmail.com>
- Update to latest release

