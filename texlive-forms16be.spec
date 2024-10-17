Name:		texlive-forms16be
Version:	51305
Release:	2
Summary:	Initialize form properties using big-endian encoding
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/forms16be
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forms16be.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forms16be.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forms16be.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides support for UTF-16BE Unicode character
encoding (called a big-endian character string) for the text
string type (PDF Reference, version 1.7, beginning on page
158). Text strings are used in "text annotations, bookmark
names, article threads, document information, and so forth" (to
partially quote page 158). The particular application is to set
property values of form fields, at least those properties that
take the text strings as its value. The package contains
support for Basic Latin plus the ability to enter any unicode
character using the notation \uXXXX, where XXXX are four hex
digits. The Package works for dvips/Distiller, pdfLaTeX,
LuaLaTeX, and XeLaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/forms16be
%{_texmfdistdir}/tex/latex/forms16be
%doc %{_texmfdistdir}/doc/latex/forms16be

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
