import re import csv
with open('connectio.log', 'r') as log_file:
log_pattern	=	re.compile(r'\[(.*)\]\s\[ID\]		(\d+)\s\[Rule\] (.+?)\s?\[(?:Service|Connection)\]			(.+?)\s(TCP|UDP) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)	->			(.+?)
\((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\):(\d+)\s?\[(?:Iface|Zone)\] (\w+)\s?\[(?:Duration|Elapsed)\]	(\d+)	sec\s?\[(?:Bytes|Sent|Received)\] (\d+)/(\d+)/(\d+)\s?\[(?:Packets|Frames)\] (\d+)/(\d+)/(\d+)')
match = log_pattern.search(line) if match:
log_data.append(match.groups()) # Open a CSV file for writing
with open('outputLog.csv', 'w', newline='') as csv_file:
csv_writer.writerow(['Timestamp', 'ID', 'Rule', 'Connection', 'Protocol', 'Source IP', 'Source Port', 'Destination url', 'Destination IP', 'Destination Port', 'Zone', 'Duration', 'Bytes Sent', 'Bytes Received', 'Bytes Total', 'Packets Sent', 'Packets Received', 'Packets Total'])
csv_writer.writerow(row)
