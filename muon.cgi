#!/usr/bin/perl -w
use CGI::Pretty qw/:standard *table *tr start_Tr start_td start_ul start_tbody end_tbody *div keywords/;
use CGI::Carp qw/warningsToBrowser fatalsToBrowser/;
use POSIX qw(strftime);
use Cwd qw/getcwd realpath/;

$num_in_group = 20;
$infile = "muon_links.txt";

@kw=keywords();
$group = $kw[0];

if    ($group =~ /^[A-Z].*/) { $group = substr($group,0,1);}
elsif ($group =~ /^[a-z].*/) { $group = uc substr($group,0,1);}
else { $group = 'A';}

print header;

print start_html(
-title=>"Group $group",
-style=>{-src=>['common.css'], -media=>'all'}
);

open(LINKS,"<$infile") || die("Can't open links file");

print "<div id='content'>\n";
print "<div  class='content links'>\n";
print h2("Group $group");

print p("Each link below goes to one event in your sample. Make sure you're on the right page before you start.");
print p("Use your browser's back button to get back to this page and select the next event.");
@links = ();
foreach $g  ('A'..$group)
{
  @links = ();
  for (my $i=1; $i <= $num_in_group; $i++) { 
    $_ = <LINKS>;
    chomp;
    push @links,$_;    
  }
}

for (my $i=1; $i <= $num_in_group; $i++) { 
  print a({-href=>$links[$i-1]},"Event $i") . br . "\n";
}

print "</div></div>";

print end_html;
