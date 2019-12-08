%define _disable_lto 1

Name:           nx-firewall
Version:        0.4.1
Release:        0.git.2019.11.18
Summary:        Plasma 5 Firewall KCM
Group:          System/Base
License:        GPLv3+
URL:            https://github.com/nx-desktop/nx-firewall
#Source:         https://github.com/nx-desktop/nx-firewall/archive/%{version}/%{name}-%{version}.tar.gz
Source0:        %{name}-master-2019.11.18.zip
Patch0:         nx-firewall-werror.patch

BuildRequires:  cmake
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5PlasmaQuick)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  python-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5X11Extras)


%description
nx-firewall is a small and easy to use KCM Firewall for Plasma 5.

%prep
%setup -qn %{name}-master
%autopatch -p0

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=deprecated-declarations"
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=inconsistent-missing-override"

#export CC=gcc
#export CXX=g++
%cmake  -DCMAKE_BUILD_TYPE=Release \
        -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
        
%make_build

%install
%make_install -C build


%files
%{_libdir}/libexec/__pycache__/nomad_ufw_plugin_helper.cpython-37.pyc
%{_libdir}/libexec/kauth/nomad_ufw_plugin_helper
%{_libdir}/libexec/kauth/nxos_netstat_helper
%{_libdir}/libexec/nomad_ufw_plugin_helper.py
%{_libdir}/qt5/plugins/kcms/org.nxos.firewall.so
%{_libdir}/qt5/qml/org/nomad/netstat/libnomad_netstat_plugin.so
%{_libdir}/qt5/qml/org/nomad/netstat/qmldir
%{_libdir}/qt5/qml/org/nomad/ufw/libnomad_ufw_plugin.so
%{_libdir}/qt5/qml/org/nomad/ufw/qmldir
%{_datadir}/dbus-1/system-services/org.nomad.ufw.service
%{_datadir}/dbus-1/system-services/org.nxos.netstat.service
%{_datadir}/dbus-1/system.d/org.nomad.ufw.conf
%{_datadir}/dbus-1/system.d/org.nxos.netstat.conf
%{_datadir}/kcm_ufw/defaults
%{_datadir}/kpackage/kcms/org.nxos.firewall/contents/ui/ConnectionItemDelegate.qml
%{_datadir}/kpackage/kcms/org.nxos.firewall/contents/ui/ConnectionsView.qml
%{_datadir}/kpackage/kcms/org.nxos.firewall/contents/ui/GlobalRules.qml
%{_datadir}/kpackage/kcms/org.nxos.firewall/contents/ui/LogItemDelegate.qml
%{_datadir}/kpackage/kcms/org.nxos.firewall/contents/ui/LogsView.qml
%{_datadir}/kpackage/kcms/org.nxos.firewall/contents/ui/RuleEdit.qml
%{_datadir}/kpackage/kcms/org.nxos.firewall/contents/ui/RuleListItem.qml
%{_datadir}/kpackage/kcms/org.nxos.firewall/contents/ui/RulesView.qml
%{_datadir}/kpackage/kcms/org.nxos.firewall/contents/ui/main.qml
%{_datadir}/kpackage/kcms/org.nxos.firewall/metadata.desktop
%{_datadir}/kpackage/kcms/org.nxos.firewall/metadata.json
%{_datadir}/kservices5/org_nxos_firewall.desktop
%{_datadir}/metainfo/org.nxos.firewall.appdata.xml
%{_datadir}/polkit-1/actions/org.nomad.ufw.policy
%{_datadir}/polkit-1/actions/org.nxos.netstat.policy
