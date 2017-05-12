%define	module	cssselect

Summary: Library for parsing CSS3 selectors and translating them to XPath 1.0
Name:	 python-%{module}
Version: 1.0.1
Release: 1
Source0: https://github.com/scrapy/cssselect/archive/v%{version}.tar.gz
License: BSD
Group:	 Development/Python
Url:	 http://packages.python.org/cssselect/
BuildArch: noarch
BuildRequires:	python-setuptools

%description
cssselect parses CSS3 Selectors and translate them to XPath 1.0
expressions. Such expressions can be used in lxml or another XPath
engine to find the matching elements in an XML or HTML document.

%package -n python2-%{module}
Summary:       Library for parsing CSS3 selectors and translating them to XPath 1.0
Group:          Development/Python

%prep
%setup -q -n %{module}-%{version}

pushd ..
cp -rp %{module}-%{version} %{py2dir}


%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

pushd %py2dir
%__python2 setup.py install --root=%{buildroot}

%files
%doc AUTHORS CHANGES LICENSE README.rst
%{py_puresitedir}/%{module}*

%files -n python2-%{module}
%doc AUTHORS CHANGES LICENSE README.rst
%{py2_puresitedir}/%{module}*
