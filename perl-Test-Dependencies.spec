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
Version:	0.23
Release:	2
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	49c7be85e155591fede4fb818462665f
Patch0:		%{name}-undef.patch
URL:		http://search.cpan.org/dist/Test-Dependencies/
BuildRequires:	perl-CPAN-Meta-Requirements >= 2.120_620
BuildRequires:	perl-Pod-Strip
BuildRequires:	perl-devel >= 1:5.10.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::Builder::Module)
BuildRequires:	perl-File-Find-Rule-Perl
BuildRequires:	perl-IPC-Cmd
BuildRequires:	perl-Module-CoreList
BuildRequires:	perl-Test-Builder-Tester >= 0.64
BuildRequires:	perl-Test-Needs
BuildRequires:	perl-Test-Simple >= 1.30
BuildRequires:	perl-YAML
BuildRequires:	perl-rpm-build-perl
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
%patch0 -p1

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
%{perl_vendorlib}/Test/Dependencies.pm
%{perl_vendorlib}/Test/Dependencies
%{_mandir}/man3/Test::Dependencies*.3pm*
