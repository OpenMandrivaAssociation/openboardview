%global realname OpenBoardView
%global upstream OpenBoardView
%global gitbase  https://github.com

Summary: View .brd files
Name:    openboardview
Version: 9.0.3
Release: %mkrel 1
License: MIT
Group:   Applications/Engineering
Url:     https://openboardview.org
Source0: %{gitbase}/%{upstream}/%{realname}/archive/refs/tags/%{version}.tar.gz
Patch0:  build-system-Allow-using-stb-from-the-system.patch

BuildRequires: git-core
BuildRequires: python
BuildRequires: cmake(SDL2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(stb)
BuildRequires: pkgconfig(zlib)

Provides: openboardview = %{version}-%{release}

%description
Linux SDL/ImGui edition software for viewing .brd files,
intended as a drop-in replacement for the "Test_Link" software and "Landrex".

%prep
%autosetup -p 1 -n %{realname}-%{version}

git submodule update --init --recursive

%build
%cmake

%make_build

%install
%make_install -C build
