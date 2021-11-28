# 674 https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    """
    Runtime: 68 ms, faster than 95.56% of Python3 online submissions for Longest Continuous Increasing Subsequence.
    Memory Usage: 15.4 MB, less than 11.47% of Python3 online submissions for Longest Continuous Increasing Subsequence.
    """
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        m = 1
        cnt = 1
        l = nums[0]
        for x in nums[1:]:
            if l < x:
                cnt += 1
            else:
                cnt = 1

            if m < cnt:
                m = cnt

            l = x
        return m


def request_ppu_vend(asinList, requests, endpoint, marketplaceId, locale, ppu_list):
    asinList = list(filter(None, asinList))
    for i in range(0, len(asinList), 6):
        asins = str(asinList[i:i+6]).replace("'", "\"")
        encoded_asins = urllib.parse.quote(asins)
        response = requests.get(
            'http://{}/datapath/query/ppuVend/batch/ppuOrchestrate/computePricePerUnitBatch/-/{}/{}/{}'.format(
                endpoint, marketplaceId, locale, encoded_asins),
            headers={'Authorization': 'SableBasic PPUDatapath', 'Accept': 'application/json'}, stream=True)
        json_response = json.loads(response.raw.read())
        process_ppu_vend(json_response, ppu_list)
        time.sleep(0.1)