import settings
import requests
import re

from BeautifulSoup import BeautifulSoup
from jinja2.filters import do_striptags


class NGit(object):

    def __init__(self):
        response = requests.get(settings.ngit)
        self.xml_feed = BeautifulSoup(response.text)

    def feed(self):
        for entry in self.xml_feed('entry'):
            try:
                html_entry = BeautifulSoup(do_striptags(entry.content.string))
                autor, uid, conteudo = BeautifulSoup(do_striptags(entry.content.string)).li(text=re.compile('.*'))
                autor = BeautifulSoup(do_striptags(entry.content.string)).a.string
                yield {"id": uid,
                    "titulo": entry.title.string,
                    'autor': entry.content.string,
                    'conteudo': conteudo[2:],
                   }
            except Exception, e:
                pass


# <entry>
# <id>tag:ngit.globoi.com,2005:Event/802153</id>
# <published>2012-09-11T10:40:09-03:00</published>
# <updated>2012-09-11T10:40:09-03:00</updated>
# <link type="text/html" href="http://ngit.globoi.com/busca" rel="alternate" />
# <title>luizgpsantos pushed 9238e71b to busca/busca:master</title>
# <content type="html">  &lt;p&gt;&lt;a href="/~luizgpsantos"&gt;luizgpsantos&lt;/a&gt; pushed &lt;a href="/busca/busca/commit/9238e71bc6f3481ab99849854a50bb7d781fd3e4"&gt;9238e71b&lt;/a&gt; to &lt;a href="/busca/busca"&gt;busca/busca:master&lt;/a&gt;&lt;/p&gt;
#   &lt;p&gt;&lt;p&gt;
# &lt;ul&gt;&lt;li&gt;Luiz Guilherme Pais dos Santos &lt;a href="/busca/busca/commit/9238e71bc6f3481ab99849854a50bb7d781fd3e4"&gt;9238e71&lt;/a&gt;: Retirei o backup de DEV e QA1 e acrescentei o backup dos aliases.&lt;/li&gt;&lt;/ul&gt;</content>
# <author>
# <name>luizgpsantos</name>
# </author>
# </entry>
