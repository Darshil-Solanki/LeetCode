/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.arr = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    // let ans = 0
    // this.arr.forEach(item=>ans+=item);
    // return ans
    return this.arr.reduce((accum, item)=>accum+item, 0);
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    // let ans = "";
    // this.arr.forEach(item=>ans+=(item+','));
    // return "["+ans.slice(0, ans.length-1)+"]";
    return "["+this.arr.toString()+"]";
}
/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
