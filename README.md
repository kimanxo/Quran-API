<h1>Simple Quran API</h1>
<h2>Features</h2>
<ul>
<li>All Quran Surah's</li>
<li>Many Readers</li>
<li>Tottaly Free</li>
<li>Multi Lang Support</li>
</ul>
<h2>Endpoints</h2>
<ul>
<li>'/' : Home Page With An Interactive SwaggerUI Documentation</li>
<li>'/langs' : Get A List Of The Available Languages </li>
<li>'/surahs' : Get A List Of All Availaible Surah's, Each With Its ID Code </li>
<li>'/readers' : Get A List Of All Availaible Readers, Each With His ID Code </li>
<li>'/reader_surahs' : Get The Available Surahs For a Specific Reader </li>
<li>'/get_surah_link' : Get A Direct Link to The Specified Surah With The Specified Readers (IDs Requires) </li>
</ul>
<h2>Instalation</h2>
<p>Clone The Project Repo By Executing These These CLI Commands:</p>
<p><code> git clone https://github.com/kimanxo/Quran-API</code></p>
<p>Install The Project Requirements By Executing These CLI Commands:</p>
<p><code> pip install -r requirements.txt</code></p>
<h2>Usage</h2>
<p>Run The API Server Locally By Executing These CLI Commands:</p>
<p><code>python Server.py</code></p>
<h2>Note:</h2>
<p>you Can Always Adjust The Servers Setting To Suit our Need By Edtiting The Last Line In The Script:</p>
<p><code>if __name__ == '__main__':
    uvicorn.run(app,port=${PORT},host='${HOST}')</code></p>
<p><b>Hint:</b> You Can Set ${HOST} to <code>host='0.0.0.0'</code> to make it accessible all across the LAN, this way anyone can access the server by refrencing your machine's local ip address.</p>
<h2>Licence & Usage & Distribution: </h2>
<p>This Project is Open Source And Free To Use And Distribute, And It Has No Copyrights Restrictions.</p>
<small>Made With Love By <b>Ismail Saadaoui</b> That Goes Under The Username: <b>Kimanxo</b>.</small>
