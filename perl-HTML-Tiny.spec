#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	HTML
%define	pnam	Tiny
Summary:	HTML::Tiny - Lightweight, dependency free HTML/XML generation
#Summary(pl.UTF-8):	
Name:		perl-HTML-Tiny
Version:	1.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f683dbc8e4570ba08d0fcb1f50c1b6dc
URL:		http://search.cpan.org/dist/HTML-Tiny/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Tiny is a simple, dependency free module for generating
HTML (and XML). It concentrates on generating syntactically correct
XHTML using a simple Perl notation.

# %description -l pl.UTF-8
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

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/HTML/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
