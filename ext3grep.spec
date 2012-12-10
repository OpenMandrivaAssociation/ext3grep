Name:		ext3grep
Version:	0.10.2
Release:	%mkrel 1
Summary:	Investigation and recovery tool for ext3 filesystem
Group:		File tools
License:	GPLv2+
URL:		http://code.google.com/p/ext3grep/
Source0:	http://ext3grep.googlecode.com/files/ext3grep-%version.tar.gz
BuildRequires:	ext2fs-devel
Patch0:		ext3grep-0.10.1-gcc44.patch
Patch1:		ext3grep-0.10.2-include-unistd_h-for-sysconf.patch
Patch2:		ext3grep-0.10.2-new-e2fsprogs.diff

%description
A tool to investigate an ext3 file system for deleted content and
possibly recover it.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
# http://code.google.com/p/ext3grep/issues/detail?id=14
export CXX=%{_bindir}/g++

%configure2_5x
%make

%install
# Builds twice unless setting it here as well:
export CXX=%{_bindir}/g++
%makeinstall_std

%files
%doc NEWS README
%{_bindir}/ext3grep
