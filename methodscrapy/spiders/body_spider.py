import scrapy
import re
import unicodedata
import csv

def strip(text):
    return re.sub('[\n|\t|\r|\v|\f|;|\"|\']+', '', text)

def clean_up(text):
    try:
        if text is None:
            return ""
        if text is type('unicode'):
            return strip( text.encode('ascii', 'ignore') )
        else:
            return strip( text )
    except:
        import sys
        print "Unexpected error:", sys.exc_info()[0]
        print(type(text))

class BodySpider(scrapy.Spider):
    name = "body"
    allowed_domains = []

    start_urls = ["http://mrk.tv/1KSngGi","http://bit.ly/1dQDYv1","http://qz.com/393206","http://slidesha.re/16cBK4L","https://twitter.com/GrowthHackers/status/596802019442176001","http://bit.ly/1uhnnrq","http://bit.ly/1EWHfRO","http://linkd.in/1KNka6x","http://bit.ly/1KNkWQW","https://twitter.com/FiveThirtyEight/status/596720646207492096","http://bit.ly/1ya2VKd","http://ow.ly/MDB92","http://tinyurl.com/plflsog","http://bit.ly/1cgXqQp","https://twitter.com/hichamchraibi/status/596795556539707394","https://growthhackers.com/simple-ux-mistakes-to-avoid-on-your-blog/","http://slidesha.re/1y02Dzm","https://growthhackers.com/programmatic-advertising-in-a-nutshell-part-one/","http://slidesha.re/1DdJTTw","http://bit.ly/1chavJj","http://bit.ly/1GU00ns","http://bit.ly/1F6ShYi","http://bit.ly/1PpSbui","http://bit.ly/1JSVKeb","https://growthhackers.com/how-to-run-better-marketing-experiments-a-growth-strategy/","http://buff.ly/1GTTZHq","https://twitter.com/martahari/status/596783772705501184","http://ctt.ec/6PEAa+","http://time.com/3482136/what-is-growth-hacking/","https://twitter.com/V9SEO/status/596797023891886082","https://twitter.com/releaseman/status/596816856985513984","http://ow.ly/MAd2d","https://twitter.com/HDScorp/status/596752119371300864","http://justforward.co","http://growthhackers.com/?post_type=slides&p=27246","http://ow.ly/MDAUY","http://bit.ly/1KNkdiP","http://klou.tt/1g37xs6g475lp","https://twitter.com/31WestGlobal/status/596796769293459456","http://bit.ly/1AJJggt","http://growthhackers.com/?p=565","http://buff.ly/1PpS6GW","https://twib.in/l/Xn6RzrdGAB8","http://tinyurl.com/n88s865","http://onforb.es/1IvDXrW","http://bit.ly/1CFHnmT","http://www.huffingtonpost.com/courtney-oconnell/7-ways-bloggers-are-growt_b_7017834.html?utm_campaign=naytev&utm_content=554cab1be4b0e299cd8f8171","http://bit.ly/1BGM2qy","https://twitter.com/gauravwadekar/status/596789331366383616","https://twitter.com/chuckaikens/status/596782246067056640","http://buff.ly/1GTFAek","https://twib.in/l/ndBzAMajza5","http://bit.ly/1GXTYHH","http://bit.ly/1KlSDbq","https://growthhackers.com/peek-at-the-27-metrics-in-pinterests-internal-growth-dashboard/","http://lamaquinadelpensamiento.blogspot.com/2015/04/que-es-growth-hacking.html","http://fb.me/7mQcyuYeo","http://growthhackers.com/10-excel-functions-a-growth-hacker-cant-live-without/","https://growthhackers.com/25-lessons-from-guest-blogging-for-the-top-blogs-in-the-world/","http://GrowthHackers.com","http://bit.ly/1ya0nvT","http://www.growthhackers.com/?p=1473","http://ow.ly/MAx1D","https://www.rebelmouse.com/Charlesfrize/","https://twitter.com/Teresa_Eme/status/596351329120833538","http://bit.ly/1Eencft","http://buff.ly/1GSq5Wy","http://bit.ly/1EVlrXb","https://twitter.com/chuckaikens/status/596767035322937344","http://bit.ly/1Rj23K5","http://ift.tt/1FUpc0Y","http://www.business2community.com/strategy/beginners-guide-growth-hacking-9-tips-entrepreneurs-01218299","https://growthhackers.com/community-growth-advice-from-nichole-elizabeth-demere/","http://bit.ly/whitelabelbusiness","http://bit.ly/1ch7CbH","http://MusicLikeNeverBefore.com/jc/index.html","https://twitter.com/growthhackers/status/596797053843406848","https://twitter.com/chuckaikens/status/596691613495259137","https://growthhackers.com/programming-for-marketers-free-email-course/","http://bit.ly/firecartx","https://twitter.com/EvanSinar/status/596758897223966720","http://bit.ly/GroBGH","http://dld.bz/dw3hS","http://bit.ly/growth00a","https://twib.in/l/85p4pBzogyX","http://buff.ly/1DN8f2o","http://ift.tt/1ALuWnH","http://buff.ly/1EP6uXH","http://ift.tt/1cwHTg7","http://buff.ly/1F9n070","https://twitter.com/Teresa_Eme/status/596381538679271425","http://ow.ly/MGKOz","http://ecommerce.visicomscientific.com/","http://rbl.ms/1EUMYYO","http://bit.ly/1vBhXrZ","http://Salesforce.com","https://twib.in/l/KrkpozBKrkK","http://bit.ly/1nxeQWP","https://twitter.com/chuckaikens/status/596751952643493888","http://bit.ly/1IpuDp7","https://twitter.com/chuckaikens/status/596797244814323712","http://buff.ly/1I5LdKu","https://twitter.com/EvanSinar/status/596795558611832834","http://buff.ly/1JRsgx8","http://ift.tt/1F4tKRD","http://www.fastcompany.com/3045934/passion-to-profit/how-to-go-from-idea-to-prototype-in-one-day","https://twitter.com/releaseman/status/596821892813758466","http://bit.ly/1Qurbwf","http://www.jeffbullas.com/2015/04/01/5-cool-web-analytics-tools-to-spy-on-your-website-visitors-and-customers/","https://growthhackers.com/utilize-data-optimize-stores-shopping-experience/","http://buff.ly/1JRscO6","http://bit.ly/1zLu0Vl","http://buff.ly/1chFeXA","http://buff.ly/1ztqPfD","http://www.growthhackers.com/?p=399","http://buff.ly/1FQ7hZe","https://twitter.com/gauravwadekar/status/596800534222364672","http://www.rtforanxiety.com/#!When-To-Outsource-Your-Business-Needs/c102s/554aad670cf23d01647a89b4","http://ift.tt/1JwufDZ","http://www.WhistlerHQ.com","http://kcy.me/234tr","http://bit.ly/1IV1any","http://www.huffingtonpost.com/brett-relander/are-you-missing-something_b_7028506.html?utm_campaign=naytev&utm_content=554caadce4b04881410062e6","http://buff.ly/1CR2XZR","http://wifiwhale.com","http://kcy.me/234ty","https://twitter.com/GrowthHackers/status/596716454537535489","http://bit.ly/1JRsepd","http://bit.ly/1zKsLpo","http://growthhackerkit.com/","https://twitter.com/Jakeliddell/status/596721425299406849","http://scoopnest.com","https://twitter.com/releaseman/status/596721175436390401","http://scotforshaw.blogspot.com/2015/02/is-software-as-service-saas-answer-to.html","https://twitter.com/skarritt/status/596724884283072512","http://kcy.me/234tx","https://twitter.com/Timothy_Hughes/status/596800009493938176","https://twib.in/l/5EKdBKyeMXB","http://buff.ly/1IhlbE8","http://bit.ly/1IoWZ2K","http://bit.ly/1H6Bk0v","http://buff.ly/1DNcnzA","http://buff.ly/1JS7IVv","https://twib.in/l/KrkXXoML9y7","https://twitter.com/GrowthHackers/status/596711459851239424","http://bit.ly/1y9UtL9","https://twitter.com/GrowthHackers/status/596721586729832448","http://growthhackers.com/?p=756","http://ift.tt/1F4xKln","https://twitter.com/31WestGlobal/status/596011659266756608","https://twitter.com/HDScorp/status/596797214132961280","https://twitter.com/31WestGlobal/status/596721474716696579","https://twitter.com/hichamchraibi/status/596821357255462912","http://bit.ly/1E9T4C6","https://twitter.com/KWalshPhillips/status/596721297217978368","https://twitter.com/akashbad/status/596470847881289730","https://twitter.com/MeghanMBiro/status/596737103456817152","https://twitter.com/ambarmstrong/status/596790507147137024","https://twitter.com/releaseman/status/596801748704038913","http://buff.ly/1EivYsQ","http://ow.ly/MuyL1","https://twitter.com/chuckaikens/status/596706665354895360","http://kcy.me/234tu","https://twitter.com/chuckaikens/status/596721769001656320","https://twitter.com/Timothy_Hughes/status/596734190885937152","http://list.ly/list/fzJ-27-awesome-backlink-tools","http://kcy.me/234tw","http://bit.ly/1H3SX0S","http://tiny.cc/gskbux","http://ow.ly/MBdg8"];



    def parse(self, response):
        # create title
        title = response.xpath('//title/text()').extract()[0]
        try:
            tit = clean_up( title )
        except:
            import sys
            print "Unexpected error:", sys.exc_info()[0]
            print(type(title))
            raise
        # now create one long line for the body text
        res = response.xpath('//*[self::h1 or self::h2 or self::h3 or self::h4 or self::p[string-length(text()) > 50]]/text()').extract()
        reslis = []
        for i in res:
            reslis.append(clean_up(i))
        # create a string out of the response
        output = ' '.join(reslis)
        # finally, for url create its own
        url = clean_up(response.url)
        #strip_pattern = "www|https|http|[\/|.|:|?|=|_|&|#|!]+"
        #fn_cand = re.sub(strip_pattern, '', url)
        with open('results/urls.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            # writer.writerow(['original_url', 'redirected_url', 'title', 'contents'])
            writer.writerow([url.encode('ascii', 'ignore'), clean_up(tit).encode('ascii', 'ignore'), clean_up(output).encode('ascii', 'ignore')])
        # filename = response.url.split("/")[-2] + '.html'
        # with open('results/'+fn_cand+'.txt', 'wb') as f:
        #     f.write(output)
