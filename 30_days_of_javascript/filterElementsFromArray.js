/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let newArr = [];
    for(let i = 0; i<arr.length; i++){
        if (fn(arr[i], i)) newArr.push(arr[i]);
    }
    // faster method
    // arr.forEach((item, i)=>{if (fn(item, i)) newArr.push(item);});
    return newArr;
};
