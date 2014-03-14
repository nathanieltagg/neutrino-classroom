#!/usr/bin/perl -w

# Quick script to pull links from a given file.
use WWW::Mechanize;

my $mech = WWW::Mechanize->new();
$mech->get( "file://Users/tagg/Downloads/muon.html" );
my @links = $mech->links();
for my $link ( @links ) {
    printf "%s\n", $link->url;
}
