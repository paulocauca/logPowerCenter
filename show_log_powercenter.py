# -*- coding: iso-8859-1 -*-

import sys
import os
sys.path.append('/prod_dat1/scriptsf/portal/site-packages/')
import cx_Oracle


def connRepository(v_FOLDER, v_WF):
	conn = cx_Oracle.connect('USUARIO/SENHA@BASE')
	cLogFile = conn.cursor()
	
	logFile = cLogFile.execute("""
	SELECT LOG_FILE FROM OPB_SESS_TASK_LOG 
    WHERE
        WORKFLOW_RUN_ID = (
            SELECT MAX(WORKFLOW_RUN_ID) AS WORKFLOW_RUN_ID FROM OPB_WFLOW_RUN
            WHERE START_TIME >= SYSDATE -1 AND upper(WORKFLOW_NAME) = upper('""" + v_WF + """') AND SUBJECT_ID = (
                    SELECT SUBJ_ID FROM OPB_SUBJECT WHERE upper(SUBJ_NAME) = upper('""" + v_FOLDER + """') )
            )""").fetchmany()
	
	conn.close()
	
	return logFile

 
if __name__ == "__main__":
	
	#Parametros 
	v_dir_converte_log='/app/powercenter/PowerCenter9.1.0/server/bin'
	v_dir_log='/app/powercenter/Interfaces/log'
	
	v_FOLDER = sys.argv[1]
	v_WF	= sys.argv[2]
	
	fileLogBin = connRepository( v_FOLDER, v_WF)
	
	for fileName in fileLogBin:	
		if(os.path.exists(fileName[0] + '.bin')):
			fileSize = os.path.getsize(fileName[0] + '.bin') /1024 / 1024
			if ( fileSize  >= 2 ): 
				print "====>>>>> ALERT: LOG ACIMA DE 2 MB, NAO SERA CONVERTIDO \n "
			else:	
				fileLogTex = os.system(v_dir_converte_log+'/infacmd.sh ConvertLogFile -in ' + fileName[0] + '.bin -fm Text')
				print fileLogTex
		else:
			print "# INFO : ARQUIVO NAO DISPONIVEL NO DIRETORIO :" + fileName[0] + ".bin \n "
