#!/usr/bin/perl
#Author: Jeremy Eudy
#Usage: clear; perl Upload\ New\ Data.pl
use warnings;
use diagnostics;
use MongoDB;
use MongoDB::GridFS;
use File::Basename;
use IO::File;
use experimental 'smartmatch';

#Connecting to the proper MongoDB database
my $client = MongoDB::MongoClient->new(host => 'localhost');
my $db = $client->get_database( 'Tutoring_Database');
my $invColl = $db->get_collection( 'Invoices' );
print "MongoDB connected.\n";

#Locations for new invoices and existing invoices (local debug only).
#my $dir = "~/Documents/Programming/Invoice\ Database/New\ Invoices/";
#my $invoices = "~/Documents/Programming/Inovice\ Database/Invoices/";

#Retrieve directories from command-line.
my $dir = $ARGV[0];
my $invoices = $ARGV[1];
print "New invoice location: $dir\n";
print "Existing invoice location: $invoices\n";
print "Currently searching $dir for new invoices...\n";

#Count number of files in $dir and $invoices.
my @dirFiles = <$dir/*>;
my $dirCount = @dirFiles;
my @invFiles = <$invoices/*>;
my $invCount = @invFiles;
my $deleteCount = 0;

#Iterate through $dir to find duplicates in $invoices.
for ( my $i = 0; $i<$dirCount; $i++ ) {
	if( $dirFiles[$i] ~~ @invFiles ) {
		print "Duplicate found. $dirFiles[$i] is not new!\n";
		unlink($dirFiles[$i]);
		$deleteCount++;
	}
}

#Print final $deleteCount.
print "$deleteCount file(s) deleted.\n"

#Invoice data:
#Number(int), Recipient(str), Issue Date(str), Item(str), Description(str), Cost(float), Quantity(int), Line Total(float),
#Total(float), Balance(float), Due Date(str)

#Parse CSVs in $dir into MongoDB.
my @invoice;
for ( my $i = 0; $i<$dirCount; $i++  ) {
	my $file = $dirFiles[$i];
	open my $info, '>', $file or die "Could not open '$file': '$!'";
	while ( <$info> ) {
		push ( @invoice, $_ );
	}
	my ( $invNum, $recipient, $issue, @item, @descrip, @cost, @quantity, @line, $total, $balance, $due ) = split /\;/, $invoice[$i];
	$invColl->insert( {
		"Number"=> $invNum,
		"Recipient" => $recipient,
		"Issue Date" => $issue,
		"Items" => @item,
		"Descriptions" => @descrip,
		"Costs" => @cost,
		"Quantities" => @quantity,
		"Line Totals" => @line,
		"Total" => $total,
		"Balance" => $balance,
		"Due Date" => $due,
	} );
        #this won't work currently since the arrays won't properly parse. I need an example CSV.
}

exit;
