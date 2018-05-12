#!/usr/bin/perl
#Author: Jeremy Eudy
#Usage: perl UserUpload.pl
use warnings;
use diagnostics;
use MongoDB;
use MongoDB::GridFS;
use File::Basename;
use IO::File;

#Connecting to the proper MongoDB database
my $client = MongoDB::MongoClient->new(host => 'localhost');
my $db = $client->get_database( 'Tutoring_Database');
my $userColl = $db->get_collection( 'Users' );
print "MongoDB connected.\n";

#User data:
#FName, LName, Email, PhoneNum

#Retrieve User CSV file from command-line.
my $file = $ARGV[0];
print "User file: $file\n";

#Put user CSV into array and upload array.
my @csv;
open my $info, '<', $file or die "Could not open '$file': '$!'";
while( <$info> ) {
	push ( @csv, $_ );
}
my $rowCount = @csv;
for ( my $i = 0; $i < $rowCount; $i++ ) {
	my ( $fName, $lName, $email, $phoneNum ) = split /\;/, $csv[$i];
	$fName = uc $fName; $lName = uc $lName; $email = uc $email;
	$userColl->insert( {
		"First Name" => $fName,
		"Last Name" => $lName,
		"Email" => $email,
		"Phone Number" => $phoneNum,
	} );
	#This won't work since I need an example CSV but the syntax is there
}
