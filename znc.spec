#
# Conditional build:
%bcond_without	ssl	# Build without support for SSL encryption.
%bcond_without	sasl	# Build without Cyrus SASL authentication module.
%bcond_without	perl	# Build without Perl scripting module.
%bcond_without	ipv6	# Build without IPv6 connection support.
%bcond_with	debug	# Build debugging binaries.
Summary:	An advanced IRC bouncer
Name:		znc
Version:	1.2
Release:	0.1
License:	GPL v2
Group:		Daemons
URL:		http://znc.in/
Source0:	http://znc.in/releases/%{name}-%{version}.tar.gz
# Source0-md5:	ef18e5402a82cc3fcab5c2ac5c2e6f3b
Source3:	fish.c
%{?with_sasl:BuildRequires: cyrus-sasl-devel}
BuildRequires:	libstdc++-devel
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.8}
%{?with_perl:BuildRequires: perl-devel}
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZNC is an IRC bounce with many advanced features like detaching,
multiple users, per channel playback buffer, SSL, IPv6, transparent
DCC bouncing, Perl and C++ module support to name a few.

%package module-adminlog
Summary:	znc adminlog global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-adminlog
A global module for the znc IRC bouncer. Log user connects and
disconnects and failed logins to file or syslog.

%package module-blockuser
Summary:	znc blockuser global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-blockuser
A global module for the znc IRC bouncer. Blocks certain users from
using ZNC saying their account was disabled.

%package module-certauth
Summary:	znc certauth global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-certauth
A global module for the znc IRC bouncer. This module lets users to
log in via SSL client keys.

%package module-fail2ban
Summary:	znc fail2ban global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-fail2ban
A global module for the znc IRC bouncer. Block IPs for some time after
a failed login.

%package module-imapauth
Summary:	znc imapauth global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-imapauth
A global module for the znc IRC bouncer. Allows users to authenticate
via IMAP.

%package module-identfile
Summary:	znc identfile global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-identfile
A global module for the znc IRC bouncer. The identfile module places
the ident of a user to a file when they are trying to connect.

%package module-lastseen
Summary:	znc lastseen global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-lastseen
A global module for the znc IRC bouncer. Logs when a user last logged
in to ZNC.

%package module-modperl
Summary:	znc modperl global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-modperl
A global module for the znc IRC bouncer. Loads perl scripts as ZNC
modules.

%package module-modules_online
Summary:	znc modules_online user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-modules_online
A user module for the znc IRC bouncer. This module fakes the online
status of ZNC-*users, so that ISON and WHOIS commands to *status e.g.
return something that makes the IRC client believe the user is online.
This helps to query with these users for specific IRC clients like
Colloquy that perform online check of open query windows.

%package module-notify_connect
Summary:	znc notify_connect global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-notify_connect
A global module for the znc IRC bouncer. Sends a notice to all admins
when a user logs in or out.

%package module-route_replies
Summary:	znc route_replies network module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-route_replies
A network module for the znc IRC bouncer. Routes back answers to the
right client when connected with multiple clients.

%package module-partyline
Summary:	znc partyline global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-partyline
A global module for the znc IRC bouncer. Allows ZNC users to join
internal channels and query other ZNC users on the same ZNC.

%package module-sasl
Summary:	znc saslglobal module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-sasl
A global module for the znc IRC bouncer. Allow users to authenticate
via SASL.

%package module-webadmin
Summary:	znc webadmin global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-webadmin
A global module for the znc IRC bouncer. Allows you to add/remove/edit
users and settings on the fly via a web browser.

%package module-autoattach
Summary:	znc autoattach user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-autoattach
A user module for the znc IRC bouncer. Reattaches you to channels on
activity.

%package module-autocycle
Summary:	znc autocycle user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-autocycle
A user module for the znc IRC bouncer. Cycles a channel when you are
the only one in there and you don't have op.

%package module-autoop
Summary:	znc autoop user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-autoop
A user module for the znc IRC bouncer. Auto op the good guys.

%package module-autoreply
Summary:	znc autoreply user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-autoreply
A user module for the znc IRC bouncer. Gives an automatic reply if
someone messages you if you are away.

%package module-autovoice
Summary:	znc autovoice user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-autovoice
A user module for the znc IRC bouncer. Autovoices everyone who joins
some channel.

%package module-awaynick
Summary:	znc awaynick user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-awaynick
A user module for the znc IRC bouncer. Change your nick while you are
away.

%package module-awaystore
Summary:	znc awaystore user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-awaystore
A user module for the znc IRC bouncer. When you are set away or
detached, this module will save all private messages for you. The
messages can be read until you delete them. Messages are stored in an
encrypted file on your shell (based on the <password> you set, if
set). That way everyone who has access to this shell still cannot read
your messages. This module will also set you away when you are idle
some time (see timer/settimer).

%package module-block_motd
Summary:	znc block_motd user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-block_motd
A user module for the znc IRC bouncer. This module blocks the server's
Message of the Day.

%package module-bouncedcc
Summary:	znc bouncedcc user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-bouncedcc
A user module for the znc IRC bouncer. The bouncedcc module bounces
dcc transfers through the znc server instead of sending them directly
to the user.

%package module-buffextras
Summary:	znc buffextras user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-buffextras
A user module for the znc IRC bouncer. Add nick changes, joins, parts,
topic changes etc. to your playback buffer.

%package module-cyrusauth
Summary:	znc cyrusauth global module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-cyrusauth
A global module for the znc IRC bouncer. This module is intended for
admins who run a shell/web/email/etc server and want to provide ZNC
access to their existing users. By using this module, when your users
login to ZNC - either with their IRC client or via the webadmin module
- their password will be checked against your Cyrus SASL library
against whatever password checking backend you configured for SASL
instead of the ZNC config file.

%package module-chansaver
Summary:	znc chansaver user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-chansaver
A user module for the znc IRC bouncer. Keeping config up to date when
user joins and parts.

%package module-charset
Summary:	znc charset user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-charset
A user module for the znc IRC bouncer. Normalizes (i.e. converts)
character encodings.

%package module-clearbufferonmsg
Summary:	znc clearbufferonmsg user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-clearbufferonmsg
A user module for the znc IRC bouncer. This module attempts to bridge
the gap between being inundated with old buffer if you have
KeepBuffer=true; and possibly missing messages when you ping out, if
you have KeepBuffer=false.

%package module-clientnotify
Summary:	znc clientnotify user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-clientnotify
A user module for the znc IRC bouncer. Notify about new incoming
connections to your user.

%package module-controlpanel
Summary:	znc controlpanel user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-controlpanel
A user module for the znc IRC bouncer. Allows you to add/remove/edit
users and settings on the fly via IRC messages.

%package module-cert
Summary:	znc cert network module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-cert
A user module for the znc IRC bouncer. This module lets users use
their own SSL certificate to connect to a server

%package module-crypt
Summary:	znc crypt user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-crypt
A user module for the znc IRC bouncer. Encryption for channel/private
messages.

%package module-ctcpflood
Summary:	znc ctcpflood user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-ctcpflood
A user module for the znc IRC bouncer. This module tries to block ctcp
floods.

%package module-dcc
Summary:	znc dcc user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-dcc
A user module for the znc IRC bouncer. This module allows you to
transfer files to and from ZNC

%package module-disconkick
Summary:	znc disconkick user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-disconkick
A user module for the znc IRC bouncer. This module will kick your
client from all channels where you are, in case if ZNC disconnects
from server.

%package module-fish
Summary:	znc fish user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-fish
A user module for the znc IRC bouncer. Adds the ability to encrypt all
your outgoing messages with the FiSH blowfish block-cipher. This way
you can do the decryption/encryption on the bouncer instead of your
IRC client.

%package module-flooddetach
Summary:	znc flooddetach user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-flooddetach
A user module for the znc IRC bouncer. This module detaches you from
channels which are flooded.

%package module-keepnick
Summary:	znc keepnick user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-keepnick
A user module for the znc IRC bouncer. Tries to get you your primary
nick.

%package module-kickrejoin
Summary:	znc kickrejoin user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-kickrejoin
A user module for the znc IRC bouncer. An Autorejoin module. Allows
you to rejoin a channel (after a delay) when kicked.

%package module-listsockets
Summary:	znc listsockets user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-listsockets
A user module for the znc IRC bouncer. This module displays a list of
all open sockets in ZNC.

%package module-log
Summary:	znc log user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-log
A user module for the znc IRC bouncer. Log conversations to file.

%package module-missingmotd
Summary:	znc missingmotd user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-missingmotd
A user module for the znc IRC bouncer. This user module will send 422
to clients when they login.

%package module-nickserv
Summary:	znc nickserv user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-nickserv
A user module for the znc IRC bouncer. Auths you with NickServ.

%package module-notes
Summary:	znc notes user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-notes
A user module for the znc IRC bouncer. Keep and replay notes. This is
an example for webmods

%package module-q
Summary:	znc q user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-q
A user module for the znc IRC bouncer. Auths you with Q (and a little
more).

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

%package module-send_raw
Summary:	znc send_raw user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-send_raw
A user module for the znc IRC bouncer. Allows you to send raw traffic
to IRC from other users.

%package module-shell
Summary:	znc shell user module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-shell
A user module for the znc IRC bouncer. Have your unix shell in a query
window right inside of your IRC client.

%package module-simple_away
Summary:	znc simple_away network module
Group:		Daemons
Requires:	%{name} = %{version}-%{release}

%description module-simple_away
A user module for the znc IRC bouncer. Automatically set you away on
IRC when disconnected from the bouncer.

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
cp %{SOURCE3} modules/fish.cpp
mv modules/sample.cpp .

%build
%configure \
	--with-module-prefix=%{_libdir}/znc \
	%{!?with_ssl:--disable-openssl} \
	%{?with_sasl:--enable-cyrus} \
	%{?with_perl:--enable-perl} \
	%{?with_ipv6:--enable-ipv6} \
	%{?with_debug:--enable-debug}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%attr(755,root,root) %{_bindir}/znc
%dir %{_libdir}/znc
%dir %{_datadir}/znc
%dir %{_datadir}/znc/modules
%{_mandir}/man1/znc.1*

%files module-adminlog
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/adminlog.so

%files module-blockuser
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/blockuser.so
%{_datadir}/znc/modules/blockuser

%files module-certauth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/certauth.so
%{_datadir}/znc/modules/certauth

%files module-fail2ban
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/fail2ban.so

%files module-imapauth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/imapauth.so

%files module-identfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/identfile.so

%files module-lastseen
%attr(755,root,root) %{_libdir}/znc/lastseen.so
%{_datadir}/znc/modules/lastseen

%if %{with perl}
%files module-modperl
%defattr(644,root,root,755)
%{_libdir}/znc/modperl/ZNC.pm
%{_libdir}/znc/perleval.pm
%attr(755,root,root) %{_libdir}/znc/modperl.so
%attr(755,root,root) %{_libdir}/znc/modperl/ZNC.so
%attr(755,root,root) %{_libdir}/znc/modperl/startup.pl
%endif

%files module-modules_online
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/modules_online.so

%files module-notify_connect
%attr(755,root,root) %{_libdir}/znc/notify_connect.so

%files module-partyline
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/partyline.so

%files module-route_replies
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/route_replies.so

%if %{with sasl}
%files module-sasl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/sasl.so
%endif

%files module-webadmin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/webadmin.so
%{_datadir}/znc/webskins
%{_datadir}/znc/modules/webadmin

%files module-autoattach
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/autoattach.so

%files module-autocycle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/autocycle.so

%files module-autoop
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/autoop.so

%files module-autoreply
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/autoreply.so

%files module-autovoice
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/autovoice.so

%files module-awaynick
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/awaynick.so

%files module-awaystore
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/awaystore.so

%files module-block_motd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/block_motd.so

%files module-bouncedcc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/bouncedcc.so

%files module-buffextras
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/buffextras.so

%files module-chansaver
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/chansaver.so

%files module-cyrusauth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/cyrusauth.so

%files module-charset
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/charset.so

%files module-clearbufferonmsg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/clearbufferonmsg.so

%files module-clientnotify
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/clientnotify.so

%files module-cert
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/cert.so
%{_datadir}/znc/modules/cert

%files module-controlpanel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/controlpanel.so

%if %{with ssl}
%files module-crypt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/crypt.so
%endif

%files module-ctcpflood
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/ctcpflood.so

%files module-dcc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/dcc.so

%files module-disconkick
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/disconkick.so

%if %{with ssl}
%files module-fish
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/fish.so
%endif

%files module-flooddetach
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/flooddetach.so

%files module-keepnick
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/keepnick.so

%files module-kickrejoin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/kickrejoin.so

%files module-listsockets
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/listsockets.so
%{_datadir}/znc/modules/listsockets

%files module-log
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/log.so

%files module-missingmotd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/missingmotd.so

%files module-nickserv
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/nickserv.so

%files module-notes
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/notes.so
%{_datadir}/znc/modules/notes

%files module-q
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/q.so

%files module-perform
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/perform.so
%{_datadir}/znc/modules/perform

%files module-raw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/raw.so

%if %{with ssl}
%files module-savebuff
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/savebuff.so
%endif

%if %{with ssl}
%files module-schat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/schat.so
%endif

%files module-send_raw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/send_raw.so
%{_datadir}/znc/modules/send_raw

%files module-shell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/shell.so

%files module-simple_away
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/simple_away.so

%files module-stickychan
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/stickychan.so
%{_datadir}/znc/modules/stickychan

%files module-watch
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/znc/watch.so

%files devel
%defattr(644,root,root,755)
%doc sample.cpp
%attr(755,root,root) %{_bindir}/znc-buildmod
%{_mandir}/man1/znc-buildmod.1*
%{_includedir}/znc
%{_pkgconfigdir}/znc.pc
