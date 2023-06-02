class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """ ハイフンを取り除く """
        edit_s = s.replace('-', '').upper()
        list_s = list(edit_s)

        """ -の数を取得 """
        dash_num =  len(edit_s) / k
        remainder = len(edit_s) % k
        if remainder:
            dash_num += 1

        """ 答えの文字列を生成 """
        ans_list = list()
        list_s.reverse()
        for i, s in enumerate(list_s, start=1):
            ans_list.insert(0, s)
            if i % k == 0 and i != len(edit_s):
                ans_list.insert(0, "-")

        ans_s = "".join(ans_list)
        return ans_s
        
        




