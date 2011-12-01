Summary:	Tool to translate x86-64 CPU Machine Check Exception data.
Name:		mcelog
Version:	1.0pre3
Release:	0.2%{?dist}
Epoch:		1
Group:		System Environment/Base
License:	GPLv2
Source0:	http://www.kernel.org/pub/linux/utils/cpu/mce/mcelog-%{version}.tar.gz
Patch0:		mcelog-initscript.patch
URL:		http://www.kernel.org/pub/linux/utils/cpu/mce/
Buildroot:	%{_tmppath}/%{name}-%{version}-root
ExclusiveArch:	x86_64

%description
mcelog is a daemon that collects and decodes Machine Check Exception data
on x86-64 machines.

%prep
%setup -q -n %{name}-1.0pre3
%patch0 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS -fpie -pie"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,8}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install mcelog $RPM_BUILD_ROOT%{_sbindir}/mcelog
install mcelog.cron $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/mcelog.cron
cp mcelog.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -m 755 mcelog.init $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/mcelogd
cp mcelog.sysconfig $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/mcelogd
cd ..
chmod -R a-s $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README CHANGES
%{_sbindir}/mcelog
%{_sysconfdir}/cron.hourly/mcelog.cron
%attr(0644,root,root) %{_mandir}/*/*
%attr(0755,root,root) %{_sysconfdir}/rc.d/init.d/mcelogd
%{_sysconfdir}/sysconfig/mcelogd

%changelog
* Thu Apr 08 2010 Prarit Bhargava <prarit@redhat.com> 1:1.0pre3-0.2
- fixed initscript and added /etc/sysconfig/mcelog (BZ 576284)

* Wed Jan 27 2010 Prarit Bhargava <prarit@redhat.com> 1:1.0pre3-0.1
- updated to 1.0pre3
- added initscript for Predictive Failure Analysis (PFA) which does not
  run by default.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1:0.9pre1-0.2
- Rebuilt for RHEL 6

* Mon Oct 05 2009 Orion Poplawski <orion@cora.nwra.com> - 1:0.9pre1-0.1
- Update to 0.9pre1
- Update URL
- Add patch to update mcelog kernel record length (bug #507026)

* Tue Aug 04 2009 Adam Jackson <ajax@redhat.com> 0.7-5
- Fix %%install for new buildroot cleanout.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.7-2
- fix license tag
- clean this package up

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:0.7-1.22
- Autorebuild for GCC 4.3

* Mon Jul 17 2006 Jesse Keating <jkeating@redhat.com>
- Rebuild.

* Fri Jun 30 2006 Dave Jones <davej@redhat.com>
- Rebuild. (#197385)

* Wed May 17 2006 Dave Jones <davej@redhat.com>
- Update to upstream 0.7
- Change frequency to hourly instead of daily.

* Thu Feb 09 2006 Dave Jones <davej@redhat.com>
- rebuild.

* Wed Feb  8 2006 Dave Jones <davej@redhat.com>
- Update to upstream 0.6

* Mon Dec 19 2005 Dave Jones <davej@redhat.com>
- Update to upstream 0.5

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Mar  1 2005 Dave Jones <davej@redhat.com>
- Rebuild for gcc4

* Wed Feb  9 2005 Dave Jones <davej@redhat.com>
- Update to upstream 0.4

* Thu Jan 27 2005 Dave Jones <davej@redhat.com>
- Initial packaging.

