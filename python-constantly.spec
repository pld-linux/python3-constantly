#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Symbolic constants in Python 2
Summary(pl.UTF-8):	Stałe symboliczne w Pythonie 2
Name:		python-constantly
Version:	15.1.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/constantly/
Source0:	https://files.pythonhosted.org/packages/source/c/constantly/constantly-%{version}.tar.gz
# Source0-md5:	f0762f083d83039758e53f8cf0086eef
URL:		https://pypi.org/project/constantly/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library that provides symbolic constant support. It includes
collections and constants with text, numeric, and bit flag values.
Originally twisted.python.constants from the Twisted project.

%description -l pl.UTF-8
Biblioteka zapewniająca obsługę stałych symbolicznych. Obejmuje
kolekcje i stałe o wartościch tekstowych, numerycznych i flagach
bitowych. Wywodzi się z modułu twisted.python.constant z projektu
Twisted.

%package -n python3-constantly
Summary:	Symbolic constants in Python 3
Summary(pl.UTF-8):	Stałe symboliczne w Pythonie 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-constantly
A library that provides symbolic constant support. It includes
collections and constants with text, numeric, and bit flag values.
Originally twisted.python.constants from the Twisted project.

%description -n python3-constantly -l pl.UTF-8
Biblioteka zapewniająca obsługę stałych symbolicznych. Obejmuje
kolekcje i stałe o wartościch tekstowych, numerycznych i flagach
bitowych. Wywodzi się z modułu twisted.python.constant z projektu
Twisted.

%prep
%setup -q -n constantly-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CREDITS LICENSE README.rst
%{py_sitescriptdir}/constantly
%{py_sitescriptdir}/constantly-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-constantly
%defattr(644,root,root,755)
%doc CREDITS LICENSE README.rst
%{py3_sitescriptdir}/constantly
%{py3_sitescriptdir}/constantly-%{version}-py*.egg-info
%endif
