%global pixmaptarget %{_datadir}/lorax/product/usr/share/anaconda/pixmaps
%global pixmapsource %{_datadir}/anaconda/pixmaps/workstation

Name:           korora-productimg-workstation
Version:        23
Release:        1%{?dist}
Summary:        Installer branding and configuration for Korora

# Copyright and related rights waived via CC0
# http://creativecommons.org/publicdomain/zero/1.0/
License:        CC0

Source0:        korora-workstation.css
Source1:        korora-workstation.py

BuildRequires:  cpio, findutils, xz
BuildRequires:  python3-devel

Provides:       lorax-product-workstation
Provides:       fedora-product-workstation
Obsoletes:      fedora-product-workstation
Conflicts:      fedora-productimg-cloud, fedora-productimg-server

%description
This package contains differentiated branding and configuration for Korora 
for use in a product.img file for Anaconda, the Korora installer. It is 
not useful on an installed system.

%prep

%build

%install

install -m 755 -d %{buildroot}%{pixmaptarget}

install -m 644 %{SOURCE0} %{buildroot}%{pixmaptarget}/../

mkdir -p %{buildroot}%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses

ln -sf %{pixmapsource}/sidebar-bg.png %{buildroot}%{pixmaptarget}
ln -sf %{pixmapsource}/topbar-bg.png %{buildroot}%{pixmaptarget}

# note filename change with this one
ln -sf %{pixmapsource}/sidebar-logo.png %{buildroot}%{pixmaptarget}/sidebar-logo_flavor.png

install -m 755 -d %{buildroot}%{_datadir}/korora-productimg

pushd %{buildroot}%{_datadir}/lorax/product/
find %{buildroot}%{_datadir}/lorax/product/ -depth -printf '%%P\0' | \
   cpio --null --quiet -H newc -o | \
   xz -9 > \
   %{buildroot}%{_datadir}/korora-productimg/product.img
popd


%files
%dir %{_datadir}/lorax/product/usr/share/anaconda
%{_datadir}/lorax/product/usr/share/anaconda/korora-workstation.css
%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses/korora-workstation.py
%{_datadir}/lorax/product/%{python3_sitearch}/pyanaconda/installclasses/__pycache__/*
%dir %{_datadir}/lorax/product/usr/share
%dir %{_datadir}/lorax/product/usr
%dir %{pixmaptarget}
%{pixmaptarget}/*.png
%dir %{_datadir}/korora-productimg
%{_datadir}/korora-productimg/product.img

%changelog
* Mon Oct 19 2015 Chris Smart <csmart@kororaproject.org> - 23-1
- Korora version of workstation, required to fix Anaconda missing buttons.

