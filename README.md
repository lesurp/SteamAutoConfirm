# Steam auto confirmation

## What it is
This script parses a file to find confirmation urls.
GET requests are made on those urls to confirm that you want to sell your item.

## How to use
To use this with a gmail inbox, you can open the conversation, 'print' it, then
download the printable page that is displayed.

Then simply run:
````
	python steam_auto_confirm.py /path/to/your/emails
````

It is possible do that with IMAP, but I am using a gmail account and this OAuth
just for that is annoying. With any email provider that allows a painless IMAP,
one can use imaplib to get the emails.

Note that the parsing / requests would be the same, so you only need to change
how you get your emails.
