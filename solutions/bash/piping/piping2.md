# Piping Exercises Part 1

Exercises based on Manfred Pamsl, Linux I

[vsftpd.log](../../../exercises/bash/piping/vsftpd.log)


## How many different IP-addresses have tried to connect?
```console
$ cut -d\" -f2 vsftpd.log | sort -u | wc -l
```

## From which IP-addresses where hacking attacks probably started?
```console
$ cut -d\" -f2 vsftpd.log | sort | uniq -c | sort -nr
```

## Which 2 usernames were most frequently used and how often?
```console
$ cut -d"[" -f3 vsftpd.log | cut -d"]" -f1 | sort | uniq -c | sort -nr | head -2
```

## How many failed logins were tried from 213.114.38.100?
## Without REGEX
```console
$ grep "FAIL" vsftpd.log | grep "213.114.38.100" | wc -l
```

### With REGEX
```console
$ grep "FAIL.*213\.114\.38\.100" vsftpd.log | wc -l
```

> In Regex the `.` (dot) means 'any character'. When you specifically want the dot, it has to be escaped. In the example above, this is not absolutely necessary because of the structure of the log entries.