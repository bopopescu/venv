import re
mytext = " Vasya a;lsdk;al 1234 a;lsd kjlasjd alsdj;ladn Koly vasya aldjla "\
    "aslkdjlsadj kolya sad vasya uiasd@mail.ru asdj lasdkj aksjd kjsadh kjasdlas as kd;sad 1233 "\
    "hello asd  yandex asd vasya alsdk jalskjd asdalksjdla aksjdlkj googgle.com alsdkjla jdla"\
    "lksajd lkjd as yandex lksajd liew qo dlksa jlakd jlaksjdoiwq lkjds as kdjlasd yandex alsdj"\
    "lakjsd oi! asdas# alkd jlksadj 12321432423 bigt@i.ua"
""""
\d = any digit 0-9
\D = any symbols now Digit
\w = any alphabet symbols [A-Z, a-z]
\W = Any non Alpabet symbols
\s = breakspace
\S = non breakspace

[0-9]{4}
[A-Z]
"""


textlook = r"yandex"
allresult = re.findall(textlook, mytext)

print(allresult)

textlook1 = r"[0-9]{4}"
allresult = re.findall(textlook1, mytext)
print(allresult)

textlook2 = r"\w{6}\s"
allresult = re.findall(textlook2, mytext)

print(allresult)


textlook3 = r"[A-Z][a-z]+"
allresult = re.findall(textlook3, mytext)

print(allresult)

textlook4= r"\w+\@\w+\.\w+"
allresult = re.findall(textlook4,mytext)

print(allresult)