%global debug_package %{nil}

Name: python-requests-unixsocket
Epoch: 100
Version: 0.1.5
Release: 1%{?dist}
BuildArch: noarch
Summary: UNIX domain socket backend for python-requests
License: Apache-2.0
URL: https://github.com/msabramo/requests-unixsocket/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
With this module, python-requests is enhanced by the ability to talk
HTTP via a UNIX domain socket.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-requests-unixsocket
Summary: UNIX domain socket backend for python-requests
Requires: python3
Requires: python3-requests
Requires: python3-urllib3
Provides: python3-requests-unixsocket = %{epoch}:%{version}-%{release}
Provides: python3dist(requests-unixsocket) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-requests-unixsocket = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(requests-unixsocket) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-requests-unixsocket = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(requests-unixsocket) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-requests-unixsocket
With this module, python-requests is enhanced by the ability to talk
HTTP via a UNIX domain socket.

%files -n python%{python3_version_nodots}-requests-unixsocket
%license LICENSE
%{python3_sitelib}/requests_unixsocket*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-requests-unixsocket
Summary: UNIX domain socket backend for python-requests
Requires: python3
Requires: python3-requests
Requires: python3-urllib3
Provides: python3-requests-unixsocket = %{epoch}:%{version}-%{release}
Provides: python3dist(requests-unixsocket) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-requests-unixsocket = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(requests-unixsocket) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-requests-unixsocket = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(requests-unixsocket) = %{epoch}:%{version}-%{release}

%description -n python3-requests-unixsocket
With this module, python-requests is enhanced by the ability to talk
HTTP via a UNIX domain socket.

%files -n python3-requests-unixsocket
%license LICENSE
%{python3_sitelib}/requests_unixsocket*
%endif

%changelog
