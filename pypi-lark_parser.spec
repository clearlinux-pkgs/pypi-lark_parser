#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-lark_parser
Version  : 0.12.0
Release  : 56
URL      : https://files.pythonhosted.org/packages/5a/ee/fd1192d7724419ddfe15b6f17d1c8742800d4de917c0adac3b6aaf22e921/lark-parser-0.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/ee/fd1192d7724419ddfe15b6f17d1c8742800d4de917c0adac3b6aaf22e921/lark-parser-0.12.0.tar.gz
Summary  : a modern parsing library
Group    : Development/Tools
License  : MIT
Requires: pypi-lark_parser-license = %{version}-%{release}
Requires: pypi-lark_parser-python = %{version}-%{release}
Requires: pypi-lark_parser-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Lark is a modern general-purpose parsing library for Python.
        
        With Lark, you can parse any context-free grammar, efficiently, with very little code.

%package license
Summary: license components for the pypi-lark_parser package.
Group: Default

%description license
license components for the pypi-lark_parser package.


%package python
Summary: python components for the pypi-lark_parser package.
Group: Default
Requires: pypi-lark_parser-python3 = %{version}-%{release}

%description python
python components for the pypi-lark_parser package.


%package python3
Summary: python3 components for the pypi-lark_parser package.
Group: Default
Requires: python3-core
Provides: pypi(lark_parser)

%description python3
python3 components for the pypi-lark_parser package.


%prep
%setup -q -n lark-parser-0.12.0
cd %{_builddir}/lark-parser-0.12.0
pushd ..
cp -a lark-parser-0.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672287357
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-lark_parser
cp %{_builddir}/lark-parser-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-lark_parser/af7225973c108376de2c312098b16c5a7a8828e6 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-lark_parser/af7225973c108376de2c312098b16c5a7a8828e6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
