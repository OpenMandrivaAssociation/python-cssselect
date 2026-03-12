%define module cssselect

Name:	 python-cssselect
Version:	1.4.0
Release:	1
License:	BSD
Summary:	Library for parsing CSS3 selectors and translating them to XPath 1.0
Group:	 	Development/Python
URL:		https://github.com/scrapy/cssselect
Source0:	https://github.com/scrapy/cssselect/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
Obsoletes: python2-%{module} < %{EVRD}

%description
cssselect parses CSS3 Selectors and translate them to XPath 1.0
expressions. Such expressions can be used in lxml or another XPath
engine to find the matching elements in an XML or HTML document.

%files
%doc AUTHORS CHANGES README.rst
%license LICENSE
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
