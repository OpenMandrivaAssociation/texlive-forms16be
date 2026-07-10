%global tl_name forms16be
%global tl_revision 51305

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Initialize form properties using big-endian encoding
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/forms16be
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/forms16be.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/forms16be.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/forms16be.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides support for UTF-16BE Unicode character encoding
(called a big-endian character string) for the text string type (PDF
Reference, version 1.7, beginning on page 158). Text strings are used in
"text annotations, bookmark names, article threads, document
information, and so forth" (to partially quote page 158). The particular
application is to set property values of form fields, at least those
properties that take the text strings as its value. The package contains
support for Basic Latin plus the ability to enter any unicode character
using the notation \uXXXX, where XXXX are four hex digits. The Package
works for dvips/Distiller, pdfLaTeX, LuaLaTeX, and XeLaTeX.

