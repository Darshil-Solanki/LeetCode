/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    if (arr.length==0) return [];
    let res = [];
    let i = 0;
    for(; i<arr.length-size;){
        res.push(arr.slice(i, i+size));
        i+=size;
    }
    res.push(arr.slice(i,arr.length));
    return res;
};
