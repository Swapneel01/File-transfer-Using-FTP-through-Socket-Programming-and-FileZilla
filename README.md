# File-transfer-Using-FTP-through-Socket-Programming-and-FileZilla
<p> A prerequisite for all the programs above is the fact that all the PCs involved, both the server and the client should be connected to the same WiFi network and the IP address of the server should be entered and changed in the code. We have also included the screenshots as well as the packet captures using WireShark which is a very popular packet sniffing software through which the packets can be analysed and request made by the client or the server can be seen.</p>
<h1> Message Transfer </h1>
<p> We have used socket programming to transfer messages on the command prompt from the client to the server and then the server replies with the same message.</p>
<h1>File Transfer </h1>
<h2>FileZilla </h2>
<p>We have used FileZilla which is a very popular FTP client available for free (download <a href="https://filezilla-project.org/">here</a>) and for the server we made use of Universal FTP server which is available for free from the Microsoft Store (download <a href="https://www.microsoft.com/en-us/p/universal-ftp-server/9nqkq104hb9r">here</a>). We connected the 2, transferred the files and captured the packets so that they can be compared to the FTP implementation using Python.</p>
<h2>FTP</h2>
<p>On the server side we have made use of pyftpdlib (more info <a href="https://github.com/giampaolo/pyftpdlib">here</a>) and for the client we have used ftplib (more info <a href="https://docs.python.org/2/library/ftplib.html">here</a>). The server supports multithreading as well, as in multiple clients can log in at the same time and access the server.</p>
<h3>TCP</h3>
<p>We have made use of Socket Programming, but before that we have read the text files, transferred the contents as message and again stored it as a text file on the client side.</p>
<br>
<p>In all the cases above, the server should be running before the client, this is very <strong>important</strong>.</p>
