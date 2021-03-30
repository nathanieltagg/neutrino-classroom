#!/usr/bin/env python3
import os

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

tasks = [
  {"infile":"muon_links.txt","batches":char_range('A','T'),"outfile":"deploy/muon_", "n" :20},
  {"infile":"momentum_links.txt","batches":char_range('A','T'),"outfile":"deploy/momentum_", "n" :20},
  ];

for task in tasks:
  print(task)
  infile_handle = open(task['infile'], 'r')
  Lines = infile_handle.readlines()
  print("Loaded %d links"%len(Lines))
  start = 0
  for batch in task['batches']:
    print(batch,start,start+task["n"])
    links = Lines[start:start+task["n"]]
    outfilename = task["outfile"]+batch+".html"
    try: 
      os.unlink(outfilename)
    except: None
    f = open(outfilename,"w+")
    print("<!DOCTYPE html>\n",file=f)
    print("<head>\n",file=f)
    print("<!-- Do not edit. Created by build.py script -->",file=f)
    print("<title>Group "+batch+"</title>\n",file=f)
    print("<link rel='stylesheet' href='common.css' type='text/css' />\n",file=f)
    print("</head>\n",file=f)
    print("<body>\n",file=f)
    print("<div id='content'>\n",file=f)
    print("<div  class='content links'>\n",file=f)
    print("<h2>Group "+batch+"</h2>\n",file=f)
    print("<p>Each link below goes to one event in your sample. Make sure you're on the right page before you start.</p>\n",file=f);
    print("<p>Use your browser's back button to get back to this page and select the next event.</p>",file=f);

    i = 1
    for link in links:
      print("<a href='"+link+"'>Event "+str(i)+"</a><br/>\n",file=f)
      i=i+1
    print(batch+ " "+str(i))
    start=start+task["n"]

    print("</div></div>",file=f);
