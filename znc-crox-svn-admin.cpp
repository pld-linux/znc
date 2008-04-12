#include <main.h>
#include <znc.h>
#include <User.h>
#include <Modules.h>

class CAdminMod : public CGlobalModule
{
public:
	GLOBALMODCONSTRUCTOR( CAdminMod )
	{
	}
	
	virtual ~CAdminMod()
	{
	}

	virtual void OnModCommand(const CString& sLine)
	{
		if (!m_pUser)
			return;

		CString sCommand = sLine.Token(0);
		cout << sCommand << endl;

		if (m_pUser->IsAdmin() && sCommand.CaseCmp("LISTUSERS") == 0) {
			cout << "LISTUSERS!" << endl;

			const map<CString, CUser*>& msUsers = CZNC::Get().GetUserMap();
			CTable Table;
			Table.AddColumn("Username");
			Table.AddColumn("Realname");
			Table.AddColumn("IsAdmin");
			Table.AddColumn("Nick");
			Table.AddColumn("AltNick");
			Table.AddColumn("Ident");
			Table.AddColumn("VHost");
	
			for (map<CString, CUser*>::const_iterator it = msUsers.begin(); it !=
						msUsers.end(); it++) {
				Table.AddRow();
				Table.SetCell("Username", it->first);
				Table.SetCell("Realname", it->second->GetRealName());
				if (!it->second->IsAdmin()) {
					Table.SetCell("IsAdmin", "No");
				} else {
					Table.SetCell("IsAdmin", "Yes");
				}
				Table.SetCell("Nick", it->second->GetNick());
				Table.SetCell("AltNick", it->second->GetAltNick());
				Table.SetCell("Ident", it->second->GetIdent());
				Table.SetCell("VHost", it->second->GetVHost());
			}
		
			if (Table.size()) {
				unsigned int uTableIdx = 0;
				CString sLine;
				while (Table.GetLine(uTableIdx++, sLine)) {
					PutModule(sLine);
				}
			}
			return;
			// LISTUSERS
		} else if (sCommand.CaseCmp("HELP") == 0) {
			CTable Table;
			Table.AddColumn("Command");
			Table.AddColumn("Arguments");
			Table.AddColumn("Description");
	
			Table.AddRow();
			Table.SetCell("Command", "GetNick");
			Table.SetCell("Arguments","[username]");
			Table.SetCell("Description","Prints (current) users nick");

			Table.AddRow();
			Table.SetCell("Command", "GetAltNick");
			Table.SetCell("Arguments","[username]");
			Table.SetCell("Description","Prints (current) users alternative nick");
	
			Table.AddRow();
			Table.SetCell("Command", "");
			Table.SetCell("Arguments","");
			Table.SetCell("Description","");
	
			if (Table.size()) {
				unsigned int uTableIdx = 0;
				CString sLine;
				while (Table.GetLine(uTableIdx++, sLine)) {
					PutModule(sLine);
				}
			}
			return;
			// HELP
		} else if (sCommand.CaseCmp("ADDUSER") == 0 && m_pUser->IsAdmin()) {
			CString sUsername = sLine.Token(1);
			CString sPassword = sLine.Token(2);
//			CString sIRCServer = sLine.Token(3, true);
			if (sUsername.empty() || sPassword.empty() /* || sIRCServer.empty() */ ) {
				PutModule("Usage: adduser <username> <password> <ircserver>");
				return;
			}

			if (CZNC::Get().FindUser(sUsername)) {
				PutModule("User " + sUsername + " already exists!");
				return;
			}

			CString sErr;
			CUser* pNewUser = new CUser(sUsername);
			pNewUser->SetPass(sPassword.MD5(), true);
//			pNewUser->AddServer(sIRCServer);
			if (!CZNC::Get().AddUser(pNewUser, sErr)) {
				delete pNewUser;
				PutModule("User not added [" + sErr + "]!");
				return;
			}

			PutModule("User " + sUsername + " added!");
			return;
			// ADDUSER
		}

		CUser* pUser = NULL;
		CString user = sLine.Token(1);
		CString value = sLine.Token(2);

		if (!m_pUser->IsAdmin() || value.empty()) {
			pUser = m_pUser;
			value = user;
		} else {
			pUser = CZNC::Get().FindUser(user);
		}
	
		if (!pUser) {
			PutModule("User not found!");
			return;
		}

		if (sCommand.CaseCmp("GETNICK") == 0) {
			PutModule("Nick is " + pUser->GetNick());
			// GETNICK
		} else if (sCommand.CaseCmp("GETALTNICK") == 0) {
			PutModule("AltNick is " + pUser->GetAltNick());
			// GETALTNICK
//		} else if (sCommand.CaseCmp("GETAWAYSUFFIX") == 0) {
//			 PutModule("AwaySuffix is " + pUser->GetAwaySuffix());
			// GETAWAYSUFFIX
		} else if (value.empty()) {
			PutModule("Usage: command [username] value");
			return;
		} else if (sCommand.CaseCmp("SETNICK") == 0) {
				pUser->SetNick(value);
				PutModule("Nick set to " + value);
			// SETNICK
		} else if (sCommand.CaseCmp("SETALTNICK") == 0) {
			pUser->SetAltNick(value);
			PutModule("AltNick set to " + value);
			// SETALTNICK
//		} else if (sCommand.CaseCmp("SETAWAYSUFFIX") == 0) {
//			 pUser->SetAwaySuffix(value);
//			PutModule("AwaySuffix set to " + value);
			// SETAWAYSUFFIX
		} else if (sCommand.CaseCmp("SETIDENT") == 0) {
			pUser->SetIdent(value);
			PutModule("Ident set to " + value);
			// SETIDENT
		} else if (sCommand.CaseCmp("SETREALNAME") == 0) {
			pUser->SetRealName(value);
			PutModule("RealName set to " + value);
			// SETREALNAME
		} else if (sCommand.CaseCmp("SETVHOST") == 0) {
			pUser->SetVHost(value);
			PutModule("VHost set to " + value);
			// SETVHOST
		} else if (sCommand.CaseCmp("SETMULTICLIENTS") == 0) {
			pUser->SetMultiClients(value.CaseCmp("TRUE") == 0 ? true : false);
			PutModule("MultiClients set to " + (value.CaseCmp("TRUE") == 0) ? "true"
					: "false");
			// SETMULTICLIENTS
		} else if (sCommand.CaseCmp("SETBOUNCEDCCS") == 0) {
			pUser->SetBounceDCCs(true);
			PutModule("BounceDCCs set to " + value);
			// SETBOUNCEDCCS
		} else if (sCommand.CaseCmp("SETUSECLIENTIP") == 0) {
			pUser->SetUseClientIP(true);
			PutModule("UseClientIP set to " + value);
			// SETUSECLIENTIP
		} else if (sCommand.CaseCmp("SETKEEPNICK") == 0) {
			pUser->SetKeepNick(true);
			PutModule("KeepNick set to " + value);
			// SETKEEPNICK
		} else if (sCommand.CaseCmp("SETDENYLOADMOD") == 0) {
			pUser->SetDenyLoadMod(true);
			PutModule("DenyLoadMod set to " + value);
			// SETDENYLOADMOD
		} else if (sCommand.CaseCmp("SETDEFAULTCHANMODES") == 0) {
			pUser->SetDefaultChanModes(value);
			PutModule("DefaultChanModes set to " + value);
			// SETDEFAULTCHANMODES
		} else if (sCommand.CaseCmp("ADDIRCSERVER") == 0) {
			PutModule("user: " + pUser->GetUserName());
			pUser->AddServer(value);
			PutModule("IRC Server added " + value);
//			cout << "x: " << pUser->CountServers() << endl;
//			PutModule("Server count: " + CString(pUser->CountServers()));
			// ADDIRCSERVER
		} else if (sCommand.CaseCmp("SETQUITMSG") == 0) {
			pUser->SetQuitMsg(value);
			PutModule("Quit Message set to " + value);
			// SETQUITMSG
		} else if (sCommand.CaseCmp("SETBUFFERCOUNT") == 0) {
			pUser->SetBufferCount(0);
			PutModule("Buffer count set to " + value);
			// SETBUFFERCOUNT
		} else if (sCommand.CaseCmp("SETKEEPBUFFER") == 0) {
			pUser->SetKeepBuffer(true);
			PutModule("Keep buffer set to " + value);
			// SETKEEPBUFFER
		} else if (sCommand.CaseCmp("SETAUTOCYCLE") == 0) {
			pUser->SetAutoCycle(true);
			PutModule("AutoCycle set to " + value);
			// SETAUTOCYCLE
		} else {
			PutModule("Unknown command.");
		}
	}
};

GLOBALMODULEDEFS( CAdminMod, "Dynamic configuration of users/settings through irc" )
