# Tutoring_Database
A MongoDB database system to store invoices and user info for bookkeeping purposes.

## Getting Started
Easy clone:
```
mkdir -p ~/Tutoring_Database/ && cd
git clone https://github.com/JeremyEudy/Tutoring_Database
```
Or replace ```~/Tutoring_Database/``` with a different valid location.

### Prerequisites
This project depends on MongoDB.pm and MongoDB current.
```
sudo apt-get install MongoDB
cpan MongoDB
```
### Usage
InvoiceUpload.pl
```
perl InvoiceUpload <Directory for new invoices> <Directory for existing invoices>
```
UserUpload.pl
```
perl UserUpload.pl <User CSV file>
```

### Author
Jeremy Eudy

### License
This project is licensed under the GPLv2
