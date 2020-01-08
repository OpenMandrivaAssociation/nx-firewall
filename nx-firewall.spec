%define snap 2019.11.18

Name:		nx-firewall
Version:	0.4.1
Release:	3.git.%{snap}.2
Summary:	Plasma 5 Firewall KCM
Group:		System/Base
License:	GPLv3+
URL:		https://github.com/nx-desktop/nx-firewall
#Source:	https://github.com/nx-desktop/nx-firewall/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	%{name}-master-%{snap}.zip
Patch0:		nx-firewall-werror.patch
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5X11Extras)
Requires:	ufw

%description
nx-firewall is a small and easy to use KCM Firewall for Plasma 5.

%prep
%setup -qn %{name}-master
%autopatch -p0

%build
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
export CFLAGS="%{optflags} -Wno-error=inconsistent-missing-override"

%cmake_kde5
%make_build

%install
%make_install -C build

%files
%{_libdir}/libexec/__pycache__/*.pyc
%{_libdir}/libexec/kauth/nomad_ufw_plugin_helper
%{_libdir}/libexec/kauth/nxos_netstat_helper
%{_libdir}/libexec/nomad_ufw_plugin_helper.py
%{_libdir}/qt5/plugins/kcms/org.nxos.firewall.so
%dir %{_libdir}/qt5/qml/org/nomad
%{_libdir}/qt5/qml/org/nomad/*
%{_datadir}/dbus-1/system-services/org.nomad.ufw.service
%{_datadir}/dbus-1/system-services/org.nxos.netstat.service
%{_datadir}/dbus-1/system.d/org.nomad.ufw.conf
%{_datadir}/dbus-1/system.d/org.nxos.netstat.conf
%{_datadir}/kcm_ufw/defaults
%dir %{_datadir}/kpackage/kcms/org.nxos.firewall
%{_datadir}/kpackage/kcms/org.nxos.firewall/*
%{_datadir}/kservices5/org_nxos_firewall.desktop
%{_datadir}/metainfo/org.nxos.firewall.appdata.xml
%{_datadir}/polkit-1/actions/org.nomad.ufw.policy
%{_datadir}/polkit-1/actions/org.nxos.netstat.policy
