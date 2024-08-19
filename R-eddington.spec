#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: f35655a
#
Name     : R-eddington
Version  : 4.2.0
Release  : 27
URL      : https://cran.r-project.org/src/contrib/eddington_4.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/eddington_4.2.0.tar.gz
Summary  : Compute a Cyclist's Eddington Number
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-eddington-lib = %{version}-%{release}
Requires: R-R6
Requires: R-Rcpp
Requires: R-xml2
BuildRequires : R-R6
BuildRequires : R-Rcpp
BuildRequires : R-xml2
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
computing cumulative E over a vector. A cyclist's Eddington number

%package lib
Summary: lib components for the R-eddington package.
Group: Libraries

%description lib
lib components for the R-eddington package.


%prep
%setup -q -n eddington
pushd ..
cp -a eddington buildavx2
popd
pushd ..
cp -a eddington buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724082529

%install
export SOURCE_DATE_EPOCH=1724082529
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/eddington/DESCRIPTION
/usr/lib64/R/library/eddington/INDEX
/usr/lib64/R/library/eddington/Meta/Rd.rds
/usr/lib64/R/library/eddington/Meta/data.rds
/usr/lib64/R/library/eddington/Meta/features.rds
/usr/lib64/R/library/eddington/Meta/hsearch.rds
/usr/lib64/R/library/eddington/Meta/links.rds
/usr/lib64/R/library/eddington/Meta/nsInfo.rds
/usr/lib64/R/library/eddington/Meta/package.rds
/usr/lib64/R/library/eddington/Meta/vignette.rds
/usr/lib64/R/library/eddington/NAMESPACE
/usr/lib64/R/library/eddington/NEWS.md
/usr/lib64/R/library/eddington/R/eddington
/usr/lib64/R/library/eddington/R/eddington.rdb
/usr/lib64/R/library/eddington/R/eddington.rdx
/usr/lib64/R/library/eddington/R/sysdata.rdb
/usr/lib64/R/library/eddington/R/sysdata.rdx
/usr/lib64/R/library/eddington/data/Rdata.rdb
/usr/lib64/R/library/eddington/data/Rdata.rds
/usr/lib64/R/library/eddington/data/Rdata.rdx
/usr/lib64/R/library/eddington/doc/eddington.R
/usr/lib64/R/library/eddington/doc/eddington.Rmd
/usr/lib64/R/library/eddington/doc/eddington.html
/usr/lib64/R/library/eddington/doc/index.html
/usr/lib64/R/library/eddington/help/AnIndex
/usr/lib64/R/library/eddington/help/aliases.rds
/usr/lib64/R/library/eddington/help/eddington.rdb
/usr/lib64/R/library/eddington/help/eddington.rdx
/usr/lib64/R/library/eddington/help/paths.rds
/usr/lib64/R/library/eddington/html/00Index.html
/usr/lib64/R/library/eddington/html/R.css
/usr/lib64/R/library/eddington/include/eddington.h
/usr/lib64/R/library/eddington/include/eddington_RcppExports.h
/usr/lib64/R/library/eddington/tests/testthat.R
/usr/lib64/R/library/eddington/tests/testthat/base-case.gpx
/usr/lib64/R/library/eddington/tests/testthat/multi-trkseg.gpx
/usr/lib64/R/library/eddington/tests/testthat/no-time-nodes.gpx
/usr/lib64/R/library/eddington/tests/testthat/no-trkseg.gpx
/usr/lib64/R/library/eddington/tests/testthat/one-node-trkseg.gpx
/usr/lib64/R/library/eddington/tests/testthat/refdata.rds
/usr/lib64/R/library/eddington/tests/testthat/simdata.rds
/usr/lib64/R/library/eddington/tests/testthat/test-gpx.r
/usr/lib64/R/library/eddington/tests/testthat/test-package.r
/usr/lib64/R/library/eddington/tests/testthat/zero-node-trkseg.gpx

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/eddington/libs/eddington.so
/V4/usr/lib64/R/library/eddington/libs/eddington.so
/usr/lib64/R/library/eddington/libs/eddington.so
