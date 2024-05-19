The challeng was a gif file which display qr codes 

![QRRR-ezgif com-animated-gif-maker](https://github.com/AbdullahAlTalaq/MySolvedCTFs/assets/99118138/9020387f-d4a5-40f7-b364-376ea6ec5df7)

so we can assume that we can get the flag by scan one of these qr code and the name of the challange was qrr and forensic so all this make our assumation strong.

I vist web site that can caputer each frame and thats what I found 
![1](https://github.com/AbdullahAlTalaq/MySolvedCTFs/assets/99118138/bcf4ae99-a146-493f-ae0b-422fe96e9587)

The web give me Direct link to each frame which contains the qr code 

and by writng simple py script we can git all the qr codes as links 


using this web site to get each frame of the gif https://picasion.com/split-animated-gif/

#!/usr/bin/python3

base_url = "https://i.picasion.com/sp/92/4Iq8/{}.gif"


for num in range(1, 66):
    gif_url = base_url.format(num)
    print(gif_url)
--------------------
this was the output 
 "https://i.picasion.com/sp/92/4Iq8/1.gif",
    "https://i.picasion.com/sp/92/4Iq8/2.gif",
    "https://i.picasion.com/sp/92/4Iq8/3.gif",
    "https://i.picasion.com/sp/92/4Iq8/4.gif",
    "https://i.picasion.com/sp/92/4Iq8/5.gif",
    "https://i.picasion.com/sp/92/4Iq8/6.gif",
    "https://i.picasion.com/sp/92/4Iq8/7.gif",
    "https://i.picasion.com/sp/92/4Iq8/8.gif",
    "https://i.picasion.com/sp/92/4Iq8/9.gif",
    "https://i.picasion.com/sp/92/4Iq8/10.gif",
    "https://i.picasion.com/sp/92/4Iq8/11.gif",
    "https://i.picasion.com/sp/92/4Iq8/12.gif",
    "https://i.picasion.com/sp/92/4Iq8/13.gif",
    "https://i.picasion.com/sp/92/4Iq8/14.gif",
    "https://i.picasion.com/sp/92/4Iq8/15.gif",
    "https://i.picasion.com/sp/92/4Iq8/16.gif",
    "https://i.picasion.com/sp/92/4Iq8/17.gif",
    "https://i.picasion.com/sp/92/4Iq8/18.gif",
    "https://i.picasion.com/sp/92/4Iq8/19.gif",
    "https://i.picasion.com/sp/92/4Iq8/20.gif",
    "https://i.picasion.com/sp/92/4Iq8/21.gif",
    "https://i.picasion.com/sp/92/4Iq8/22.gif",
    "https://i.picasion.com/sp/92/4Iq8/23.gif",
    "https://i.picasion.com/sp/92/4Iq8/24.gif",
    "https://i.picasion.com/sp/92/4Iq8/25.gif",
    "https://i.picasion.com/sp/92/4Iq8/26.gif",
    "https://i.picasion.com/sp/92/4Iq8/27.gif",
    "https://i.picasion.com/sp/92/4Iq8/28.gif",
    "https://i.picasion.com/sp/92/4Iq8/29.gif",
    "https://i.picasion.com/sp/92/4Iq8/30.gif",
    "https://i.picasion.com/sp/92/4Iq8/31.gif",
    "https://i.picasion.com/sp/92/4Iq8/32.gif",
    "https://i.picasion.com/sp/92/4Iq8/33.gif",
    "https://i.picasion.com/sp/92/4Iq8/34.gif",
    "https://i.picasion.com/sp/92/4Iq8/35.gif",
    "https://i.picasion.com/sp/92/4Iq8/36.gif",
    "https://i.picasion.com/sp/92/4Iq8/37.gif",
    "https://i.picasion.com/sp/92/4Iq8/38.gif",
    "https://i.picasion.com/sp/92/4Iq8/39.gif",
    "https://i.picasion.com/sp/92/4Iq8/40.gif",
    "https://i.picasion.com/sp/92/4Iq8/41.gif",
    "https://i.picasion.com/sp/92/4Iq8/42.gif",
    "https://i.picasion.com/sp/92/4Iq8/43.gif",
    "https://i.picasion.com/sp/92/4Iq8/44.gif",
    "https://i.picasion.com/sp/92/4Iq8/45.gif",
    "https://i.picasion.com/sp/92/4Iq8/46.gif",
    "https://i.picasion.com/sp/92/4Iq8/47.gif",
    "https://i.picasion.com/sp/92/4Iq8/48.gif",
    "https://i.picasion.com/sp/92/4Iq8/49.gif",
    "https://i.picasion.com/sp/92/4Iq8/50.gif",
    "https://i.picasion.com/sp/92/4Iq8/51.gif",
    "https://i.picasion.com/sp/92/4Iq8/52.gif",
    "https://i.picasion.com/sp/92/4Iq8/53.gif",
    "https://i.picasion.com/sp/92/4Iq8/54.gif",
    "https://i.picasion.com/sp/92/4Iq8/55.gif",
    "https://i.picasion.com/sp/92/4Iq8/56.gif",
    "https://i.picasion.com/sp/92/4Iq8/57.gif",
    "https://i.picasion.com/sp/92/4Iq8/58.gif",
    "https://i.picasion.com/sp/92/4Iq8/59.gif",
    "https://i.picasion.com/sp/92/4Iq8/60.gif",
    "https://i.picasion.com/sp/92/4Iq8/61.gif",
    "https://i.picasion.com/sp/92/4Iq8/62.gif",
    "https://i.picasion.com/sp/92/4Iq8/63.gif",
    "https://i.picasion.com/sp/92/4Iq8/64.gif",
    "https://i.picasion.com/sp/92/4Iq8/65.gif",
--------------------

I tryed to make simple script that sending all these to "https://blog.qr4.nl/Online-QR-Code-Decoder.aspx" that can read it and extract the contant for all of these qr codes
check webscraper.py 
but It did not work maybe something wrong with post and requst with this web.. I tryed to find anthor web tool but I get alternative idea
Which is download all these images and save it and extract it by cyberchif
check Download.py 
I get all images qr saved in newfolder and I send them all to cyber chif 
see the cyber chif attmept 
[https://gchq.github.io/CyberChef/#recipe=Parse_QR_Code(false/disabled/breakpoint)ROT13(true,true,false,13)&input=U3ludEx7bmZ4cWNibnhxXzY2NzY1X2ZicXZzNjY2NiF9DQpTeW50THticWZjMnRxZnFzZnEhfQ0KU3ludEx7YnFmYzJ0](https://gchq.github.io/CyberChef/#recipe=Parse_QR_Code(false/disabled/breakpoint)ROT13(true,true,false,13)&input=U3ludEx7bmZ4cWNibnhxXzY2NzY1X2ZicXZzNjY2NiF9DQpTeW50THticWZjMnRxZnFzZnEhfQ0KU3ludEx7YnFmYzJ0cSF9DQpTeW50THtxYm5mY2J4cWZuNyF9DQpTeW50THtsbmZjcXhiY2ZueHFjYm54cWY2IX0NClN5bnRMe2FiZ19ndXJfc3lubm5ubm5ubm5ubm50dHR0dCF9DQpTeW50THtreHFzeGJmY3hzZmJfZnFmcWZxZnFmcXFmcWYhfQ0KU3ludEx7Zm55cW5iZnhxZm5jYnhxbm5iZmN4cSF9DQpTeW50THthYmdfZ3VyX3N5bnRfam55eW51IX0NClN5bnRMe3Fmc3R1Z3RzdHNxZnJfc3MhfQ0KU3ludEx7bmNmeGJxY254ZnFfdnFmbndxczU2IX0NClN5bnRMe1BiYXRlbmdmX2hfdGJnX3ZnZ2d9DQpTeW50THt3dXhxeXNmcXluX2ZxY2JmcWNxZl81Njc4NzY1cXFxcSF9DQpTeW50THtuY2ZxeDdjNmpieGZfcWJmd3M2X3FidmZ3cWJ2c3dmIX0NClN5bnRMe3Z2ZnFzZnFfeHFmd3hmcV9xd2ZxZiF9DQpTeW50THtmeHdxeHdmX3FmYnFfcWZzd2Zxc2YhfQ0KU3ludEx7cXN0cXRzcXR2ZXdyZV9xdmZxY3NfcXNxcyF9DQpTeW50THtuYmZjeHFjYmZueHFfZnZicXN3ZnFzZmJxc19mYmJiYnJycnJyX19fcnZzd2JudmZ3IX0NClN5bnRMe3FibmZ4cWNibmZ4cW5meHFjYm5mX25iZnF3Zm52d3FibnZmd3Fidl9uZmZmbmZmIX0&ieol=CRLF&oeol=CRLF)


![22](https://github.com/AbdullahAlTalaq/MySolvedCTFs/assets/99118138/fb808093-b8dd-45a8-9e09-5a6526e8ded1)


and I get these text from the images without consider the dublicates 
SyntL{nfxqcbnxq_66765_fbqvs6666!}
SyntL{bqfc2tqfqsfq!}
SyntL{bqfc2tq!}
SyntL{qbnfcbxqfn7!}
SyntL{lnfcqxbcfnxqcbnxqf6!}
SyntL{abg_gur_synnnnnnnnnnnnttttt!}
SyntL{kxqsxbfcxsfb_fqfqfqfqfqqfqf!}
SyntL{fnyqnbfxqfncbxqnnbfcxq!}
SyntL{abg_gur_synt_jnyynu!}
SyntL{qfstugtstsqfr_ss!}
SyntL{ncfxbqcnxfq_vqfnwqs56!}
SyntL{Pbatengf_h_tbg_vggg}
SyntL{wuxqysfqyn_fqcbfqcqf_5678765qqqq!}
SyntL{ncfqx7c6jbxf_qbfws6_qbvfwqbvswf!}
SyntL{vvfqsfq_xqfwxfq_qwfqf!}
SyntL{fxwqxwf_qfbq_qfswfqsf!}
SyntL{qstqtsqtvewre_qvfqcs_qsqs!}
SyntL{nbfcxqcbfnxq_fvbqswfqsfbqs_fbbbbrrrrr___rvswbnvfw!}
SyntL{qbnfxqcbnfxqnfxqcbnf_nbfqwfnvwqbnvfwqbv_nfffnff!} 

It apper that it needs some shifting .. I used ROT13 and I get thses flags 

FlagY{askdpoakd_66765_sodif6666!}
FlagY{odsp2gdsdfsd!}
FlagY{odsp2gd!}
FlagY{doaspokdsa7!}
FlagY{yaspdkopsakdpoakds6!}
FlagY{not_the_flaaaaaaaaaaaaggggg!}
FlagY{xkdfkospkfso_sdsdsdsdsddsds!}
FlagY{saldaoskdsapokdaaospkd!}
FlagY{not_the_flag_wallah!}
FlagY{dsfghtgfgfdse_ff!}
FlagY{apskodpaksd_idsajdf56!}
FlagY{Congrats_u_got_ittt}
FlagY{jhkdlfsdla_sdposdpds_5678765dddd!}
FlagY{apsdk7p6woks_dosjf6_doisjdoifjs!}
FlagY{iisdfsd_kdsjksd_djsds!}
FlagY{skjdkjs_dsod_dsfjsdfs!}
FlagY{dfgdgfdgirjer_disdpf_dfdf!}
FlagY{aospkdposakd_siodfjsdfsodf_sooooeeeee___eifjoaisj!}
FlagY{doaskdpoaskdaskdpoas_aosdjsaijdoaisjdoi_asssass!}

that was the right flag :FlagY{Congrats_u_got_ittt}

-------------------------------------------
Thank you for reading 
Abdullah Al Talaq
