README: My first "real" python programming exercise;
exercise_one

The log file of an application consists of the following entries:
DATE LOGLEVEL SESSION-ID BUSINESS-ID REQUEST-ID MSG

Example log entries:
 2012-09-13 16:04:22 DEBUG SID:34523 BID:1329 RID:65d33 'Starting new session'
 2012-09-13 16:04:30 DEBUG SID:34523 BID:1329 RID:54f22 'Authenticating User'
 2012-09-13 16:05:30 DEBUG SID:42111 BID:319 RID:65a23 'Starting new session'
 2012-09-13 16:04:50 ERROR SID:34523 BID:1329 RID:54ff3 'Missing Authentication token'
 2012-09-13 16:05:31 DEBUG SID:42111 BID:319 RID:86472 'Authenticating User'
 2012-09-13 16:05:31 DEBUG SID:42111 BID:319 RID:7a323 'Deleting asset with ID 435435'
 2012-09-13 16:05:32 WARN SID:42111 BID:319 RID:7a323 'Invalid asset ID'

Example of parsing a line:
2012-09-13 16:04:22 DEBUG SID:34523 BID:1329 RID:65d33 'Starting new session'
DATE = 2012-09-13 16:04:22
LOGLEVEL = DEBUG
SESSION-ID = 34523
BUSINESS-ID = 1329
REQUEST-ID = 65d33
MSG = Starting new session

1) Write a program that reads the log entries from a file and stores them in appropriate data structures.
The data should be stored in memory, ie. only use standard in memory data structures, not an external database. 

2) Using the code from (1) write functions that:
returns all log lines with a given log level
returns all log lines belonging to a given business
returns all log lines for a given session id
returns all log lines within a given date range

3) Write a profiling class that can be used to collect basic performance statistics about different blocks of code.
The class should calculate the time taken for a block of code to execute.
The class should store sufficient information so that it can calculate the maximum, minimum and average execution times.
The class should have a function that produces a print in the output  in the following format:
   BlockName: getLogLevel
   NumSamples: 12
   Min: 0.02 secs
   Max: 0.34 secs
   Average: 0.09 secs

4) Use the code from (3) to benchmark the functions from (2) and produce a report for each function for a log file with 10000 entries.
You will have to generate a log file for testing with 10000 lines:
DATE with a random distribution for a period of 2 hours
LOGLEVEL with a random distribution of TRACE, DEBUG, INFO, WARN, ERROR, FATAL 
SESSION-ID  with a random distribution of 500 id
BUSINESS-ID with a random distribution of 100 id
REQUEST-ID  with a random distribution of 1000 id
MSG some random string
5) Select the slowest performing function detected in (4) and if possible redesign the way the data is store to improve significantly the performance of the function.
If it is not possible to improve my kudos to you :)

