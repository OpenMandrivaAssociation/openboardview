Summary: PCB schematics viewer
Name:    openboardview
Version: 9.95.1
Release: 1
License: MIT
Group:   Applications/Engineering
Url:     https://openboardview.org
Source:  %{name}-%{version}.tar.zst
Patch0:  no-bundled-libraries-that-we-provide-ourselves.patch
Patch1:  fix-imgui.h-include.patch

BuildRequires: git-core
BuildRequires: python
BuildRequires: cmake(glad)
BuildRequires: cmake(SDL2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(stb)
BuildRequires: pkgconfig(zlib)

Provides: openboardview = %{version}-%{release}

%description
A modern open-source PCB schematics viewer that supports popular formats.

%prep
%autosetup -p 0

%build
%cmake -G Ninja \
       -DCMAKE_BUILD_TYPE=Release

%ninja_build

%install
%ninja_install -C build

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_iconsdir}/hicolor/*/apps/%{name}*
