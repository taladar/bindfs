Name:           bindfs
Version:        1.13.1
Release:        2%{?dist}
Summary:        Fuse filesystem to mirror a directory

Group:          System Environment/Base
License:        GPLv2+
URL:            http://bindfs.org/
Source0:        http://bindfs.org/downloads//bindfs-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  fuse-devel
# for test suite
BuildRequires:  ruby
BuildRequires:  valgrind
# Needed to mount bindfs via fstab
Recommends:     fuse


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


%check
# Fedora's koji does not provide /dev/fuse, therefore skip the tests there
# Always cat log files on failure to be able to debug issues
if [ -e /dev/fuse ]; then
    make check || (cat tests/test-suite.log tests/internals/test-suite.log; false)
else
    # internal tests use valgrind and should work
    make -C tests/internals/ check || (cat tests/internals/test-suite.log; false)
fi


%files
%defattr(-,root,root,-)
%license COPYING
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Apr 08 2016 Till Maas <opensource@till.name> - 1.13.1-2
- Add recommendation for fuse (https://bugzilla.redhat.com/1320272)

* Mon Feb 22 2016 Till Maas <opensource@till.name> - 1.13.1-1
- Update to new release
- cleanup spec

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Till Maas <opensource@till.name> - 1.13.0-1
- Update to new release
- Use %%license
- Add testsuite

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 03 2014 Till Maas <opensource@till.name> - 1.12.6-1
- Update to new release

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
