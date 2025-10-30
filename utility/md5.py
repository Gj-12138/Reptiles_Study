"""

    sign    --    md5--加密

"""
# import hashlib
#
# # 已知样本：_ts和对应的sign
# samples = [
#     ("1761827643218", "19e36636801238f39aac9d63b83ba62e"),
#     ("1761827746097", "9af3a94f61cf6f61a463bb074818ec29"),
#     ("1761827775032", "dc989afbae23f022a5404237c8721d86"),
#     ("1761827791421", "c79dc6a714a90f76518b4a1c534ed306")
# ]
#
# # 尝试可能的密钥（可扩展为字典攻击）
# possible_secrets = [
#     "mashangpa", "msp", "api", "secret", "key",
#     "123456", "4", "page1", "mashangpa4","tuling"
# ]
#
# for secret in possible_secrets:
#     # 验证该密钥是否符合所有样本
#     match = True
#     for ts, target_sign in samples:
#         # 生成签名：MD5(ts字符串 + 密钥)
#         sign_str =secret+ts
#         generated_sign = hashlib.md5(sign_str.encode()).hexdigest()
#         if generated_sign != target_sign:
#             match = False
#             break
#     if match:
#         print(f"找到密钥：{secret}")
#         print(f"验证通过，签名规则：MD5(str(_ts) + '{secret}')")
#         break
# else:
#     print("未找到匹配的短密钥，可能是更长的自定义密钥（建议分析前端JS）")