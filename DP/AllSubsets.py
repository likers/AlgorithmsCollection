from copy import deepcopy
class Solution:
	def getSubsets(self, parentSet):
		print parentSet
		result = [[]]
		for item in parentSet:
			holder = deepcopy(result)
			for set in holder:
				set.append(item)
				result.append(set)
			
		print result

so = Solution()
so.getSubsets([1,2,3])


