#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-gevent
Version  : 22.10.2
Release  : 79
URL      : https://files.pythonhosted.org/packages/9f/4a/e9e57cb9495f0c7943b1d5965c4bdd0d78bc4a433a7c96ee034b16c01520/gevent-22.10.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9f/4a/e9e57cb9495f0c7943b1d5965c4bdd0d78bc4a433a7c96ee034b16c01520/gevent-22.10.2.tar.gz
Summary  : Coroutine-based network library
Group    : Development/Tools
License  : BSD-2-Clause CC-BY-4.0 MIT Python-2.0
Requires: pypi-gevent-filemap = %{version}-%{release}
Requires: pypi-gevent-lib = %{version}-%{release}
Requires: pypi-gevent-license = %{version}-%{release}
Requires: pypi-gevent-python = %{version}-%{release}
Requires: pypi-gevent-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cffi)
BuildRequires : pypi(cython)
BuildRequires : pypi(greenlet)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(zope.event)
BuildRequires : pypi(zope.interface)
BuildRequires : pypi-cython
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
An example of AJAX chat taken from Tornado demos and converted to use django and gevent.

%package filemap
Summary: filemap components for the pypi-gevent package.
Group: Default

%description filemap
filemap components for the pypi-gevent package.


%package lib
Summary: lib components for the pypi-gevent package.
Group: Libraries
Requires: pypi-gevent-license = %{version}-%{release}
Requires: pypi-gevent-filemap = %{version}-%{release}

%description lib
lib components for the pypi-gevent package.


%package license
Summary: license components for the pypi-gevent package.
Group: Default

%description license
license components for the pypi-gevent package.


%package python
Summary: python components for the pypi-gevent package.
Group: Default
Requires: pypi-gevent-python3 = %{version}-%{release}

%description python
python components for the pypi-gevent package.


%package python3
Summary: python3 components for the pypi-gevent package.
Group: Default
Requires: pypi-gevent-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(gevent)
Requires: pypi(greenlet)
Requires: pypi(setuptools)
Requires: pypi(zope.event)
Requires: pypi(zope.interface)

%description python3
python3 components for the pypi-gevent package.


%prep
%setup -q -n gevent-22.10.2
cd %{_builddir}/gevent-22.10.2
pushd ..
cp -a gevent-22.10.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672274539
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-gevent
cp %{_builddir}/gevent-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gevent/e390b2ea7c66d8859ed575dcad84522b804123ae || :
cp %{_builddir}/gevent-%{version}/NOTICE %{buildroot}/usr/share/package-licenses/pypi-gevent/c3c1f290cd381675b69efce2eee3c2ce03d398d8 || :
cp %{_builddir}/gevent-%{version}/deps/c-ares/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-gevent/e9c597f9b6cf935773ee731d4170b0c2ba142dbb || :
cp %{_builddir}/gevent-%{version}/deps/libev/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gevent/10e633ee2e9f8a961554d0d579f03a1d0755ff3b || :
cp %{_builddir}/gevent-%{version}/deps/libuv/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gevent/995532b42e0ad16d5ee90d1538f3d74a91fa76e6 || :
cp %{_builddir}/gevent-%{version}/deps/libuv/LICENSE-docs %{buildroot}/usr/share/package-licenses/pypi-gevent/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-gevent

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-gevent/10e633ee2e9f8a961554d0d579f03a1d0755ff3b
/usr/share/package-licenses/pypi-gevent/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb
/usr/share/package-licenses/pypi-gevent/995532b42e0ad16d5ee90d1538f3d74a91fa76e6
/usr/share/package-licenses/pypi-gevent/c3c1f290cd381675b69efce2eee3c2ce03d398d8
/usr/share/package-licenses/pypi-gevent/e390b2ea7c66d8859ed575dcad84522b804123ae
/usr/share/package-licenses/pypi-gevent/e9c597f9b6cf935773ee731d4170b0c2ba142dbb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
