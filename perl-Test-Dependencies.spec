#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Dependencies
Summary:	Test::Dependencies - Ensure that your Makefile.PL specifies all module dependencies
#Summary(pl):	
Name:		perl-Test-Dependencies
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/Z/ZE/ZEV/Test-Dependencies-0.11.tar.gz
# Source0-md5:	f092f03973d5f5d1f8ef0e730f957771
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(B::PerlReq)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(IPC::Cmd)
BuildRequires:	perl(Module::CoreList)
BuildRequires:	perl(PerlReq::Utils)
BuildRequires:	perl(Pod::Strip)
BuildRequires:	perl(Test::Builder::Module)
BuildRequires:	perl(YAML)
BuildRequires:	perl(Test::Builder::Tester) >= 0.64
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Makes sure that all of the modules that are 'use'd are listed in the
Makefile.PL as dependencies.

# %description -l pl
# TODO

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
