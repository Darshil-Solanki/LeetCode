/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if (n===0) return arr;
    let res = []
    arr.forEach((item)=>{
        if(item instanceof Array) res.push(...flat(item, n-1));
        else res.push(item);
    });
    return res
};

// var flat = function (arr, n) {
//     if (n===0) return arr;
//     let res = []
//     const flatten = (arr, n)=>{
//         for(let i = 0; i<arr.length; i++){
//             if(Array.isArray(arr[i]) && n>0)
//                 flatten(arr[i], n-1);
//             else
//                 res.push(arr[i]);
//         }
//         return res
//     }
//     return flatten(arr, n)
// };
