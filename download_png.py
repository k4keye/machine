import urllib.request

'''
url ="http://uta.pw/shodou/img/28/214.png"
savename="test.png"

#파일다운로드 1(URL , 저정이름) 
#urllib.request.urlretrieve(url,savename)

#파일다운로드 2(바이너리로 읽어서 저장) 
mem = urllib.request.urlopen(url).read()
with open(savename,mode="wb") as f:
    f.write(mem)
    print("저장되었습니다.")

#텍스트 읽기
url ="https://www.naver.com/"
mem = urllib.request.urlopen(url).read()
#print(mem) 그냥 출력
print(mem.decode("utf-8")) # 디코딩 하여 출력

'''


#책예제
url ="http://api.aoikujira.com/ip/ini"
mem = urllib.request.urlopen(url).read()
print(mem.decode("utf-8"))