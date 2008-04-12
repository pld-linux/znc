#include "main.h"
#include "User.h"
#include "Nick.h"
#include "Modules.h"
#include "Chan.h"
#include "znc.h"
#include "Server.h"

class CStatUpdateMod : public CGlobalModule {
private:
	CString m_sPath;
	char epoch_str[64];
	
public:
	GLOBALMODCONSTRUCTOR(CStatUpdateMod) {  }
	
	virtual ~CStatUpdateMod () {}

	virtual void UpdateStatFile ()
	{
	    // Create filestream
	    FILE *file = fopen (m_sPath.c_str(), "w+");

		if (file == NULL)
			return;
	
	    sprintf(epoch_str, "%i", (int)time(NULL));

	    // Setup time
	    fputs ("STATUPDATE_TIME;", file);
	    fputs (epoch_str, file);
	    fputs ("\n", file);
	    
	    const map<CString, CUser*>& msUsers = CZNC::Get().GetUserMap();
	    for (map<CString, CUser*>::const_iterator it = msUsers.begin(); it != msUsers.end(); it++)
	    {
		CUser& User = *it->second;
		const CString& sNick = User.GetUserName();

		fputs (sNick.c_str(), file);
		fputs (";", file);
		
		if (User.IsUserAttached())
		{
		    fputs ("online\n", file);
		}
		else
		{
		    fputs ("offline\n", file);
		}
	    }

	    // close filestream
	    fclose (file);
	}

	virtual bool OnLoad(const CString& sArgs, CString& sMessage) {
	    m_sPath = sArgs;	
	    PutModule("StatUpdate module successfully loaded with args: [" + sArgs + "]");
	    return true;
	}

	virtual bool OnBoot() {
		return true;
	}
	
	virtual void OnUserAttached ()
	{
	    UpdateStatFile();
	}
	
	virtual void OnUserDetached ()
	{
	    UpdateStatFile();
	}
	
	virtual void OnModCommand(const CString& sCommand) {
		if (sCommand.CaseCmp("DEBUG") == 0) {
			PutModule("Current path is: " + m_sPath);
		}
		
		if ((sCommand.CaseCmp("UPDATE") == 0 || sCommand.CaseCmp("REFRESH") == 0) && m_pUser->IsAdmin()) {
			UpdateStatFile();
			PutModule("StatUpdate file successfully updated.");
		}

		if (sCommand.CaseCmp("VERSION") == 0) {
			PutModule("StatUpdate - v0.2b");
			PutModule("Autor: Daniel 'd4n13L' Schmitz (daniel@danielschmitz.de)");
		}
	}

	virtual EModRet OnStatusCommand(const CString& sCommand) {
		if (sCommand.CaseCmp("STATUPDATE") == 0) {
			PutModule("Hello! I am here ;-)");
			return HALT;
		}

		return CONTINUE;
	}
};

GLOBALMODULEDEFS(CStatUpdateMod, "StatUpdate writes users online status into a text file.")
