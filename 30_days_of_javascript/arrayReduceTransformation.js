/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    // for(let i = 0; i<nums.length; i++){
    //     init=fn(init, nums[i])
    // }
    nums.forEach((item, i)=>{init=fn(init, item)})
    return init;
};
