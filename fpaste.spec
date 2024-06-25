Name:           fpaste
Version:	0.4.5.1
Release:	1
Summary:        A simple tool for pasting info onto fpaste.org
License:        GPLv3+
Group:          Text tools
URL:            https://pagure.io/fpaste
Source0:        https://pagure.io/releases/fpaste/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
It is often useful to be able to easily paste text to the Fedora
Pastebin at http://fpaste.org and this simple script will do that
and return the resulting URL so that people may examine the
output. This can hopefully help folks who are for some reason
stuck without X, working remotely, or any other reason they may
be unable to paste something into the pastebin.

%prep
%setup -q
%autopatch -p1

%build
#nothing required

%install
%make_install

%files
%doc CHANGELOG README.rst
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

