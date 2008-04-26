
Name:		ext3grep
Version:	0.6.0
Release:	%mkrel 1
Summary:	Investigation and recovery tool for ext3 filesystem
Group:		File tools
License:	GPLv2+
URL:		http://code.google.com/p/ext3grep/
Source:		http://ext3grep.googlecode.com/files/ext3grep-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	ext2fs-devel

%description
A tool to investigate an ext3 file system for deleted content and
possibly recover it.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS README
%{_bindir}/ext3grep
