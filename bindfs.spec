%global _hardened_build 1

Name:           bindfs
Version:        1.12.4
Release:        3%{?dist}
Summary:        Fuse filesystem to mirror a directory

Group:          System Environment/Base
License:        GPLv2+
URL:            http://bindfs.org/
Source0:        http://bindfs.org/downloads//bindfs-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  fuse-devel


%description
Bindfs allows you to mirror a directory and also change the the permissions in
the mirror directory.


%prep
%setup -q


%build
%configure INSTALL="%{_bindir}/install -p"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Till Maas <opensource@till.name> - 1.12.4-1
- Update to new release

* Wed Jan 15 2014 Till Maas <opensource@till.name> - 1.12.3-1
- Update to new release
- Harden build

* Thu Jul 25 2013 Till Maas <opensource@till.name> - 1.12.2-1
- Update to new release
- Update URL
- Update source URL

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Till Maas <opensource@till.name> - 1.11-1
- Update to new release
- Do not recode ChangeLog anymore

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 13 2012 Till Maas <opensource@till.name> - 1.10-1
- Update to new release

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.8.3-3
- Rebuilt with new fuse

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Till Maas <opensource@till.name> - 1.8.3-1
- Update to new upstream release

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 14 2008 Till Maas <opensource@till.name> - 1.8.2-2
- Update URL and Source0 to google code

* Sun Dec 14 2008 Till Maas <opensource@till.name> - 1.8.2-1
- Update to new release with GPLv2+ license headers 

* Fri Dec 12 2008 Till Maas <opensource@till.name> - 1.8.1-2
- Skip Requires: fuse
- Preseve timestamp of manpage with install -p in %%configure

* Fri Dec 12 2008 Till Maas <opensource@till.name> - 1.8.1-1
- Update to new release

* Wed Oct 29 2008 Till Maas <opensource@till.name> - 1.8-2
- Convert ChangeLog to UTF8

* Wed Oct 29 2008 Till Maas <opensource@till.name> - 1.8-1
- Update to new release

* Fri Oct 05 2007 Till Maas <opensource till name> - 1.3-1
- initial spec for Fedora
