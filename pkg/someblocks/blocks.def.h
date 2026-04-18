//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
  {"",      "sb-notify",        1,              13},
  {"",		  "sb-wifi",    		  30,       			1},
	{"",		  "sb-temp",		      5,			        15},
	{"",		  "sb-mem", 		      10,			        14},
  {"",      "sb-music",         1,              3},
	{"",		  "sb-vol",		        60,			        10},
	{"",		  "sb-brightness",	  0,			        11},
	{"",		  "sb-bat",		        30,			        2},
	{"",		  "sb-date",		      60,			        0},
	
	/* Updates whenever "pkill -SIGRTMIN+10 someblocks" is ran */
	/* {"", "date '+%b %d (%a) %I:%M%p'",					0,		10}, */
};



//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim[] = " | ";
static unsigned int delimLen = 5;
