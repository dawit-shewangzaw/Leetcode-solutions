class Solution {
	public int[] intersection(int[] nums1, int[] nums2){
		List<Integer> list = new ArrayList<>();
		List<Integer> list2 = new ArrayList<>();
		List<Integer> ans = new ArrayList<>();
		
		for(int n : nums1){
			list.add(n);
		}
		for(int n2 : nums2){
			list2.add(n2);
		}
		for(int num : list){
			if(list2.contains(num)){
				ans.add(num);
			}
		}

		Set<Integer> set = new HashSet<>(ans);
		ans.clear();
		ans.addAll(set);

		return ans.stream()
			.mapToInt(Integer::intValue)
			.toArray();
		}
}

		