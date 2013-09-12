#!/usr/bin/python

import platform, os, sys

"""

Take an options dictionary and update ./config/veil.py

"""
def generateConfig(options):
	
	config = """#!/usr/bin/python

##################################################################################################
#
# Veil configuration file												
#
# Run update.py to automatically set all these options.
#
##################################################################################################

"""

	config += '# OS to use (Kali/Backtrack/Debian/Windows)\n'
	config += 'OPERATING_SYSTEM="' + options['OPERATING_SYSTEM'] + '"\n\n'
	print " [*] OPERATING_SYSTEM = " + options['OPERATING_SYSTEM']

	config += '# Terminal clearing method to use\n'
	config += 'TERMINAL_CLEAR="' + options['TERMINAL_CLEAR'] + '"\n\n'
	print " [*] TERMINAL_CLEAR = " + options['TERMINAL_CLEAR']
	
	config += '# Veil base install path\n'
	config += 'VEIL_PATH="' + options['VEIL_PATH'] + '"\n\n'
	print " [*] VEIL_PATH = " + options['VEIL_PATH']
	
	source_path = os.path.expanduser(options["PAYLOAD_SOURCE_PATH"])
	config += '# Path to output the source of payloads\n'
	config += 'PAYLOAD_SOURCE_PATH="' + source_path + '"\n\n'
	print " [*] PAYLOAD_SOURCE_PATH = " + source_path

	# create the output source path if it doesn't exist
	if not os.path.exists(source_path): 
		os.makedirs(source_path)
		print " [!] path '" + source_path + "' created"
	
	compiled_path = os.path.expanduser(options["PAYLOAD_COMPILED_PATH"])
	config += '# Path to output compiled payloads\n'
	config += 'PAYLOAD_COMPILED_PATH="' + compiled_path +'"\n\n'
	print " [*] PAYLOAD_COMPILED_PATH = " + compiled_path

	# create the output compiled path if it doesn't exist
	if not os.path.exists( compiled_path ): 
		os.makedirs( compiled_path )
		print " [!] path '" + compiled_path + "' created"

	config += '# Path to temporary directory\n'
	config += 'TEMP_DIR="' + options["TEMP_DIR"] + '"\n\n'
	print " [*] TEMP_DIR = " + options["TEMP_DIR"]
	
	config += '# The path to the metasploit framework, for example: /usr/share/metasploit-framework/\n'
	config += 'METASPLOIT_PATH="' + options['METASPLOIT_PATH'] + '"\n\n'
	print " [*] METASPLOIT_PATH = " + options['METASPLOIT_PATH']

	f = open("veil.py", 'w')
	f.write(config)
	f.close()
	
	print " [*] Configuration file successfully written to 'veil.py'\n"

if __name__ == '__main__':

	options = {}

	if platform.system() == "Linux":
		
		# check /etc/issue for the exact linux distro
		issue = open("/etc/issue").read()
		
		if issue.startswith("Kali"):
			options["OPERATING_SYSTEM"] = "Kali"
			options["TERMINAL_CLEAR"] = "clear"
			options["METASPLOIT_PATH"] = "/usr/share/metasploit-framework/"
			
		elif issue.startswith("BackTrack"):
			options["OPERATING_SYSTEM"] = "BackTrack"
			options["TERMINAL_CLEAR"] = "clear"
			options["METASPLOIT_PATH"] = "/opt/metasploit/msf3/"
		else:
			options["OPERATING_SYSTEM"] = "Linux"
			options["TERMINAL_CLEAR"] = "clear"
			msfpath = raw_input(" [>] Please enter the path of your metasploit installation: ")
			options["METASPLOIT_PATH"] = msfpath
		
		veil_path = "/".join(os.getcwd().split("/")[:-1]) + "/"
		options["VEIL_PATH"] = veil_path
		options["PAYLOAD_SOURCE_PATH"] = "~/veil-output/source/"
		options["PAYLOAD_COMPILED_PATH"] = "~/veil-output/compiled/"
		options["TEMP_DIR"]="/tmp/"

	# not current supported
	elif platform.system() == "Windows":
		options["OPERATING_SYSTEM"] = "Windows"
		options["TERMINAL_CLEAR"] = "cls"

		veil_path = "\\".join(os.getcwd().split("\\")[:-1]) + "\\"
		options["VEIL_PATH"] = veil_path
		
		options["PAYLOAD_SOURCE_PATH"] = veil_path + "output\\source\\"
		options["PAYLOAD_COMPILED_PATH"] = veil_path + "output\\compiled\\"
		options["TEMP_DIR"]="C:\\Windows\\Temp\\"
		
		msfpath = raw_input(" [>] Please enter the path of your metasploit installation: ")
		options["METASPLOIT_PATH"] = msfpath
	
	# unsupported platform... 
	else:
		print " [!] ERROR: PLATFORM NOT SUPPORTED"
		sys.exit()

	generateConfig(options)
