/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject)=>{
        let length = functions.length;
        let res = [];
        let flag = false;
        functions.forEach((fn, idx)=>{
            fn().then(value=>{
                    if (flag) return;
                    res[idx]=value;
                    length--;
                    if (length===0){
                        resolve(res);
                    }
                }).catch(error=>{
                    if (!flag){
                        flag = true;
                        reject(error);
                    }
                });
        });
    });
}

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
