# Conditional build:
%bcond_without ssl    Build without support for SSL encryption.
%bcond_without sasl   Build without Cyrus SASL authentication module.
%bcond_without perl   Build without Perl scripting module.
%bcond_without ipv6   Build without IPv6 connection support.
%bcond_with debug     Build debugging binaries.
Summary:	An advanced IRC bouncer
Name:		znc
Version:	0.052
Release:	0.1
License:	GPL v2
Group:		Daemons
URL:		http://znc.sf.net/
Source0:	http://dl.sourceforge.net/znc/%{name}-%{version}.tar.gz
# Source0-md5:	726046e3b44d811ededf4e850b5e0f06
Source1:	%{name}-crox-svn-admin.cpp
Source2:	%{name}-crox-svn-antiidle.cpp
Source3:	%{name}-crox-svn-fish.cpp
Source4:	%{name}-crox-svn-statupdate.cpp
Source5:	%{name}-cnu-log.cpp
Patch0:		%{name}-0.052-add_denysetvhost2.diff
%{?with_sasl:BuildRequires: cyrus-sasl-devel}
BuildRequires:	libstdc++-devel
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.8}
%{?with_perl:BuildRequires: perl-base}
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZNC is an IRC bounce with many advanced features like detaching,
multiple users, per channel playback buffer, SSL, IPv6, transparent
DCC bouncing, Perl and C++ module support to name a few.

%package module-admin
Summary:	znc admin global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-admin
A global module for the znc IRC bouncer. Allows you to add/remove/edit
users and settings on the fly via IRC messages.

%package module-imapauth
Summary:	znc imapauth global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-imapauth
A global module for the znc IRC bouncer. Allows users to authenticate
via IMAP.

%package module-modperl
Summary:	znc modperl global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-modperl
A global module for the znc IRC bouncer. Loads perl scripts as ZNC
modules.

%package module-partyline
Summary:	znc partyline global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-partyline
A global module for the znc IRC bouncer. Allows ZNC users to join
internal channels and query other ZNC users on the same ZNC.

%package module-saslauth
Summary:	znc saslauth global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-saslauth
A global module for the znc IRC bouncer. Allow users to authenticate
via SASL.

%package module-webadmin
Summary:	znc webadmin global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-webadmin
A global module for the znc IRC bouncer. Allows you to add/remove/edit
users and settings on the fly via a web browser.

%package module-antiidle
Summary:	znc antiidle user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-antiidle
A user module for the znc IRC bouncer. Hides your idle time.

%package module-autoattach
Summary:	znc autoattach user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-autoattach
A user module for the znc IRC bouncer. Reattaches you to channels on
activity.

%package module-autoop
Summary:	znc autoop user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-autoop
A user module for the znc IRC bouncer. Auto op the good guys.

%package module-away
Summary:	znc away user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-away
A user module for the znc IRC bouncer. Stores messages while away,
also auto away.

%package module-awaynick
Summary:	znc awaynick user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-awaynick
A user module for the znc IRC bouncer. Change your nick while you are
away.

%package module-chansaver
Summary:	znc chansaver user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-chansaver
A user module for the znc IRC bouncer. Keeping config up to date when
user joins and parts.

%package module-crypt
Summary:	znc crypt user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-crypt
A user module for the znc IRC bouncer. Encryption for channel/private
messages.

%package module-email
Summary:	znc email user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-email
A user module for the znc IRC bouncer. Monitors email activity on
local disk /var/mail/user.

%package module-fish
Summary:	znc fish user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-fish
A user module for the znc IRC bouncer. Adds the ability to encrypt all
your outgoing messages with the FiSH blowfish block-cipher. This way
you can do the decryption/encryption on the bouncer instead of your
IRC client.

%package module-kickrejoin
Summary:	znc kickrejoin user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-kickrejoin
A user module for the znc IRC bouncer. An Autorejoin module. Allows
you to rejoin a channel (after a delay) when kicked.

%package module-log
Summary:	znc log user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-log
A user module for the znc IRC bouncer. Log conversations to file.

%package module-nickserv
Summary:	znc nickserv user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-nickserv
A user module for the znc IRC bouncer. Auths you with NickServ.

%package module-perform
Summary:	znc perform user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-perform
A user module for the znc IRC bouncer. Performs commands on connect.

%package module-raw
Summary:	znc raw user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-raw
A user module for the znc IRC bouncer. View all of the raw traffic.

%package module-savebuff
Summary:	znc savebuff user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-savebuff
A user module for the znc IRC bouncer. Saves your channel buffers into
an encrypted file so they can survive restarts and reboots.

%package module-schat
Summary:	znc schat user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-schat
A user module for the znc IRC bouncer. SSL (encrypted) DCC chats.

%package module-shell
Summary:	znc shell user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-shell
A user module for the znc IRC bouncer. Have your unix shell in a query
window right inside of your IRC client.

%package module-statupdate
Summary:	znc statupdate user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-statupdate
A user module for the znc IRC bouncer. StatUpdate writes users online
status into a text file.

%package module-stickychan
Summary:	znc stickychan user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-stickychan
A user module for the znc IRC bouncer. Keeps you sticked to specific
channels.

%package module-watch
Summary:	znc watch user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-watch
A user module for the znc IRC bouncer. Monitor activity for specific
text patterns from specific users and have the text sent to a special
query window.

%package devel
Summary:	Development files needed to compile znc modules
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
All includes and program files you need to compile your own znc
modules.

%prep
%setup -q
%patch0 -p1
cp %{SOURCE1} modules/admin.cpp
cp %{SOURCE2} modules/antiidle.cpp
cp %{SOURCE3} modules/fish.cpp
cp %{SOURCE4} modules/statupdate.cpp
cp %{SOURCE5} modules/log.cpp
mv modules/sample.cpp .

%build
%configure \
	--with-module-prefix=%{_libdir}/znc \
	%{!?with_ssl:--disable-openssl} \
	%{?with_sasl:--enable-sasl} \
	%{!?with_perl:--disable-perl} \
	%{?with_ipv6:--enable-ipv6} \
	%{?with_debug:--enable-debug}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README znc.conf
%attr(755,root,root) %{_bindir}/znc

%files module-admin
%defattr(644,root,root,755)
%{_libdir}/znc/admin.so

%files module-imapauth
%defattr(644,root,root,755)
%{_libdir}/znc/imapauth.so

%if %{with perl}
%files module-modperl
%defattr(644,root,root,755)
%{_libdir}/znc/modperl.pm
%{_libdir}/znc/modperl.so
%endif

%files module-partyline
%defattr(644,root,root,755)
%{_libdir}/znc/partyline.so

%if %{with sasl}
%files module-saslauth
%defattr(644,root,root,755)
%{_libdir}/znc/saslauth.so
%endif

%files module-webadmin
%defattr(644,root,root,755)
%{_libdir}/znc/webadmin.so
%{_libdir}/znc/webadmin/skins/*

%files module-antiidle
%defattr(644,root,root,755)
%{_libdir}/znc/antiidle.so

%files module-autoattach
%defattr(644,root,root,755)
%{_libdir}/znc/autoattach.so

%files module-autoop
%defattr(644,root,root,755)
%{_libdir}/znc/autoop.so

%if %{with ssl}
%files module-away
%defattr(644,root,root,755)
%{_libdir}/znc/away.so
%endif

%files module-awaynick
%defattr(644,root,root,755)
%{_libdir}/znc/awaynick.so

%files module-chansaver
%defattr(644,root,root,755)
%{_libdir}/znc/chansaver.so

%if %{with ssl}
%files module-crypt
%defattr(644,root,root,755)
%{_libdir}/znc/crypt.so
%endif

%files module-email
%defattr(644,root,root,755)
%{_libdir}/znc/email.so

%if %{with ssll}
%files module-fish}
%defattr(644,root,root,755)
%{_libdir}/znc/fish.so
%endif

%files module-kickrejoin
%defattr(644,root,root,755)
%{_libdir}/znc/kickrejoin.so

%files module-log
%defattr(644,root,root,755)
%{_libdir}/znc/log.so

%files module-nickserv
%defattr(644,root,root,755)
%{_libdir}/znc/nickserv.so

%files module-perform
%defattr(644,root,root,755)
%{_libdir}/znc/perform.so

%files module-raw
%defattr(644,root,root,755)
%{_libdir}/znc/raw.so

%if %{with ssl}
%files module-savebuff
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/savebuff.so}
%endif

%if %{with ssl}
%files module-schat
%defattr(644,root,root,755)
%{_libdir}/znc/schat.so
%endif

%files module-shell
%defattr(644,root,root,755)
%{_libdir}/znc/shell.so

%files module-statupdate
%defattr(644,root,root,755)
%{_libdir}/znc/statupdate.so

%files module-stickychan
%defattr(644,root,root,755)
%{_libdir}/znc/stickychan.so

%files module-watch
%defattr(644,root,root,755)
%{_libdir}/znc/watch.so

%files devel
%defattr(644,root,root,755)
%doc sample.cpp
%attr(755,root,root) %{_bindir}/znc-buildmod
%attr(755,root,root) %{_bindir}/znc-config
%{_includedir}/znc
