# TODO: finish tests (actually run them)
#
# Conditional build:
%bcond_with	tests	# unit tests

Summary:	Symbolic constants in Python
Summary(pl.UTF-8):	Stałe symboliczne w Pythonie
Name:		python3-constantly
Version:	23.10.4
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/constantly/
Source0:	https://files.pythonhosted.org/packages/source/c/constantly/constantly-%{version}.tar.gz
# Source0-md5:	c090579309b2b34be04385b54b0a5a85
URL:		https://pypi.org/project/constantly/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools >= 1:68.2
BuildRequires:	python3-versioneer >= 0.29
%if %{with tests}
BuildRequires:	python3-twisted
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
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

%prep
%setup -q -n constantly-%{version}

%build
%py3_build

%if %{with tests}
# trial-3? ... constantly/test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS LICENSE README.rst
%{py3_sitescriptdir}/constantly
%{py3_sitescriptdir}/constantly-%{version}-py*.egg-info
