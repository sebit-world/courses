### Comment (#)
```bash
# The content after '#' are called comments.
# Comments are remarks for the reader and will not be executed
```

### Change directory(cd)
```bash
# goto /home/nano
cd /home/nano

# goto /home/nano/Documents
cd ~/Documents   

# go up one level
cd ..

# goto previous directory 
cd -
```

### List (ls)
```bash
# list the files in the current directory
ls

# list in a long listing format
ls -l

# list all files including hidden files    
ls -la

# list all files sizes in human readable formats
ls -lah	
```

### shutdown, poweroff, reboot
```bash
sudo shutdown now           # shut down immediately
sudo shutdown --halt 22:00  # halt the system at 10pm
sudo shutdown --halt +5     # halt the system after 5 mins delay
sudo shutdown -c            # cancel a pending shutdown

# shut down immediately
sudo poweroff 

# Reboot
sudo reboot

```


### Copy (cp) , Move (mv), Remove (rm), Make Directory (mkdir)
```bash
# Copy file(s) into another directory
cp filename.txt ~/Documents
cp filename1.txt filename2.txt filename3.txt ~/Documents

# Copy content of a file into another file
cp filename1.txt filename2.txt

# Copy entire directory
cp -R ~/Documents ~/Documents_backup

# Move file into another directory
mv filename.txt ~/Documents

# Rename file
mv old_filename.txt new_filename.txt

# Create directory
mkdir directory_name

# Creates directories along the path if they do not exist
mkdir -p /path/to/directory/

# Remove
rm filename
rm filename1 filename2 filename3

# Remove files and directories recursively
rm -r directory_name
```

### Create file(touch), Concatenate file(cat)
```bash
# Create an empty file
touch hello_world.py

# Dump the file content on the screen
cat /var/log/syslog

# Concatenate syslog and syslog.1 into a single file ~/combined.log
cat /var/log/syslog /var/log/syslog.1 > ~/combined.log

```


