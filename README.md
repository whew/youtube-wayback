# youtube-wayback
Check if YouTube videos are archived in the Wayback Machine

### Usage
```python3 youtube_wayback.py [-x URL] URL [URL ...]```

#### Options
* `-x`, `--proxy` URL of the proxy server to use

### Example usage
```
$ python3 youtube_wayback.py jNQXAC9IVRw 022CdArz5oM youtube.com/watch?v=yBszWsBPpLs youtu.be/Ji9KmXwrA5Y
jNQXAC9IVRw https://web.archive.org/web/20070601075850oe_/http://sjl-casing1.sjl.youtube.com/get_video?video_id=jNQXAC9IVRw
022CdArz5oM https://web.archive.org/web/20201017214117oe_/https://r1---sn-a5meknle.googlevideo.com/videoplayback?expire=1602992476&ei=_GSLX82YDpStkwaTs7LwAQ&ip=207.241.231.174&id=o-AKI920pQSSaS98mr-nFu9_imLXjUw1f2ejXwGG51PAeC&itag=22&source=youtube&requiressl=yes&pcm2=no&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=14.582&lmt=1602969775478212&fvip=1&fexp=23915654&c=WEB&txp=5416222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRAIgUPptk4-03aLj5gTqjznbZdXDGY4bHR8CNscDJYte4YUCIFRgD5zVvqc7VhoWhzLSCLkntl42GErTDliqapeE0Piq&video_id=022CdArz5oM&redirect_counter=1&cm2rm=sn-n4vll7e&req_id=faf1c4796e80a3ee&cms_redirect=yes&mh=i5&mm=34&mn=sn-a5meknle&ms=ltu&mt=1602970821&mv=m&mvi=1&pl=20&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRAIgTDVl58twhmU6QL3XUnC0iQVT1G9aabQ9a-VeUvb7JMICIF5Ii99Uqoq0FlEieFzwFYoAoahbydMwsY5bmtBfht98
yBszWsBPpLs 404
Ji9KmXwrA5Y https://web.archive.org/web/20150828172651oe_/https://r19---sn-nwj7knek.googlevideo.com/videoplayback?ratebypass=yes&signature=B09818D4BEFCCD93F0ED4BAE1F41482511919409.34B4235A9F2DBC67B790ACA6D0E37FE783575754&upn=eNWrouTmZig&itag=22&key=yt5&lmt=1440736302225356&ipbits=0&fexp=9407992%2C9408710%2C9409069%2C9409115%2C9413121%2C9415365%2C9415435%2C9415485%2C9415943%2C9416023%2C9416126%2C9416837%2C9416916%2C9417707%2C9418153%2C9418448%2C9418504%2C9418919%2C9419167%2C9419445%2C9419788%2C9419801%2C9420022&mime=video%2Fmp4&id=o-AKtVVsmy0CFXa32KQJk9z_MjGx80ZU_rWNDodUE0aEJX&pl=20&mm=31&mn=sn-nwj7knek&ms=au&mt=1440782687&mv=m&ip=207.241.229.47&requiressl=yes&initcwndbps=6780000&dur=129.381&expire=1440804409&sver=3&sparams=dur%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cupn%2Cexpire&source=youtube&signature=
```
