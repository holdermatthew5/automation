**Author:** Matthew Holder
**Version:** 0.1.0

[PR]()

Problem Domain:

Given a document of potential contacts extract all emails and phone numbers.
Write all phone numbers to seperate lines in 'phone_numbers.txt'.
Write all emails to seperate lines in 'emails.txt'.

Description:

The 'automation.py' script writes all numbers matching the '\(?\d{3}?\S?\d{3}\S?\d{4}' RegEx to a file 'phone_numbers.txt'.
It also writes all emails matching the '\S+@\S+.[a-z]{3}' RegEx to a file 'emails.txt'.