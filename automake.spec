# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       automake
Summary:    A GNU tool for automatically creating Makefiles
Version:    1.11.1
Release:    3
Group:      Development/Tools
License:    GPLv2+ and GFDL and MIT
BuildArch:  noarch
URL:        http://www.gnu.org/software/automake/
Source0:    http://ftp.gnu.org/gnu/automake/automake-%{version}.tar.bz2
Source1:    filter-provides-automake.sh
Source2:    filter-requires-automake.sh
Source3:    automake.man
Source4:    aclocal.man
Source5:    automake-rpmlintrc
Source100:  automake.yaml
Requires:   autoconf >= 2.62
BuildRequires:  autoconf >= 2.62


%description
Automake is a tool for automatically generating `Makefile.in'
files compliant with the GNU Coding Standards.

You should install Automake if you are developing software and would
like to use its ability to automatically generate GNU standard
Makefiles. If you install Automake, you will also need to install
GNU's Autoconf package.




%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --docdir=%{_docdir}/%{name}-%{version}

make %{?jobs:-j%jobs}

# >> build post
mv -f NEWS NEWS_
iconv -f ISO_8859-15 -t UTF-8 NEWS_ -o NEWS
# << build post
%install
rm -rf %{buildroot}
# >> install pre
rm -rf ${RPM_BUILD_ROOT}

# << install pre
%make_install

# >> install post
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT/%{_mandir}/man1/automake.1
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT/%{_mandir}/man1/aclocal.1

# create this dir empty so we can own it
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/aclocal
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
# << install post






%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS README THANKS NEWS
%{_bindir}/*
%doc %{_infodir}/automake.info*.gz
%{_datadir}/automake-*
%{_datadir}/aclocal-*
%doc %{_mandir}/man1/*
%dir %{_datadir}/aclocal
# << files


