Name:		texlive-babel-romansh
Version:	30286
Release:	2
Summary:	Babel/Polyglossia support for the Romansh language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/romansh
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-romansh.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-romansh.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-romansh.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a language description file that enables
support of Romansh either with babel or with polyglossia.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-romansh/romansh.ldf
%doc %{_texmfdistdir}/doc/generic/babel-romansh/romansh.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-romansh/romansh.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
