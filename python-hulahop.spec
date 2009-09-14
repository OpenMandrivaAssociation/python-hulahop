# NOTE: Do not edit, file was generated by jhconvert

Name: python-hulahop
Version: 0.5.1
Release: %mkrel 4
Summary: A pygtk widget for embedding mozilla
License: LGPL
Group: Development/Python
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/glucose/hulahop/hulahop-0.5.1.tar.bz2

Requires: python-gobject  
Requires: pygtk2.0  
Requires: python  
Requires: python-xpcom  

BuildRequires: autoconf  
BuildRequires: automake  
BuildRequires: gtk+2-devel  
BuildRequires: libtool  
BuildRequires: python-gobject-devel  
BuildRequires: pygtk2.0-devel  
BuildRequires: libpython-devel  
BuildRequires: python-xpcom  
BuildRequires: xulrunner-devel  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
The hulalop library contains a widget for embedding mozilla.
It's based on pyxpcom and give access to the whole mozilla
xpcom API through python.

%prep
%setup -q -n hulahop-0.5.1


%build
%define __libtoolize true
%configure --disable-static am_cv_python_pyexecdir=%{py_platsitedir}
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install


%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%{_datadir}/*
%{_libdir}/hulahop
%{py_platsitedir}/*
%doc COPYING NEWS

