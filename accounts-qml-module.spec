#
# Please do not update/rebuild/touch this package before asking first
# to mikala and/or neoclust and/or daviddavid
# This package is part of the KDE Stack.
#

Summary:	QML module to manage the user's online accounts
Name:		accounts-qml-module
Version:	0.7
Release:	1
License:	LGPL v2+
Group:		Libraries
URL:		https://gitlab.com/accounts-sso/accounts-qml-module
Source0:	https://gitlab.com/accounts-sso/accounts-qml-module/-/archive/VERSION_%{version}/%{name}-VERSION_%{version}.tar.bz2
# Source0-md5:	17f735646b47d42b5bfebaf85a561484
## upstream patches
# PATCH-FIX-UPSTREAM
Patch1:		0001-add-a-CONFIG_no_docs-option-to-skip-building-documentation.patch
Patch2:		0002-Build-add-qmltypes-file-to-repository.patch
# PATCH-FIX-UPSTREAM
Patch3:		0003-Fix-compilation-with-Qt-5.13.patch
Patch4:		0004-Fix-build-failure-with-GCC-12.patch
Patch5:		0005-examples_rename-Ubuntu.Components-to-Lomiri.Components.patch
Patch6:		0006-Rename-QML-plugin-to-SSO.OnlineAccounts.patch
Patch7:		0007-Generate-plugin.qmltypes-during-build.patch
Patch8:		0008-Use-C++17-when-building-for-Qt6.patch
Patch9:		0009-Remove-Werror.patch
Patch10:	0010-Find-signon_accounts-for-the-right-Qt-version.patch
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6


#BuildRequires:	cmake(AccountsQt6)
#BuildRequires:	cmake(Qt6Core)
#BuildRequires:	cmake(Qt6Gui)
#BuildRequires:	cmake(Qt6Help)
#BuildRequires:	cmake(Qt6Network)
#BuildRequires:	cmake(Qt6Qml)
#BuildRequires:	cmake(Qt6Test)
#BuildRequires:	cmake(Qt6Xml)
#BuildRequires:	cmake(SignOnQt6)

%description
This QML module provides an API to manage the user's online accounts
and get their authentication data. It's a tiny wrapper around the
Qt-based APIs of libaccounts-qt and libsignon-qt.

#------------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
BuildArch:	noarch

%description doc
This package contains the developer documentation for
accounts-qml-module.

%files doc
%defattr(644,root,root,755)
%doc %{_datadir}/%{name}/


#------------------------------------------------------------------------------

%prep
%setup -q -n %{name}-VERSION_%{version}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1

%build
%qmake_qt6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT INSTALL_ROOT=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_libdir}/qt6/qml/SSO

%clean
rm -rf $RPM_BUILD_ROOT
