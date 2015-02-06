Summary:	Pictures for use with the paint program Tuxpaint
Name: 		tuxpaint-stamps
Version:	2009.06.28
Release:	3
License:	GPL
Group:		Graphics
URL:		http://www.newbreedsoftware.com/tuxpaint/
Source: 	%{name}-%{version}.tar.gz
Patch0:		tuxpaint-stamps-2009.06.28-mixed-rules.patch

BuildArch:	noarch
Requires:	tuxpaint

%description
Tux Paint is a simple paint program gear towards young children. 
It provides a simple but entertaining interface, allows drawing
with brushes, lines, shapes, and 'stamps,' and has a 'magic' 
tool, for special effects. Loading and saving is done via a 
graphical interface, and the underlying environment's 
filesystem isn't exposed (much like programs on PDAs).

This packages contains a lot of extra pictures (stamps) for tuxpaint.

%prep
%setup -q
%patch0 -p0
rm -rf `find -name CVS`
# Fix unreadable files
find . -perm 0600 -exec chmod 0644 '{}' \;

%install
mv Makefile Makefile.tmp
cat Makefile.tmp | sed -e "s#^PREFIX=/usr/local#PREFIX=%{buildroot}/usr#g" > Makefile
rm -f Makefile.tmp

make install-all

%files
%doc docs/*
%{_datadir}/tuxpaint/*

%changelog
* Tue Aug 18 2009 Frederik Himpe <fhimpe@mandriva.org> 2009.06.28-1mdv2010.0
+ Revision: 417826
- Update to new version 2009.06.28

* Fri Aug 01 2008 Funda Wang <fundawang@mandriva.org> 2008.06.30-1mdv2009.0
+ Revision: 259566
- New version 2008.06.30

* Mon Jun 16 2008 Thierry Vignaud <tvignaud@mandriva.com> 2007.07.01-2mdv2009.0
+ Revision: 220174
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2007.07.01-1mdv2008.1
+ Revision: 136552
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 10 2007 Funda Wang <fundawang@mandriva.org> 2007.07.01-1mdv2008.0
+ Revision: 50971
- New version


* Fri Dec 01 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 2006.12.01-1mdv2007.0
+ Revision: 89729
- Fix spec file
- 2006.12.01

  + Lenny Cartier <lenny@mandriva.com>
    - Import tuxpaint-stamps

* Thu Feb 09 2006 Lenny Cartier <lenny@mandriva.com> 2005.11.25-1mdk
- 2005.11.25

* Sun Jan 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2003.12.23-1mdk
- new release
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- don't own %%{_datadir}/tuxpaint
- cosmetics
- get rid of CVS files

