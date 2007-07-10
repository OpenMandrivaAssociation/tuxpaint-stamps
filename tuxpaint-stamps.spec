Summary:	Pictures for use with the paint program Tuxpaint
Name: 		tuxpaint-stamps
Version:	2007.07.01
Release:	%mkrel 1
License:	GPL
Source: 	%{name}-%{version}.tar.bz2

Group:		Graphics
URL:		http://www.newbreedsoftware.com/tuxpaint/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
Requires: 	tuxpaint

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
rm -rf `find -name CVS`

%install
rm -rf $RPM_BUILD_ROOT
mv Makefile Makefile.tmp
cat Makefile.tmp | sed -e "s#^PREFIX=/usr/local#PREFIX=$RPM_BUILD_ROOT/usr#g" > Makefile
rm -f Makefile.tmp

make install-all

# fix perms
chmod -R go=u-w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/*
%{_datadir}/tuxpaint/*
