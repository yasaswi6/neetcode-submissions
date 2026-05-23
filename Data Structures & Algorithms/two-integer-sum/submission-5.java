class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> sum = new HashMap<>();
        int[] indices = new int[2];
        for(int i = 0;i < nums.length;i++){
            sum.put(nums[i],i);
        }
        int remaining = 0;
        for(int i = 0;i < nums.length;i++){
            remaining = target - nums[i];
            sum.remove(nums[i],i);
            if(sum.containsKey(remaining)){
                indices[0] = i;
                indices[1] = sum.get(remaining);
                break;
            }
        }
        return indices;
    }
}
