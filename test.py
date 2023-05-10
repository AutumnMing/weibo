import requests
from urllib.parse import urlencode
base_url = 'https://vipact.api.mgtv.com/api/v1/act/vote/charlist?'
params = {
    'ticket': '75CABB60712F32F18EA5A910400B77A4',
    'act_name': '20230414cf2023',
    'count': '50',
    'invoker': 'mobile-zhifubao',
    '_dx_seq_id': '6d93ac64-2f2d-ce45-b08a-8128ea244cd4',
    'v': 'v4'
}
url = base_url + urlencode(params)
res = requests.get(url, params=params)
print(res.json())
