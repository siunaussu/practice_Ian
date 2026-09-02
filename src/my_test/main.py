import re
import base64
import requests

def post_json(url: str, payload: dict,  cookies: dict, timeout: int = 10):
    """post json 请求极简模板"""
    try:
        resp = requests.post(
            url=url,
            json=payload,  # 自动设置 Content‑Type: application/json
            timeout=timeout,
            cookies= cookies
        )
        resp.raise_for_status()  # http状态码非2xx直接抛异常
        return resp.json()       # 返回解析后的dict
    except requests.exceptions.RequestException as e:
        print(f"请求异常: {e}")
        return None

def http_get(url, cookies, params=None):
    """
    极简get请求
    :param url: 请求地址
    :param params: get查询参数，字典格式
    :return: response对象
    """
    resp = requests.get(url, cookies=cookies, params=params, timeout=10)
    resp.raise_for_status()  # 状态码非200直接抛异常
    return resp


if __name__ == '__main__':
    urls = ["https://meeting.tencent.com/cw/KWPzaP4V51","https://meeting.tencent.com/cw/2p9p1LoQf3","https://meeting.tencent.com/cw/KWPjwWDJf9","https://meeting.tencent.com/cw/Km9w1Vkx5d","https://meeting.tencent.com/cw/lvXPB5OAea","https://meeting.tencent.com/cw/KnOM7RX79e","https://meeting.tencent.com/cw/KELGk43wfc","https://meeting.tencent.com/cw/KwzqPq7005","https://meeting.tencent.com/cw/2V4aYjyvcd","https://meeting.tencent.com/cw/l5EnMobZ48","https://meeting.tencent.com/cw/NQnzdwXR2b","https://meeting.tencent.com/cw/K0RBzApbc5","https://meeting.tencent.com/cw/KwzBAmW0b0","https://meeting.tencent.com/cw/l6MAD5goa0","https://meeting.tencent.com/cw/2OzRWr60d5","https://meeting.tencent.com/cw/2ZGbpd0E93","https://meeting.tencent.com/cw/Nbn6ZYn55b","https://meeting.tencent.com/cw/lJOVjLzJb8","https://meeting.tencent.com/cw/NgXq5Dwgd1","https://meeting.tencent.com/cw/K0RJaM6G67","https://meeting.tencent.com/cw/KwzbB6Vkb1","https://meeting.tencent.com/cw/2ZGvLQ0E45","https://meeting.tencent.com/cw/2qYeZYgg8f","https://meeting.tencent.com/cw/l6MxAjxZ69","https://meeting.tencent.com/cw/Kwza199k41","https://meeting.tencent.com/cw/2Oz5pQE7fd","https://meeting.tencent.com/cw/lvW0MDnA3e","https://meeting.tencent.com/cw/23v8kv0maf","https://meeting.tencent.com/cw/2MG1qV5512","https://meeting.tencent.com/cw/29e1P7Qbd0","https://meeting.tencent.com/cw/29ek51QQ7b","https://meeting.tencent.com/cw/N1e1Rr1m85","https://meeting.tencent.com/cw/2V4qe6Jdeb","https://meeting.tencent.com/cw/K0Rjdd5b6e","https://meeting.tencent.com/cw/23voPmeB8f","https://meeting.tencent.com/cw/KELv3JxDfa","https://meeting.tencent.com/cw/2rV0AQGVf3","https://meeting.tencent.com/cw/l5L1DJJD14","https://meeting.tencent.com/cw/NAXGAWVM7e","https://meeting.tencent.com/cw/2rDxX98X6c","https://meeting.tencent.com/cw/Km7VDV3wfd","https://meeting.tencent.com/cw/Km7Db1kxf5","https://meeting.tencent.com/cw/2yQX8ZyMbc","https://meeting.tencent.com/cw/No77ngx521","https://meeting.tencent.com/cw/ldDyxrRm8b","https://meeting.tencent.com/cw/2rDwQnpJ74","https://meeting.tencent.com/cw/KWmLAxwA85","https://meeting.tencent.com/cw/2pyQZmPQc0","https://meeting.tencent.com/cw/N8A1yXA041","https://meeting.tencent.com/cw/NxQA86r956","https://meeting.tencent.com/cw/2yQ3Z3zr87","https://meeting.tencent.com/cw/KnVzeeP9db","https://meeting.tencent.com/cw/2V8BbP6P39","https://meeting.tencent.com/cw/29bW4Amq51","https://meeting.tencent.com/cw/N1xa1Q1314","https://meeting.tencent.com/cw/24kje8Lrf2","https://meeting.tencent.com/cw/KnVpGMqG0f","https://meeting.tencent.com/cw/2B9m4GWmcf","https://meeting.tencent.com/cw/l6A5gLJe17","https://meeting.tencent.com/cw/2aDzE7r8ca","https://meeting.tencent.com/cw/2V8M1v9P55","https://meeting.tencent.com/cw/24k7n3arf5","https://meeting.tencent.com/cw/Kzk4Zz360c","https://meeting.tencent.com/cw/KeDvOM5k92","https://meeting.tencent.com/cw/N8AmYO34db","https://meeting.tencent.com/cw/l6ALAD0o77","https://meeting.tencent.com/cw/2MjQDMnZef","https://meeting.tencent.com/cw/2Mja5MGP4d","https://meeting.tencent.com/cw/KWAM85PEc1","https://meeting.tencent.com/cw/l5m1Oo3V63","https://meeting.tencent.com/cw/l5mne4Br5f","https://meeting.tencent.com/cw/2qxvGP9R90","https://meeting.tencent.com/cw/KWARbmvB99","https://meeting.tencent.com/cw/NXbPee6z21","https://meeting.tencent.com/cw/l5mEvxogb1","https://meeting.tencent.com/cw/2ORexm438d"]
    for url in urls:
        data = {
            "web_uid": "40bac880-b1e6-482b-8629-ed5012a14278",
            "landing_url": "https://meeting.tencent.com/",
            "landing_path": "https://meeting.tencent.com/",
            "landing_referralurl": "https://www.google.com.hk/",
            "landing_referraldomain": "https://www.google.com.hk",
            "_ga": "GA1.1.1573161935.1768821572",
            "_qimei_uuid42": "1a80e091c2c100eae136f5fd8b6f60d1e74c14876c",
            "_qimei_q36": "",
            "_qimei_h38": "0800f563e136f5fd8b6f60d102000007d1a80e",
            "we_meet_token": "eJx0kc1y2jAUhd9F25YiCVmymekiSUtpHUgYAgY2HtmSGdX-*onrdPruHcBM6KJanvON7j33-AYvj*tPqjKWV6mMlQBT4IGPZ5U3TezOCqI*xPDyiMeoBxEJPDRwRuTxiT2jE4QJxczzB1P*apSWMc*s1GAKKCQ*hIP3KrVRdQWmAENMoI-JacBgJs6oShoDpqCTySBaVcrTPsynlMEAX1ct6qOqYts38ox3tc4HR8hXdQ02SFoeL1N9ek2gjmAKXqiz4umNh7OejctwHezaXvwI3f08qDNVqvzbbv6hgHAeLWbSFGh336GfS-qUb4q3r4j16M6O*f6Qfgkbd2cdwVnq6U23cmWUI-7Yz0mfR6t*bbfhYum6Imtmz130UB-Gm**RCesN4yt78Ert7yl9Vu1xv*4WHd6oZELbbfSwZDOvcqTdhvvPN6e-jdaqUqoJfRcaXQuX2n8gc*k0S3zOGBklxBcjkgTZiIt0MiJUQEJZwFP0fh4x0Tcf8DStXWXjtNb-ad0Zqa91YPDnbwAAAP--oEq3Xg__",
            "account_corp_id": "312462758",
            "corp_id": "312462758",
            "app_uid": "16802000000045765014951",
            "token_expire_time": "1787275725",
            "user_type": "2",
            "ACTIVITY_TICKET": "eJxMUtuSmkAU-Jd5TSo7N2aAqjxkXRNRVkvUdbMvFAsHmMhNLqKk8u%2Ap1WFL3k43Xd3T5-xFW3fzLQjDsitav71UgGyEvl5RFUHRqlhBjWzECOWCSsP0iTAxxbePG1IYmHDLIFoUVJWK-KD1WR0hG2ENN9HBv1LIRgQTKS2LMc3BuVI1%2AEHcXp2IiUfVCepGlQWyEcWUY5PyD1NNtir-CEukKYTEFjU0npWJKsan9NCX9WEMoRJkI3e3nTwRS3mbbNMvmqMzF41bmAmPLsP0URSzfffGoWsOGWS-hlU29WbDJZ1-WRzVG3jS9ZYraFIqFmTVBd5kmQd7h-x8HMjlvF9Hz3m6MZ55Pt-265eXKd-F1uuppE35lC8z-OBQydn7n8n09aF%2A6Jtz7qTLdXL0kt98O5msdw7MBszNdOrGKv3xXQevIbnVoOcITioE-9rmXcH3c1seoPA-hcmg8aPKQTFxJ7ztxORxTKURsDjikoD1zkMhLEzMkDGG%2AbhdfShhWVc3u8%2A70H90DdRj%2ART9%2Ax8AAP--jCm05g__",
            "_ga_RPMZTEBERQ": "GS2.1.s1786670908$o2$g1$t1786670925$j43$l0$h0",
            "lz_appid": "312462758",
            "lz_uid": "16802000000045765014951",
            "_qimei_i_3": "7ffa4d8b9509018a9493fc615a8471e8a6eaa1f0165856d1e58f7d5e7392213a683265943989e2b4d291",
            "hy_anon_user": "a_meeting_open_id_8b5c196b742540e5996f6e307c807f8c",
            "hy_source": "web",
            "lz_sign": "b7qZmyMevKAVGSwqLvIAQ8F0SNmX3WhLYDOEy8AlDn8PAK3fAgVVYTNIVTzDzHOBuc60Ef7V1-NXaSVlrESSHGYi2VGHtzjnNlVUsncXv-c",
            "lz_time": "1786689239107",
            "_qimei_fingerprint": "596ba86e292a94d99b975450d7ac04cc",
            "_gcl_au": "1.1.420275060.1786693018",
            "_ga_6WSZ0YS5ZQ": "GS2.1.s1786693265$o1$g0$t1786693265$j60$l0$h0",
            "lz_expire": "1786711369136",
            "_qimei_i_1": "70bc7a829d5a508dc491fd655a8775b6f2b8f0f9405d5584b4db29582493206c616330c139d8eadc83b0ece5",
            "hy_anon_token": "8tE8bq6InCxff5mUqQZfc9aGHP6NPD80Cr/k258SiLJ9CYW8HiMzU5pREYyvnbvj0BG1Q9/KnkehH1aSnt0onsNBIbySGO3JvjToZbIP+3GSrmyTOVg++T/m/xSnFwk/B10kOImjhshjUW4cevfYKIuuseR6aAov68SyU7i17gLVyaZwRJTzmrGOpeW5XXNPnhHhk8MWtuK4tvKFGaO80MbXje6a4PyXtGfYzq1HpT7JqU7Act67XIdNY+1rZCPhhXt6nvLrby+tDVTDWPB9MY/FbGpMtZqhsNMHjmPtW9tterIZFV/Xxub8c2JKJsLb1C3Xtru4tGCU9rla69AXVcs7NS8OLG3kQZ85waOMVp2/+66cEh2vIinRVkb0Mpe4X34ILT2QQuJCO15atzxg5TYXvnOosz6NAZu2Y5nGWTymINR/bCYuq1sR2r3N9IMachs3vXkh/I6LaOZV+X1pLS6jeKakVHzmmssS6a4k/plbykNTaYb7XltvKW6uBYpJGCWN+qZS9Tw6uZ2QYxYamxElwvEC9kKZHLKab9U3ZT6xVv6xRDRue6uRGrUlw7BKWzC2gGQ1WBc+i2hSfgoCajqn9nwydqSLUXAEEzS6TANy1immon7F42T5+O9fMNGGZD8rJraC/VuP0vlheuYfQg==",
            "_ga_6P1G7NCG3R": "GS2.1.s1786693017$o3$g1$t1786693597$j60$l0$h805440173"
        }
        res = http_get(url, cookies=data)
        share_id = re.search(r'(?<=:\\"id=)[0-9a-f\-]+', res.text).group()
        subject = re.search(r'\\"subject\\":\\"(.*?)\\",\\"origin_subject', res.text).group(1)
        raw_bytes = base64.b64decode(subject)
        subject_result = raw_bytes.decode("utf-8")
        print(share_id,subject_result)

        # 申请权限
        api_url = "https://meeting.tencent.com/wemeet-tapi/v2/meetlog/permission/record-apply?c_app_id=&c_os_model=web&c_os=web&c_os_version=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F151.0.0.0%20Safari%2F537.36&c_timestamp=1786687796809&c_nonce=2Zytt7Cp5&c_app_version=&c_instance_id=5&rnds=2Zytt7Cp5&c_district=0&platform=Web&c_app_uid=&c_account_corp_id=312462758&trace-id=47efcd1881dcc760c3377581886f7725&c_lang=zh-CN"
        body = {
            "apply_type": 2,
            "is_meetlog": False,
            "reason": "你好，我是夷定昌，请帮我开通查看权限。",
            "share_id": share_id,
            "subject": subject_result
        }
        cookies = {
            "web_uid": "40bac880-b1e6-482b-8629-ed5012a14278",
            "landing_url": "https://meeting.tencent.com/",
            "landing_path": "https://meeting.tencent.com/",
            "landing_referralurl": "https://www.google.com.hk/",
            "landing_referraldomain": "https://www.google.com.hk",
            "_ga": "GA1.1.1573161935.1768821572",
            "_qimei_uuid42": "1a80e091c2c100eae136f5fd8b6f60d1e74c14876c",
            "_qimei_fingerprint": "2ea5fb46f867b1c360e387fe3df6749d",
            "_qimei_q36": "",
            "_qimei_h38": "0800f563e136f5fd8b6f60d102000007d1a80e",
            "we_meet_token": "eJx0kc1y2jAUhd9F25YiCVmymekiSUtpHUgYAgY2HtmSGdX-*onrdPruHcBM6KJanvON7j33-AYvj*tPqjKWV6mMlQBT4IGPZ5U3TezOCqI*xPDyiMeoBxEJPDRwRuTxiT2jE4QJxczzB1P*apSWMc*s1GAKKCQ*hIP3KrVRdQWmAENMoI-JacBgJs6oShoDpqCTySBaVcrTPsynlMEAX1ct6qOqYts38ox3tc4HR8hXdQ02SFoeL1N9ek2gjmAKXqiz4umNh7OejctwHezaXvwI3f08qDNVqvzbbv6hgHAeLWbSFGh336GfS-qUb4q3r4j16M6O*f6Qfgkbd2cdwVnq6U23cmWUI-7Yz0mfR6t*bbfhYum6Imtmz130UB-Gm**RCesN4yt78Ert7yl9Vu1xv*4WHd6oZELbbfSwZDOvcqTdhvvPN6e-jdaqUqoJfRcaXQuX2n8gc*k0S3zOGBklxBcjkgTZiIt0MiJUQEJZwFP0fh4x0Tcf8DStXWXjtNb-ad0Zqa91YPDnbwAAAP--oEq3Xg__",
            "account_corp_id": "312462758",
            "corp_id": "312462758",
            "app_uid": "16802000000045765014951",
            "token_expire_time": "1787275725",
            "user_type": "2",
            "ACTIVITY_TICKET": "eJxMUtuSmkAU-Jd5TSo7N2aAqjxkXRNRVkvUdbMvFAsHmMhNLqKk8u%2Ap1WFL3k43Xd3T5-xFW3fzLQjDsitav71UgGyEvl5RFUHRqlhBjWzECOWCSsP0iTAxxbePG1IYmHDLIFoUVJWK-KD1WR0hG2ENN9HBv1LIRgQTKS2LMc3BuVI1%2AEHcXp2IiUfVCepGlQWyEcWUY5PyD1NNtir-CEukKYTEFjU0npWJKsan9NCX9WEMoRJkI3e3nTwRS3mbbNMvmqMzF41bmAmPLsP0URSzfffGoWsOGWS-hlU29WbDJZ1-WRzVG3jS9ZYraFIqFmTVBd5kmQd7h-x8HMjlvF9Hz3m6MZ55Pt-265eXKd-F1uuppE35lC8z-OBQydn7n8n09aF%2A6Jtz7qTLdXL0kt98O5msdw7MBszNdOrGKv3xXQevIbnVoOcITioE-9rmXcH3c1seoPA-hcmg8aPKQTFxJ7ztxORxTKURsDjikoD1zkMhLEzMkDGG%2AbhdfShhWVc3u8%2A70H90DdRj%2ART9%2Ax8AAP--jCm05g__",
            "_ga_RPMZTEBERQ": "GS2.1.s1786670908$o2$g1$t1786670925$j43$l0$h0",
            "lz_sign": "kxQXwT7PijjlvvAVzRwKf_Barg6vUpPt8YmMom6gSTzpVAXG7USqd9cyfebebWzKKLzwp1QNettXFFJgze0OkxpYos2_w7RsOLKtKqanIZM",
            "lz_appid": "312462758",
            "lz_uid": "16802000000045765014951",
            "lz_time": "1786670925552",
            "_qimei_i_3": "7ffa4d8b9509018a9493fc615a8471e8a6eaa1f0165856d1e58f7d5e7392213a683265943989e2b4d291",
            "hy_anon_user": "a_meeting_open_id_8b5c196b742540e5996f6e307c807f8c",
            "hy_source": "web",
            "lz_expire": "1786705763744",
            "_qimei_i_1": "22c12b829d5a508dc491fd655a8775b6f2b8f0f9405d5584b4db29582493206c616330c139d8eadc8386a7fd",
            "hy_anon_token": "8tE8bq6InCxff5mUqQZfc9aGHP6NPD80Cr/k258SiLJ9CYW8HiMzU5pREYyvnbvj0BG1Q9/KnkehH1aSnt0onsNBIbySGO3JvjToZbIP+3GSrmyTOVg++T/m/xSnFwk/B10kOImjhshjUW4cevfYKIuuseR6aAov68SyU7i17gLVyaZwRJTzmrGOpeW5XXNPvYpEVJaJ+bWUMSCZ9yxNlXvv2BCWeZZxZf0laFTtUUy2ylSWzeDs2PMOY4z2z7AfAt88W4xWE1+blwDE4s5x2SZb38UAnO48ttV0CtwVpc/8ruyR4OUxTQY7rSUpi6wPn5sK05RbcyC6URMey8jxSRLB0tzZp09Acu67gzv7CE180ip9eUUKZGL0zXmT3dToYli81gX7bASq0N5GKv9ET3gvWAUIfCFOyvwypEsSe9pGiGPm6oeZ0bI/C/f/RphKlhem1CenA38BcFgVsAHRNAobl6DfVhs53GkHVwaYxApyDVoAfO7b6bIzkGYXKaq5wALtrciLmsSUtA2alXWogbbEJ0sCSD2JfqsfGednoCPoFgDMEiljVUOiuKpL3YKno5E921AEMyFqZI/e8oQRBIBEMqI0GQ0D/XQP22kBlQt5pn5CPNvBl80Rg6N76wbmDsALWcdh4dX4NCYoZKOEuA==",
            "_ga_6P1G7NCG3R": "GS2.1.s1786687766$o2$g0$t1786687766$j60$l0$h88484638"
        }
        result = post_json(api_url, body, cookies)
        print(result)
