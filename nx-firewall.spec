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
%autopatch -p1

%build
export CC=gcc
export CXX=g++
%cmake  -DCMAKE_BUILD_TYPE=Release \
        -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
        
%make_build

%install
%make_install -C build


%files
