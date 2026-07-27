class Solution {
    public int maxProduct(int[] nums) {

        int max = 0;
        int sMax = 0;

        for (int i =0; i< nums.length; i++) {

            if (max <= nums[i]){

                sMax = max;
                max = nums[i];
            }else if (sMax < nums[i] && nums[i] != max) {
                sMax = nums[i];
            }
        }

        return (max -1) * (sMax -1);
        
    }
}