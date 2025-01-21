/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let obj = {};
    this.forEach(item=>{
        let ans = fn(item);
        if (ans in obj)
            obj[ans].push(item);
        else
            obj[ans] = [item];
    });
    return obj;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
