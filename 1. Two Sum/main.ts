function twoSum(nums: number[], target: number): number[] {
    for(let i = 0; i < nums.length; i++) {
        for(let j = i; j < nums.length; j++) {
            if(i!= j && nums[i] + nums[j] == target) {
                return [i,j]
            }
        }
    }
    return [];
};


function main() {
    console.log(twoSum([2,7,11,15], 9)); // [0,1]
}

