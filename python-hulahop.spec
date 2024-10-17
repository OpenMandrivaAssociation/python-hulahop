Name: python-hulahop
Version: 0.7.1
Release: %mkrel 2
Summary: A pygtk widget for embedding mozilla
License: LGPL
Group: Development/Python
Url: https://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/glucose/hulahop/hulahop-%{version}.tar.bz2

Requires: python-gobject  
Requires: pygtk2.0  
Requires: python  
Requires: python-xpcom >= 1.9.2

BuildRequires: autoconf  
BuildRequires: automake  
BuildRequires: gtk+2-devel  
BuildRequires: libtool  
BuildRequires: python-gobject-devel  
BuildRequires: pygtk2.0-devel  
BuildRequires: libpython-devel  
BuildRequires: python-xpcom-devel >= 1.9.2
BuildRequires: xulrunner-devel  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The hulalop library contains a widget for embedding mozilla.
It's based on pyxpcom and give access to the whole mozilla
xpcom API through python.

%prep
%setup -q -n hulahop-%{version}

%build
%define __libtoolize true
%configure --disable-static \
           am_cv_python_pythondir=%{python_sitelib} \
           am_cv_python_pyexecdir=%{python_sitelib}
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
%{python_sitelib}/*
%doc COPYING NEWS
