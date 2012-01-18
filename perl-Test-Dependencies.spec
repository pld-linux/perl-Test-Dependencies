#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Dependencies
Summary:	Test::Dependencies - Ensure that your Makefile.PL specifies all module dependencies
Summary(pl.UTF-8):	Test::Dependencies - sprawdzanie czy Makefile.PL określa wszystkie zależności
Name:		perl-Test-Dependencies
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c6a2296a4dd1f023cb396832c4c2535c
URL:		http://search.cpan.org/dist/Test-Dependencies/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(B::PerlReq)
BuildRequires:	perl(PerlReq::Utils)
BuildRequires:	perl(Test::Builder::Module)
BuildRequires:	perl(Test::Builder::Tester) >= 0.64
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-IPC-Cmd
BuildRequires:	perl-Module-CoreList
BuildRequires:	perl-Pod-Strip
BuildRequires:	perl-YAML
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Makes sure that all of the modules that are 'use'd are listed in the
Makefile.PL as dependencies.

%description -l pl.UTF-8
Ten moduł sprawdza, czy wszystkie moduły, do których dany pakiet
odwołuje się przez "use", są wymienione jako zależności w pliku
Makefile.PL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/Dependencies
%{_mandir}/man3/*
