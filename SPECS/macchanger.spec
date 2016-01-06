Name:           macchanger
Version:        1.6.0
Release:        3
Summary:        An utility for viewing/manipulating the MAC address of network interfaces
Group:          Applications/System
License:        GPLv2+

URL:            http://www.alobbs.com/macchanger
#               https://github.com/alobbs/macchanger

Source0:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig

# https://github.com/alobbs/macchanger/issues/3
Source2:        http://www.gnu.org/licenses/gpl-2.0.txt

# no OUI update at the moment
#Patch0:         macchanger-1.X.0-OUI-list-update.diff

# https://github.com/alobbs/macchanger/commit/27cbde0df8f1bfcfbcacc38d4c40096694303874
Patch3:         macchanger-1.6.0-dynamic-lists.diff
# https://github.com/alobbs/macchanger/commit/8e59754795d9431314e72c19b09d8f150499c8a1
Patch4:         macchanger-1.6.0-dev-name-overflow.diff
# https://github.com/alobbs/macchanger/commit/72f813e68ee6dbedacc87b98286c4803af30ac76
Patch7:         macchanger-1.6.0-endding.diff
# https://github.com/alobbs/macchanger/commit/d93794a34686f9f75f6579e929a17a7762fcb383
Patch8:         macchanger-1.6.0-doc-cleanup.diff
# https://github.com/alobbs/macchanger/commit/52c07ddc355a3415ac31a4106334098e336a5890
Patch9:         macchanger-1.6.0-bia-fix.diff
# https://github.com/alobbs/macchanger/commit/26eda412450f09c4f43961a2e5ac31e92f47d30d
Patch10:        macchanger-1.6.0-show-default.diff


BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post):   /sbin/install-info
Requires(preun):  /sbin/install-info
BuildRequires:    texinfo


%description
Features:
  * set specific MAC address of a network interface
  * set the MAC randomly
  * set a MAC of another vendor
  * set another MAC of the same vendor
  * reset MAC address to its original permanent hardware value
  * display a vendor MAC list (more than 17000 items)


%prep
%setup -q
%patch3 -p1 -b .dynlists
%patch4 -p1 -b .devnameoverflow
%patch7 -p1 -b .endding
%patch8 -p1 -b .docclean
%patch9 -p1 -b .bia
%patch10 -p1 -b .show

cp %{SOURCE2} COPYING


%build
%configure
make %{?_smp_mflags} V=1


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir

%post 
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun 
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_infodir}/*.info.gz
%{_mandir}/man1/*


%changelog
* Wed Jan 06 2016 Ivaylo Kuzev <ivkuzev@gmail.com>
- Initial Build

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  1 2013 Tomas Hoger <thoger@fedoraproject.org> - 1.6.0-1
- Update to upstream 1.6.0 (RHBZ#928256)
- Dropped patches - fixes applied upstream:
  1.5.0-OUI-list-update.diff
  1.5.0-man-update.diff
  1.5.0-random-seed.diff
  1.5.0-exit-code.diff
  1.5.0-formatstr-warning.diff
  1.5.0-permanent-mac.diff
- Patches updated for 1.6.0:
  1.6.0-dynamic-lists.diff
  1.6.0-dev-name-overflow.diff
  1.6.0-endding.diff
- New patches for 1.6.0:
  1.6.0-bia-fix.diff - fix regression from new --bia option
    https://github.com/alobbs/macchanger/issues/1
  1.6.0-show-default.diff - change default action to --show
    https://github.com/alobbs/macchanger/issues/4
  1.6.0-doc-cleanup.diff - documentation cleanup
- Add GPLv2 text, no longer included in 1.6.0 upstream sources.
- texinfo BuildRequires is no longer temporary, as upstream tarball does not
  include .info any more and it needs to be built at compile time.
- Use verbose build output (make V=1).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Tomas Hoger <thoger@fedoraproject.org> - 1.5.0-11
- Fix build warning to do bad format string (size_t).
- Fix command line argument typo: endding -> ending, see Debian bug
  http://bugs.debian.org/621698
- Add option to reset MAC address to hardware permanent address.
  Patch by Anders Sundman, taken from the Debian macchanger package.
- Add texinfo BuildRequires to rebuild .info from updated .texi.
- Minor correction of the man-update patch.
- Update OUI list from IEEE, now more than 15000 items listed

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Tomas Hoger <thoger@fedoraproject.org> - 1.5.0-9
- Fix buffer overflow when excessively long device name is specified as
  command line argument (caught by FORTIFY_SOURCE, RHBZ#641704)
- Add Debian patch fixing exit code for certain error conditions, see
  Debian bug http://bugs.debian.org/547596
- Update OUI list from IEEE, now more than 14000 items listed

* Wed Sep  2 2009 Tomas Hoger <thoger@fedoraproject.org> - 1.5.0-8
- Fix pseudo random number generator seeding (RHBZ#520268)
- Update OUI list from IEEE, now more than 12000 items listed
- Update man page to list -s / --show
- Fix handling of internal mac lists where static array was still assumed,
  while dynamically allocated array was used

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5.0-5
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0-4
- Autorebuild for GCC 4.3

* Sat Mar 24 2007 Damien Durand <splinux@fedoraproject.org> - 1.5.0-3
- Fix doc section

* Sat Mar 24 2007 Damien Durand <splinux@fedoraproject.org> - 1.5.0-2
- Remove info directory in the install section

* Thu Mar 22 2007 Damien Durand <splinux@fedoraproject.org> - 1.5.0-1
- Initial RPM release
