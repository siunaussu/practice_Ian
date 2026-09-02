
def pay_interface() -> dict:
    """待开发完成"""
    pass

def pay():
    result = pay_interface()

    if result['code'] == 200:
        return  "支付成功"
    elif result['code'] == 403:
        return "支付失败"
    else:
        return  "支付异常"


