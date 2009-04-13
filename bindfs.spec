Name:           bindfs
Version:        1.8.3
Release:        1%{?dist}
Summary:        Fuse filesystem to mirror a directory

Group:          System Environment/Base
License:        GPLv2+
URL:            http://code.google.com/p/bindfs/
Source0:        http://bindfs.googlecode.com/files/bindfs-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  fuse-devel
BuildRequires:  recode


%description
Bindfs allows you to mirror a directory and also change the the permissions in
the mirror directory.


%prep
%setup -q
recode latin1..utf8 ChangeLog


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
