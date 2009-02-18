#
%define 	svn_rel	34
#
%define		rel 1
Summary:	Project to create Polish language data for Tesseract
Summary(pl.UTF-8):	Projekt tworzący dane języka polskiego dla Tesseracta
Name:		tesseract-polish
Version:	0
Release:	0.r%{svn_rel}.1
License:	Apache v2.0
Group:		Development/Tools
Source0:	%{name}-r%{svn_rel}.tar.bz2
# Source0-md5:	8045c487adbef13749cad69db02d5396
URL:		http://code.google.com/p/tesseract-polish/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project aims to develop high quality data files for Polish
language support for Tesseract OCR.

Included are the sources for sample documents, utilities to process
and prepare dictionary data for compilation into DAWG format etc.

%description -l pl.UTF-8
Ten projekt ma na celu opracowanie wysokiej jakości plików danych
języka Polskiego dla programu Tesseract OCR.

Projekt obejmuje źródła dokumentów użytych do treningu OCR-a,
narzędzie służące do przetwarzania danych słownikowych i przygotowania
ich do kompilacji do formatu DAWG itd.

%package -n tesseract-lang-pl
Summary:	Polish language data for Tesseract
Summary(pl.UTF-8):	Dane języka polskiego dla Tesseracta
Group:		Applications/Graphics

%description -n tesseract-lang-pl
This package contains the data files required to recognize Polish
language. This data comes from the tesseract-polish project. Source
files and utilities are available in the tesseract-polish package.

%description -n tesseract-lang-pl -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
polskiego. Dane pochodzą z projektu tesseract-polish. Pliki źródłowe i
narzędzia używane do ich przetwarzania dostępne są w pakiecie
tesseract-polish.

%prep
%setup -q -n %{name}-r%{svn_rel}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/tessdata,/usr/src/%{name}}
install tessdata/pol.* $RPM_BUILD_ROOT%{_datadir}/tessdata
cp -R tessdata_filelist src $RPM_BUILD_ROOT/usr/src/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ATTRIBUTIONS BUGS NOTICE  README
%dir /usr/src/%{name}
/usr/src/%{name}/tessdata_filelist
%dir /usr/src/%{name}/src
/usr/src/%{name}/src/dictionaries
/usr/src/%{name}/src/training_images
%dir /usr/src/%{name}/src/utils
/usr/src/%{name}/src/utils/*.pm
%attr(755,root,root) /usr/src/%{name}/src/utils/*.sh
%attr(755,root,root) /usr/src/%{name}/src/utils/*.pl

%files -n tesseract-lang-pl
%defattr(644,root,root,755)
%doc NOTICE
%{_datadir}/tessdata
