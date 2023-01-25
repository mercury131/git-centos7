Name:           git
Version:        2.38.3
Release:        0
License:        GPL
Prefix:         %{_prefix}
Source:         https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.38.3.tar.gz
Summary:        git 2.38.3
BuildRoot:      %{_tmppath}/%{name}-root

%description
git 2.38.3 for centos 7

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/local # standard way

make


%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
#[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/*
#/git
%changelog
* Sun Nov  18 2020 Anton Cherevaty
- git 2.38.3 for centos 7 version being packaged

