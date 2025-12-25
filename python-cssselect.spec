%define	module	cssselect

Summary: Library for parsing CSS3 selectors and translating them to XPath 1.0
Name:	 python-%{module}
Version:	1.3.0
Release:	1
Source0: https://github.com/scrapy/cssselect/archive/v%{version}/%{name}-%{version}.tar.gz
License: BSD
Group:	 Development/Python
Url:	 https://packages.python.org/cssselect/
BuildArch: noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
Obsoletes: python2-%{module} < %{EVRD}

%description
cssselect parses CSS3 Selectors and translate them to XPath 1.0
expressions. Such expressions can be used in lxml or another XPath
engine to find the matching elements in an XML or HTML document.

%files
%doc AUTHORS CHANGES LICENSE README.rst
%{py_puresitedir}/%{module}*
