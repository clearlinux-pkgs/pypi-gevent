#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-gevent
Version  : 21.12.0
Release  : 73
URL      : https://files.pythonhosted.org/packages/c8/18/631398e45c109987f2d8e57f3adda161cc5ff2bd8738ca830c3a2dd41a85/gevent-21.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c8/18/631398e45c109987f2d8e57f3adda161cc5ff2bd8738ca830c3a2dd41a85/gevent-21.12.0.tar.gz
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
BuildRequires : pypi(wheel)
BuildRequires : pypi(zope.event)
BuildRequires : pypi(zope.interface)
BuildRequires : pypi-cython

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
%setup -q -n gevent-21.12.0
cd %{_builddir}/gevent-21.12.0
pushd ..
cp -a gevent-21.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656403743
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-gevent
cp %{_builddir}/gevent-21.12.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gevent/e390b2ea7c66d8859ed575dcad84522b804123ae
cp %{_builddir}/gevent-21.12.0/NOTICE %{buildroot}/usr/share/package-licenses/pypi-gevent/c3c1f290cd381675b69efce2eee3c2ce03d398d8
cp %{_builddir}/gevent-21.12.0/deps/c-ares/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-gevent/e9c597f9b6cf935773ee731d4170b0c2ba142dbb
cp %{_builddir}/gevent-21.12.0/deps/libev/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gevent/10e633ee2e9f8a961554d0d579f03a1d0755ff3b
cp %{_builddir}/gevent-21.12.0/deps/libuv/LICENSE %{buildroot}/usr/share/package-licenses/pypi-gevent/848f7398f89046426a7ba23cb56cd3c93c030c64
cp %{_builddir}/gevent-21.12.0/deps/libuv/LICENSE-docs %{buildroot}/usr/share/package-licenses/pypi-gevent/1167f0e28fe2db01e38e883aaf1e749fb09f9ceb
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
/usr/share/package-licenses/pypi-gevent/848f7398f89046426a7ba23cb56cd3c93c030c64
/usr/share/package-licenses/pypi-gevent/c3c1f290cd381675b69efce2eee3c2ce03d398d8
/usr/share/package-licenses/pypi-gevent/e390b2ea7c66d8859ed575dcad84522b804123ae
/usr/share/package-licenses/pypi-gevent/e9c597f9b6cf935773ee731d4170b0c2ba142dbb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
