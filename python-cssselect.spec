%define	module	cssselect
%define name	python-%{module}
%define version 0.6.1
%define release 1

Summary: Library for parsing CSS3 selectors and translating them to XPath 1.0
Name:	 %{name}
Version: 0.8
Release: 1
Source0: http://pypi.python.org/packages/source/c/cssselect/cssselect-%{version}.tar.gz
License: BSD
Group:	 Development/Python
Url:	 http://packages.python.org/cssselect/
BuildArch: noarch
BuildRequires:	python-setuptools

%description
cssselect parses CSS3 Selectors and translate them to XPath 1.0
expressions. Such expressions can be used in lxml or another XPath
engine to find the matching elements in an XML or HTML document.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean

%files
%doc AUTHORS CHANGES LICENSE README.rst
%py_puresitedir/%{module}*


%changelog
* Tue May 08 2012 Lev Givon <lev@mandriva.org> 0.6.1-1
+ Revision: 797547
- imported package python-cssselect


