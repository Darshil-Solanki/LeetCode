/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let res = []
    let mp = new Map();
    arr1.forEach((item, idx)=>{ res.push(item); mp.set(item.id, idx); });
    arr2.forEach((item)=>{ 
        if(mp.has(item.id)){
            let idx = mp.get(item.id);
            for(let key in item){
                res[idx][key]=item[key];
            }
        }
        else
            res.push(item);
    });
    return res.sort((a, b)=>a.id-b.id);
};
