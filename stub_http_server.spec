Name:    stub_http_server
Version: 0.1
Release: 1
Summary: stub_http_server
Group:   Development Tools
License: ASL 2.0
Source0: stub_http_server.service
Source1: stub_http_server.js
Requires: nodejs
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

# Use systemd for fedora >= 18, rhel >=7, SUSE >= 12 SP1 and openSUSE >= 42.1
%define use_systemd (0%{?fedora} && 0%{?fedora} >= 18) || (0%{?rhel} && 0%{?rhel} >= 7) || (!0%{?is_opensuse} && 0%{?suse_version} >=1210) || (0%{?is_opensuse} && 0%{?sle_version} >= 120100)


%description
stub_http_server

%install
%if %{use_systemd}
%{__mkdir} -p %{buildroot}%{_unitdir}
%{__install} -m644 %{SOURCE0} \
    %{buildroot}%{_unitdir}/%{name}.service
%endif
ls
mkdir -p %{buildroot}/var/lib/stub_http_server
ls
ls /builddir/build/BUILDROOT/stub_http_server-0.1-1.x86_64/var/lib/stub_http_server
install -m 0664 %{SOURCE1} %{buildroot}/var/lib/stub_http_server

%pre
/usr/bin/getent group stub_http_server > /dev/null || /usr/sbin/groupadd -r stub_http_server
/usr/bin/getent passwd stub_http_server > /dev/null || /usr/sbin/useradd -r -d /var/lib/stub_http_server/ -s /bin/bash -g stub_http_server stub_http_server

%post
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%preun
%if %use_systemd
/usr/bin/systemctl stop %{name}
%endif

%postun
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%files
%dir %attr(0775, victoriametrics, victoriametrics) /var/lib/stub_http_server/stub_http_server.js
%if %{use_systemd}
%{_unitdir}/%{name}.service
%endif
